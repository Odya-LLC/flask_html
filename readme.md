# Flask-HTML
![Flask](https://img.shields.io/static/v1?label=under&message=Development&color=yellow&logo=flask)
![GitHub top language](https://img.shields.io/github/languages/top/Odya-LLC/flask_html)
![LICENCE](https://img.shields.io/github/license/Odya-LLC/flask_html)
![Odya](https://img.shields.io/static/v1?label=Developed_by&message=Odya&color=green&logo=python)



HTML generator for Flask applications. Make your HTML code more readable and easier to maintain.
## Installation
```bash
pip install flask_html
```

## Usage
```python
from flask_html import Page, Head
from flask_html.tags import Style, Body, Div, P
from flask import request
@app.route('/')
def index():
    head = Head('Title', [],['https://code.jquery.com/jquery-3.6.1.min.js'], [{"meta_property": "value"}])
    page = Page(head)
    page.register_js("""
                    $(document).ready(function(){
                        $("body").append("<p>hello world</p>");
                    })
                     
                     """)
    body = Body(page, styles=Style(color="red", padding_top="15px"),classes=['class1', 'class2'], id='body_id',elements=[
        Div(styles=Style(margin="10px"), classes=['class1', 'class2'], id='div_id', elements=[
            P(styles=Style(color="blue"), classes=['class1', 'class2'], id='p_id', elements=[
                "Hello World"
            ])
        ])
    ])
    return page.render(body, request)
```

## Elements

### Example of Div elements
```python
"""Div HTML element

Args:
    styles (Style, optional): Inline css styles. Defaults to None.
    classes (List[str], optional): List of class names. Defaults to [].
    id (str, optional): Unique ID. Defaults to None.
    elements (List[object], optional): List of child elements. Defaults to [].
    props (Dict[str, str], optional): Additional tag properties. Defaults to {}.
"""
Div(styles=None, classes=[], id=None, elements=[], props={})
```
### All elements

 - Div
 - P
 - B
 - H1-H6
 - A
 - Img
 - Span
 - Ul
 - Li
 - Button
 - Input
 - Form
 - Header
 - Footer
 - Nav

## License
This project is licensed under the MIT License (see the `LICENSE` file for details).