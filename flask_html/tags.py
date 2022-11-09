from typing import Dict, List
from . import Page
from .core import Style, Item

class Body(Item):
    def __init__(self, page: Page, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[object] = [], props: Dict[str, str] = {}):
        """Body HTML element

        Args:
            page (Page): Page element, uses for Body tag.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """        
        super().__init__(page=page, style=styles, classes=classes, id=id, tag="body", content=elements, props=props)
        self.register_style()

class Div(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Div HTML element

        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """        
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
class H4(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        super().__init__(None, classes, id, styles, "h4", elements, props)
class H5(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        super().__init__(None, classes, id, styles, "h5", elements, props)
class H6(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        super().__init__(None, classes, id, styles, "h6", elements, props)

class Header(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        super().__init__(None, classes, id, styles, "header", elements, props)

class Footer(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        super().__init__(None, classes, id, styles, "footer", elements, props)
        
class Nav(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        super().__init__(None, classes, id, styles, "nav", elements, props)

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