# Flask-HTML
HTML generator for Flask applications.

## Installation
```bash
pip install git+https://github.com/Odya-LLC/flask_html.git@main
```

## Usage
```python
from flask_html import Page, Head
from flask_html.tags import Style, Body, Div, P
@app.route('/')
def index():
    head = Head('Title', ['link to css'],['link to js'], [{"meta property": "value"}])
    page = Page(head)
    body = Body(page, styles=Style(color="red", padding_top="15px"),classes=['class1', 'class2'], id='body_id',elements=[
        Div(styles=Style(margin="10px"), classes=['class1', 'class2'], id='div_id', elements=[
            P(styles=Style(color="blue"), classes=['class1', 'class2'], id='p_id', elements=[
                "Hello World"
            ])
        ])
    ])
    return page.render(body)
```
