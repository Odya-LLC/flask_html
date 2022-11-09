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
    __tag = None
    __classes = None
    __id = None
    __props = None
    page = None
    elements = []
    styles = None
    js = ""
    def register_style(self):
        if self.styles:
            self.page.register_style(self.styles[0], self.styles[1])
        if self.js:
            self.page.register_js(self.js)
        for i in range(len(self.elements)):
            if isinstance(self.elements[i], Item):
                self.elements[i].page = self.page
                self.elements[i].register_style()
    
    
    def get_tag(self):
        return self.__tag
    
    def __init__(self, page: Page = None, classes: List[str] = [], id: str = None, style: Style = None, tag: str = "div", content: List[object] = [], props: Dict[str, str] = {}):

        classes = [] if len(classes) == 0 else classes
        props = {} if len(props) == 0 else props
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
        if page:
            self.page = page
        self.elements = content
        self._cls = classes
        _cl = None
        if style:
            _cl = self.__generate_style(style)
            self._cls.append(_cl)
        
        if len(self._cls) > 0:
            self.__append_classes()
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
        """Render HTML element

        Returns:
            str: String HTML element
        """        
        _cnt = ""
        for item in self.elements:
            _cnt += str(item)
        return self.item.format(tag=self.__tag, classes=self.__classes, id=self.__id, content=_cnt, props=self.__props)

    def __append_classes(self):
        classes = self._cls
        
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
        self.hash_code = "o" + sha256("{secret}{styles}".format(secret=current_app.config.get("SECRET_KEY", "123123"), styles=styles).encode()).hexdigest()[:5]
        return self.__register_style(self.hash_code, styles)

    def __register_style(self, hash_code: str, styles: str):
        self.styles = (hash_code, styles)
        return hash_code