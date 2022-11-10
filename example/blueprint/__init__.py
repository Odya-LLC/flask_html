from flask import Blueprint, request
from flask_html import Page, Head
from flask_html.core import Item
from flask_html.tags import H1, P, Body, Button, Div, Footer, Form, Header, Img, Input, Li, Section, Small, Ul, A
pages = Blueprint("pages", __name__, url_prefix="/")


@pages.route("/")
def index():
    head = Head('Title', ['https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css'],['https://code.jquery.com/jquery-3.6.1.min.js','https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js'], [{"meta_property": "value"}])
    page = Page(head)
    menu_items = {
        "Home": "/",
        "About": "/about",
        "Contact": "/contact",
        "Blog": "/blog"
    }
    card = Div(classes=['card', "shadow-sm"], elements=[
        Img(src="https://picsum.photos/300/150", classes=['card-img-top']),
        Div(classes=['card-body'], elements=[
            P(classes=['card-text'], elements=['Some quick example text to build on the card title and make up the bulk of the card content.']),
            Div(classes=['d-flex', 'justify-content-between', 'align-items-center'], elements=[
                Div(classes=['btn-group'], elements=[
                    Button('View', classes=['btn', 'btn-sm', 'btn-outline-secondary']),
                    Button('Edit', classes=['btn', 'btn-sm', 'btn-outline-secondary'])
                ]),
                Small('9 mins',classes=['text-muted'])
            ])
        ])
    ])
    section = Section(classes=['py-5', 'text-center', 'container'], elements=[
        Div(classes=['row', 'py-lg-5'], elements=[
            Div(classes=['col-lg-6', 'col-md-8', 'mx-auto'], elements=[
                H1(elements=['Album example'], classes=['fw-light']),
                P(elements=['Something short and leading about the collection below—its contents, the creator, etc. Make it short and sweet, but not too short so folks don’t simply skip over it entirely.'], classes=['lead', 'text-muted']),
                P(elements=[
                    A(elements=['Main call to action'], classes=['btn', 'btn-primary', 'my-2'], href="#"),
                    A(elements=['Secondary action'], classes=['btn', 'btn-secondary', 'my-2'], href="#")
                ])
            ])
        ])
    ])
    album = Div(classes=['album', 'py-5', 'bg-light'], elements=[
        Div(classes=['container'], elements=[
            Div(classes=['row', 'row-cols-1', 'row-cols-sm-2', 'row-cols-md-3', 'g-4'], elements=[
                Div(classes=['col'], elements=[
                    card
                ]) for x in range(9)
            ])
        ])
    ])
    main = Item(tag='main', content=[
        section,
        album
    ])
    footer = Footer(classes=['text-muted', 'py-5'], elements=[
        Div(classes=['container'], elements=[
            P(classes=['float-end', 'mb-1'], elements=['Back to top']),
            P(classes=['mb-1'], elements=['Album example is &copy; Bootstrap, but please download and customize it for yourself!']),
            P(classes=['mb-0'], elements=['New to Bootstrap? ', A(href="https://getbootstrap.com/", elements=['Visit the homepage'])])
        ])
    ])
    body = Body(page, id='body_id',elements=[
        Header(classes=['p-3', 'text-bg-dark'], elements=[
            Div(classes=['container'], elements=[
                Div(classes=['d-flex', 'flex-wrap', 'align-items-center', 'justify-content-center', 'justify-content-lg-start'], elements=[
                    Ul(classes=['nav', 'col-12', 'col-lg-auto', 'me-lg-auto', 'mb-2', 'justify-content-center', 'mb-md-0'], elements=[
                        Li(classes=['nav-item'], elements=[
                            A(classes=['nav-link', 'px-2', 'text-light'], href=value, elements=[key]),
                        ]) for key, value in menu_items.items()
                    ]),
                    Form(method="GET", action="/", classes=['col-12', 'col-lg-auto', 'mb-3', 'mb-lg-0'], props={'role' : "search"}, elements=[
                        Input(_type="search",name="search", classes=['form-control','form-control-dark','text-bg-dark'], props={'placeholder':"Search..."}, id="search"),
                    ]),
                    Div(classes=['text-end'], elements=[
                        Button('Login', classes=['btn', 'btn-outline-light', 'me-2']).on("click", "alert('Login')"),
                        Button('Sign-up', classes=['btn', 'btn-warning']),
                    ])
                ])
            ])
        ]),
        main,
        footer
    ])
    return page.render(body, request)