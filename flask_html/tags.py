from typing import Dict, List
from hashlib import sha256
from time import gmtime, strftime
from . import Page

        

class Style:
    
    def __init__(self, **kwargs):
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
    __tag = None
    __classes = None
    __id = None
    __props = None
    page = None
    elements = []
    styles = ""
    
    def register_style(self):
        if self.styles:
            self.page.register_style(self.styles)
        for item in self.elements:
            if isinstance(item, Item):
                item.page = self.page
                item.register_style()
    
    def __init__(self, page: Page = None, classes: List[str] = [], id: str = None, style: Style = None, tag: str = "div", content: List[object] = [], props: Dict[str, str] = {}):
        if page:
            self.page = page
        self.elements = content
        _cl = None
        if style:
            _cl = self.__generate_style(style)
            classes.append(_cl)
        if len(classes) > 0:
            self.__append_classes(classes)
        else:
            self.__classes = ""
        if id:
            self.__id = "id='{}'".format(id)
        else:
            self.__id = ""
        self.__tag = tag
        if len(props) > 0:
            _props = ""
            for key, value in props.items():
                _props += "{}='{}' ".format(key, value)
            self.__props = _props.rstrip(" ")
        else:
            self.__props = ""
        
    def __str__(self):
        return self.render()
    
    def __repr__(self):
        return self.render()
    
    def render(self):
        _cnt = ""
        for item in self.elements:
            _cnt += str(item)
        return self.item.format(tag=self.__tag, classes=self.__classes, id=self.__id, content=_cnt, props=self.__props)

    def __append_classes(self,classes: List[str] = None):
        print(classes)
        _res = ""
        if classes:
            _res = "class='"
            for _class in classes:
                _res += _class + " "
            _res = _res.rstrip(" ")
            _res = _res + "'"
        self.__classes = _res
        
    def __generate_style(self, style: Style):
        styles = style.render()
        self.hash_code = "o" + sha256("{content}{styles}{now}".format(content="lklkd4dkf", styles=styles, now=strftime("%Y-%m-%d %H:%M",gmtime())).encode()).hexdigest()[:5]
        return self.__register_style(self.hash_code, styles)

    def __register_style(self, hash_code: str, styles: str):
        _st = """
        .{hash_code} {{
        {styles}
        }}
        """.format(hash_code = hash_code, styles=styles)
        self.styles = _st
        return hash_code

class Body(Item):
    def __init__(self, page: Page, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[object] = [], props: Dict[str, str] = {}):
        super().__init__(page=page, style=styles, classes=classes, id=id, tag="body", content=elements, props=props)
        self.register_style()

class Div(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        super().__init__(None, classes, id, styles, "div", elements, props)

class P(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        super().__init__(None, classes, id, styles, "p", elements, props)

class B(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        super().__init__(None, classes, id, styles, "b", elements, props)

class Span(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        super().__init__(None, classes, id, styles, "span", elements, props)

class Ul(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        super().__init__(None, classes, id, styles, "ul", elements, props)
        
class Li(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        super().__init__(None, classes, id, styles, "li", elements, props)
        
class H1(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        super().__init__(None, classes, id, styles, "h1", elements, props)
        
class H2(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        super().__init__(None, classes, id, styles, "h2", elements, props)
        
class H3(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        super().__init__(None, classes, id, styles, "h3", elements, props)

class Header(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        super().__init__(None, classes, id, styles, "header", elements, props)

class Footer(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        super().__init__(None, classes, id, styles, "footer", elements, props)
        
class Nav(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        super().__init__(None, classes, id, styles, "nav", elements, props)

class Footer(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        super().__init__(None, classes, id, styles, "footer", elements, props)

class Img(Item):
    def __init__(self, src: str, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        props['src'] = src
        super().__init__(None, classes, id, styles, "img", elements, props)
        
class Button(Item):
    def __init__(self, _type: str, title: str, styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        props['type'] = _type
        elements = [title]
        super().__init__(None, classes, id, styles, "button", elements, props)

class A(Item):
    def __init__(self, href: str, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        props['href'] = href
        super().__init__(None, classes, id, styles, "a", elements, props)

class Form(Item):
    def __init__(self, method: str, action: str, enctype: str = "multipart/form-data", styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        props['method'] = method
        props['action'] = action
        props['enctype'] = enctype
        super().__init__(None, classes, id, styles, "form", elements, props)

class Input(Item):
    def __init__(self, _type: str, name: str, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        props['type'] = _type
        props['name'] = name
        super().__init__(None, classes, id, styles, "input", elements, props)