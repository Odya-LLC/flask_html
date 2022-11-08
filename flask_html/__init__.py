from typing import Dict, List
from flask import request, make_response

class Head:
    custom_styles = ""
    def __init__(self, title: str, styles : List[str] = [], scripts : List[str] = [], metas : List[Dict[str, str]] = []):
        styles.append(request.url + "?css=1")
        _cont = """
        <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">"""
        for meta in metas:
            _cont += """
            <meta """
            for key, value in meta.items():
                _cont += "{}='{}' ".format(key, value)
            _cont += """>"""
        _cont += """<title>{title}</title>
        """.format(title=title)
        for style in styles:
            _cont += """
            <link rel="stylesheet" href="{style}">
            """.format(style=style)
        for script in scripts:
            _cont += """
            <script src="{script}"></script>
            """.format(script=script)
        
        
        self.content = _cont
    
    def __str__(self):
        return self.content
    
    def __repr__(self):
        return self.content
    
    def render(self):
        if self.custom_styles != "":
            self.content+="""
            <style>
            {styles}
            </style>
            """.format(styles=self.custom_styles)
        self.content += """</head>"""
        return self.content
    
    def register_style(self, style: str):
        self.custom_styles += style

class Page:
    def __init__(self, head : Head, lang: str = "en"):
        self.head = head
        self.lang = lang
    custom_classes = ""
    def render(self, content, request):
        css = request.args.get("css")
        if css:
            resp = make_response(self.custom_classes)
            resp.headers['Content-Type'] = 'text/css ;charset=utf-8'
            return resp
        content = """
            <!DOCTYPE html>
                <html lang="{lang}">
                {head}
                <body>
                {content}
                </body>
                </html>
            """.format(lang=self.lang, head = self.head.render(), content=str(content))
        return content
    
    def register_style(self, style: str):
        self.custom_classes += style