from hashlib import sha256
from . import Page
from typing import Dict, List
from flask import current_app

class Style:
    """Inline CSS style
        Keyword arguments:
            keyword -- value
        Example:
            Style(color="red", padding_top="blue")
    """     
    def __init__(self, **kwargs):
        """Inline CSS style
        Keyword arguments:
            keyword -- value
        Example:
            Style(color="red", padding_top="blue")
        """       
        self.style = ""
        for key, value in kwargs.items():
            if "_" in key:
                key = key.replace("_", "-")
            self.style+="{}:{};\n".format(key, value)

    def __str__(self):
        return self.render()
    
    def __repr__(self):
        return self.render()

    def render(self):
        return self.style
    
class Item:
    
    item  = "<{tag} {classes} {id} {props}>{content}</{tag}>"
    
    page = None
    __classes = []
    __id = None
    __styles = []
    __tag = None
    __elements = []
    __props = {}
    __js = None
    
    def register_style(self):
        if self.__styles:
            self.page.register_style(self.__styles[0], self.__styles[1])
        if self.__js:
            self.page.register_js(self.__js)
        for i in range(len(self.__elements)):
            if isinstance(self.__elements[i], Item):
                self.__elements[i].page = self.page
                self.__elements[i].register_style()
    
    def __init__(self, page: Page = None, classes: List[str] = [], id: str = None, style: Style = None, tag: str = "div", content: List[object] = [], props: Dict[str, str] = {}):
        """Base template for all HTML elements

        Args:
            page (Page, optional): Page element, uses for Body tag. Defaults to None.
            classes (List[str], optional): List of class names for tag. Defaults to [].
            id (str, optional): Unique ID for tag. Defaults to None.
            style (Style, optional): Custom inline styles for tag. Defaults to None.
            tag (str, optional): Tag name. Defaults to "div".
            content (List[object], optional): List of Elements. Defaults to [].
            props (Dict[str, str], optional): Tag rpoperties. Defaults to {}.
        """   
        
        classes = [] if len(classes) == 0 else classes
        props = {} if len(props) == 0 else props
        
        if page:
            self.page = page
        self.__elements = content
        self.__classes = classes
        if style:
            _cl = self.__generate_style(style)
            self.__classes.append(_cl)
        if id:
            self.__id = id
        self.__tag = tag
        self.__props = props
        
    def __str__(self):
        return self.render()
    
    def render(self):
        _id = ""
        if self.__id:
            _id = "id='{}'".format(self.__id)
        _classes = ""
        if len(self.__classes) > 0:
            _classes = "class='"
            for _class in self.__classes:
                _classes += _class + " "
            _classes = _classes.rstrip(" ")
            _classes = _classes + "'"
        _props = ""
        if len(self.__props) > 0:
            for key, value in self.__props.items():
                _props += "{}='{}' ".format(key, value)
            _props = _props.rstrip(" ")
        _cnt = ""
        for item in self.__elements:
            _cnt += str(item)
        return self.item.format(tag=self.__tag, classes=_classes, id=_id, content=_cnt, props=_props)
        
    
    def __generate_style(self, style: Style):
        styles = style.render()
        self.hash_code = "o" + sha256("{secret}{styles}".format(secret=current_app.config.get("SECRET_KEY", "123123"), styles=styles).encode()).hexdigest()[:5]
        return self.__register_style(self.hash_code, styles)

    def __register_style(self, hash_code: str, styles: str):
        self.__styles = (hash_code, styles)
        return hash_code
    
    def on(self, event, func):
        if not self.__id:
            self.__id = "o" + sha256("{secret}{tag}{event}{func}".format(secret=current_app.config.get("SECRET_KEY", "123123"), tag=str(self.__tag), event=event, func=func).encode()).hexdigest()[:5]
        self.__js = "document.getElementById('{}').addEventListener('{}', function() {{ {} }});".format(self.__id, event, func)
        return self