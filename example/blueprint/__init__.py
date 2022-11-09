from flask import Blueprint, request
from flask_html import Page, Head
from flask_html.core import Style
from flask_html.tags import Body, Div, P, Table, Tbody, Thead, Td, Tr, Th
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
    table = Table(styles=Style(padding="10px", border="2px solid black"), id='table_id', elements=[
        Thead(styles=Style(padding="10px"), id='thead_id', elements=[
            Tr(id='tr_id', elements=[
                Th("ID",styles=Style(padding="10px")),
                Th("Name",styles=Style(padding="10px")),
                Th("Age",styles=Style(padding="10px"))
            ]),
        ]),
        Tbody(styles=Style(padding="10px"), id='tbody_id', elements=[
            Tr(id='tr_id', elements=[
                Td("1",styles=Style(padding="10px")),
                Td("Odya",styles=Style(padding="10px")),
                Td("22",styles=Style(padding="10px"))
            ]),
            Tr(id='tr_id', elements=[
                Td("2",styles=Style(padding="10px")),
                Td("ValOdya",styles=Style(padding="10px")),
                Td("23",styles=Style(padding="10px"))
            ]),
        ])
    ])
    
    body = Body(page, styles=Style(color="red", padding_top="15px"),classes=['class1', 'class2'], id='body_id',elements=[
        Div(styles=Style(margin="10px"), classes=['class1', 'class2'], id='div_id', elements=[
            P(styles=Style(color="blue"), id='p_id', elements=[
                "Hello World"
            ]),
            P(styles=Style(color="blue"), id='p_id', elements=[
                "Hello World"
            ])
        ]),
        table
    ])
    return page.render(body, request)