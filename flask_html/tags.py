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

# -------------------- A ----------------------------

class A(Item):
    def __init__(self, href: str, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        props['href'] = href
        super().__init__(None, classes, id, styles, "a", elements, props)

class Abbr(Item):
    def __init__(self, title: str, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Abbr HTML element

        Args:
            title (str): The title of the element
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """  
        props['title'] = title
        super().__init__(None, classes, id, styles, "abbr", elements, props)

class Address(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Artice HTML element

        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """  
        super().__init__(None, classes, id, styles, "address", elements, props)

class Article(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Artice HTML element

        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """  
        super().__init__(None, classes, id, styles, "article", elements, props)

class Aside(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Aside HTML element

        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """  
        super().__init__(None, classes, id, styles, "aside", elements, props)

class Audio(Item):
    def __init__(self, src: str, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Audio HTML element

        Args:
            src (str): The source of the audio file
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """  
        new_props = props.copy()
        new_props['src'] = src
        if 'controls' not in props:
            props['controls']="controls"
        source = Item(None, [], [], [], "source", [], new_props)
        elements.append(source)
        super().__init__(None, classes, id, styles, "audio", elements, props)

# -------------------- B ----------------------------

class B(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """B HTML element (bold)
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "b", elements, props)
        

class Button(Item):
    def __init__(self, title: str, _type: str="button", styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        """Button HTML element
        
        Args:
            _type (str): The type of button (submit, reset, button)
            title (str): The title of the button
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        props['type'] = _type
        elements = [title]
        super().__init__(None, classes, id, styles, "button", elements, props)

class Blockquote(Item):
    def __init__(self, cite: str = None, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Blockquote HTML element
        
        Args:
            cite (str): The source of the quote. Defaults to None.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        if cite:
            props['cite'] = cite
        super().__init__(None, classes, id, styles, "blockquote", elements, props)

class Br(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        """Br HTML element (line break)
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "br", [], props)
        
# -------------------- C ----------------------------

class Canvas(Item):
    def __init__(self, width: int, height: int, styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        """Canvas HTML element
        
        Args:
            width (int): The width of the canvas
            height (int): The height of the canvas
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        props['width'] = width
        props['height'] = height
        super().__init__(None, classes, id, styles, "canvas", [], props)
        
class Caption(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Caption HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "caption", elements, props)

class Cite(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Cite HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "cite", elements, props)

class Code(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Code HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "code", elements, props)

class Col(Item):
    def __init__(self, span: int = None, width: int = None, styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        """Col HTML element
        
        Args:
            span (int): The number of columns to span. Defaults to None.
            width (int): The width of the column. Defaults to None.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        if span:
            props['span'] = span
        if width:
            props['width'] = width
        super().__init__(None, classes, id, styles, "col", [], props)

class Colgroup(Item):
    def __init__(self, span: int = None, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Colgroup HTML element
        
        Args:
            span (int): The number of columns to span. Defaults to None.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        if span:
            props['span'] = span
        super().__init__(None, classes, id, styles, "colgroup", elements, props)

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

class Datagrid(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Datagrid HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[Item], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "datagrid", elements, props)

class Dd(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Dd HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "dd", elements, props)

class Del(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Del HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "del", elements, props)

class Details(Item):
    def __init__(self, open: bool = False, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Details HTML element
        
        Args:
            open (bool): Whether the details are open or not. Defaults to False.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        if open:
            props['open'] = open
        super().__init__(None, classes, id, styles, "details", elements, props)

class Dl(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Dl HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "dl", elements, props)

class Dt(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Dt HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "dt", elements, props)

class Em(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Em HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "em", elements, props)

class Embed(Item):
    def __init__(self, src: str, type: str, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Embed HTML element
        
        Args:
            src (str): URL of the embeddable content.
            type (str): MIME type of the embeddable content.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        props['src'] = src
        props['type'] = type
        super().__init__(None, classes, id, styles, "embed", elements, props)

class Fieldset(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Fieldset HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "fieldset", elements, props)
        
class Figcaption(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Figcaption HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "figcaption", elements, props)

class Figure(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Figure HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "figure", elements, props)

class Form(Item):
    def __init__(self, method: str, action: str, enctype: str = "multipart/form-data", styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Form HTML element
        
        Args:
            method (str): The HTTP method to use when sending form data.
            action (str): The URL to send the form data to.
            enctype (str, optional): The type of content that is used to submit the form to the server. Defaults to "multipart/form-data".
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        props['method'] = method
        props['action'] = action
        props['enctype'] = enctype
        super().__init__(None, classes, id, styles, "form", elements, props)
        
class Footer(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Footer HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "footer", elements, props)

class H1(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """H1 HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "h1", elements, props)
        
class H2(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """H2 HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "h2", elements, props)
        
class H3(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """H3 HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "h3", elements, props)

class H4(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """H4 HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "h4", elements, props)

class H5(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """H5 HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "h5", elements, props)

class H6(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """H6 HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "h6", elements, props)

class Header(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Header HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "header", elements, props)

class Hr(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        """Hr HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "hr", [], props)

# ------------------ I ------------------ #

class I(Item):
    def __init__(self, text: str = None, styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        """I HTML element
        
        Args:
            text (str, optional): Text content. Defaults to None.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        elements = [text] if text else []
        super().__init__(None, classes, id, styles, "i", elements, props)

class Iframe(Item):
    def __init__(self, src: str = None, styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        """Iframe HTML element
        
        Args:
            src (str, optional): Source URL. Defaults to None.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        if src:
            props["src"] = src
        super().__init__(None, classes, id, styles, "iframe", [], props)

class Img(Item):
    def __init__(self, src: str, styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        """Img HTML element
        
        Args:
            src (str, optional): Source URL. Defaults to None.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        if src:
            props["src"] = src
        super().__init__(None, classes, id, styles, "img", [], props)
        
class Input(Item):
    def __init__(self, _type: str, name: str, styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        """Input HTML element
        
        Args:
            _type (str): Input type.
            name (str): Input name.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        props['type'] = _type
        props['name'] = name
        super().__init__(None, classes, id, styles, "input", [], props)
        
class Ins(Item):
    def __init__(self, text: str = None, styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        """Ins HTML element
        
        Args:
            text (str, optional): Text content. Defaults to None.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        elements = [text] if text else []
        super().__init__(text, classes, id, styles, "ins", elements, props)
        
class Label(Item):
    def __init__(self, _for: str = None, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Label HTML element
        
        Args:
            _for (str, optional): For property. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        if _for:
            props['for'] = _for
        super().__init__(None, classes, id, styles, "label", elements, props)

class Li(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Li HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "li", elements, props)

class Legend(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Legend HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "legend", elements, props)

class Link(Item):
    def __init__(self, href: str, rel: str = None, styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        """Link HTML element
        
        Args:
            href (str): Source URL.
            rel (str, optional): Relationship. Defaults to None.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        props["href"] = href
        if rel:
            props["rel"] = rel
        super().__init__(None, classes, id, styles, "link", [], props)
        
# ---------------- N ----------------

class Nav(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Nav HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "nav", elements, props)


# ---------------- O ----------------

class Ol(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Ol HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "ol", elements, props)
        
class Option(Item):
    def __init__(self, value: str, text: str = None, selected: bool = False, styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        """Option HTML element
        
        Args:
            value (str): Option value.
            text (str, optional): Option text. Defaults to None.
            selected (bool, optional): Is selected. Defaults to False.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        elements = [text] if text else []
        props['value'] = value
        if selected:
            props['selected'] = 'selected'
        super().__init__(None, classes, id, styles, "option", elements, props)
        
class Optgroup(Item):
    def __init__(self, label: str, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Optgroup HTML element
        
        Args:
            label (str): Group label.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        props['label'] = label
        super().__init__(None, classes, id, styles, "optgroup", elements, props)
    
# ---------------- P ----------------

class P(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """P HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "p", elements, props)

class Param(Item):
    def __init__(self, name: str, value: str, styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        """Param HTML element
        
        Args:
            name (str): Parameter name.
            value (str): Parameter value.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        props['name'] = name
        props['value'] = value
        super().__init__(None, classes, id, styles, "param", [], props)

class Pre(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Pre HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "pre", elements, props)

class Progress(Item):
    def __init__(self, value: int, max: int = 100, styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        """Progress HTML element
        
        Args:
            value (int): Progress value.
            max (int, optional): Maximum value. Defaults to 100.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        props['value'] = value
        props['max'] = max
        super().__init__(None, classes, id, styles, "progress", [], props)
        
# ---------------- Q ----------------

class Q(Item):
    def __init__(self, text: str, cite: str = None, styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        """Q HTML element
        
        Args:
            text (str): Quote text.
            cite (str): Quote source.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        props['cite'] = cite
        super().__init__(None, classes, id, styles, "q", [text], props)

# ---------------- S ----------------

class S(Item):
    def __init__(self, text: str, styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        """S HTML element
        
        Args:
            text (str): Text.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "s", [text], props)

class Small(Item):
    def __init__(self, text: str, styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        """Small HTML element
        
        Args:
            text (str): Text.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "small", [text], props)

class Script(Item):
    def __init__(self, src: str = None, text: str = None, styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        """Script HTML element
        
        Args:
            src (str): Script source.
            text (str): Script text.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        elements = None
        if src:
            props['src'] = src
        elif text:
            elements = [text]
        super().__init__(None, classes, id, styles, "script", elements, props)
        
class Section(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Section HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "section", elements, props)

class Select(Item):
    def __init__(self, options: List[Option] = [], styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        """Select HTML element
        
        Args:
            options (List[Option]): List of options.
            selected (int, optional): Selected option. Defaults to 0.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        
        super().__init__(None, classes, id, styles, "select", options, props)

class Source(Item):
    def __init__(self, src: str, media: str = None, styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        """Source HTML element
        
        Args:
            src (str): Source.
            media (str): Media query.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        props['src'] = src
        props['media'] = media
        super().__init__(None, classes, id, styles, "source", [], props)
        
class Span(Item):
    def __init__(self, text: str, styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        """Span HTML element
        
        Args:
            text (str): Text.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "span", [text], props)

class Strong(Item):
    def __init__(self, text: str, styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        """Strong HTML element
        
        Args:
            text (str): Text.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "strong", [text], props)
        
class Style(Item):
    def __init__(self, text: str, styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        """Style HTML element
        
        Args:
            text (str): Text.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "style", [text], props)

class Sub(Item):
    def __init__(self, text: str, styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        """Sub HTML element
        
        Args:
            text (str): Text.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "sub", [text], props)
        
class Sup(Item):
    def __init__(self, text: str, styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        """Sup HTML element
        
        Args:
            text (str): Text.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "sup", [text], props)

class Strong(Item):
    def __init__(self, text: str, styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        """Strong HTML element
        
        Args:
            text (str): Text.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "strong", [text], props)

# ------------------ T ------------------

class Table(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Table HTML element
        
        Args:
            rows (List[List[Item]], optional): List of rows. Defaults to [].
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "table", elements, props)
        
class Tbody(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Tbody HTML element
        
        Args:
            rows (List[List[Item]], optional): List of rows. Defaults to [].
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "tbody", elements, props)

class Td(Item):
    def __init__(self, text: str, styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        """Td HTML element
        
        Args:
            text (str): Text.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "td", [text], props)
        
class Tfoot(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Tfoot HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "tfoot", elements, props)

class Th(Item):
    def __init__(self, text: str, styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        """Th HTML element
        
        Args:
            text (str): Text.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "th", [text], props)
        
class Thead(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Thead HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "thead", elements, props)

class Title(Item):
    def __init__(self, text: str, styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        """Title HTML element
        
        Args:
            text (str): Text.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "title", [text], props)
        
class Tr(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Tr HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "tr", elements, props)

# ------------------ U ----------------
        
class Ul(Item):
    def __init__(self, styles: Style = None, classes: List[str] = [], id: str = None, elements: List[Item] = [], props: Dict[str, str] = {}):
        """Ul HTML element
        
        Args:
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            elements (List[object], optional): List of child elements. Defaults to [].
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "ul", elements, props)

class U(Item):
    def __init__(self, text: str, styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        """U HTML element
        
        Args:
            text (str): Text.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        super().__init__(None, classes, id, styles, "u", [text], props)

class Video(Item):
    def __init__(self, src: str, styles: Style = None, classes: List[str] = [], id: str = None, props: Dict[str, str] = {}):
        """Video HTML element
        
        Args:
            src (str): Video source.
            styles (Style, optional): Inline css styles. Defaults to None.
            classes (List[str], optional): List of class names. Defaults to [].
            id (str, optional): Unique ID. Defaults to None.
            props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
        """
        props["src"] = src
        super().__init__(None, classes, id, styles, "video", [], props)


