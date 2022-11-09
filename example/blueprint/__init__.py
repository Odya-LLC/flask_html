from flask import Blueprint, request
from flask_html import Page, Head
from flask_html.tags import Body, Div, P, Style
pages = Blueprint("pages", __name__, url_prefix="/")


@pages.route("/")
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