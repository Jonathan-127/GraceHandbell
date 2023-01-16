"""
A simple app demonstrating how to manually construct a navbar with a customised
layout using the Navbar component and the supporting Nav, NavItem, NavLink,
NavbarBrand, and NavbarToggler components.
Requires dash-bootstrap-components 0.3.0 or later
"""
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, html

import dash
from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

import dash_bootstrap_components as dbc
from dash import Input, Output, State, html
from dash_bootstrap_components._components.Container import Container

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

# stylesheet with the .dbc class
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
# app = Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO, dbc.icons.BOOTSTRAP, dbc_css])

app = dash.Dash(
    prevent_initial_callbacks=True,
    external_stylesheets=[dbc.themes.SUPERHERO, dbc.icons.BOOTSTRAP, dbc_css],
    meta_tags=[{'name': 'viewport',
                'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}]
    )

server = app.server
#####  Navbar  #####
# make a reuseable navitem for the different examples
# nav_item = dbc.NavItem(dbc.NavLink("Link", href="/"))

div_about = html.Div(
            [
                html.I(className="bi bi-info-circle-fill me-2"),
                "사역원 소개 ",
            ],
            className="d-flex align-items-center",
    )

div_profile = html.Div(
            [
                html.I(className="bi bi-person-circle me-2"),
                "대표 소개 ",
            ],
            className="d-flex align-items-center",
        )

div_handbell = html.Div(
            [
                html.I(className="bi bi-bell-fill me-2"),
                "교회와 핸드벨 ",
            ],
            className="d-flex align-items-center",
        )

div_playlist = html.Div(
            [
                html.I(className="bi bi-youtube me-2"),
                "벨찬송 ",
            ],
            className="d-flex align-items-center",
        )


# make a reuseable dropdown for the different examples
dropdown = html.Div(
    [
        dbc.DropdownMenu(
            [
                dbc.DropdownMenuItem(div_about, href="/about", id="dd-about", n_clicks=0),
                dbc.DropdownMenuItem(div_profile, href="/profile", id="dd-profile", n_clicks=0),
                dbc.DropdownMenuItem(div_handbell, href="/handbell", id="dd-handbell", n_clicks=0),
                dbc.DropdownMenuItem(div_playlist, href="/playlist", id="dd-playlist", n_clicks=0),
            ],
            nav=True,
            in_navbar=True,
            label="Menu",
            id='dd-item'
        ),
        html.P(id="menu-dropdown", className="mt-3"),
    ]
)


# this example that adds a logo to the navbar brand
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.Div(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src='./assets/logo.png', height="30px")),
                        dbc.Col(dbc.NavbarBrand("교회 핸드벨 사역원", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                dbc.Nav(
                    [dropdown],
                    className="ms-auto",
                    navbar=True,
                ),
                id="navbar-collapse",
                navbar=True,
            ),
        ],
    ),
    color="dark",
    dark=True,
    className="mb-5",
    sticky='top'
)
#####  Navbar  #####


#####  ABOUT  #####
about_card_content = [
    dbc.CardHeader("사역원 소개"),
    dbc.CardBody(
        [
            html.H5("About me", className="card-title"),
            html.P(
                "This is some card content that we'll reuse",
                className="card-text",
            ),
        ]
    ),
]

abt_card = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardImg(src='./assets/3.jpg', bottom=True),
                            ],
                        )
                    ] 
                )
            ]
        ),
    ]
)

about_content = dbc.Container(
    [
        # html.Div([html.Img(src=app.get_asset_url("logo.png"), height="30px"), "교회 핸드벨 사역원"]),
        # html.Br(),
        # html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1("교회 핸드벨 사역원", style={'display': 'block', 'text-align': "center", 'font-weight': 'bold'}),
                        html.H3("Handbell Ringers of Korean Churches", style={'display': 'block', 'text-align': "center"}),
                        html.Br(),
                        # html.Img(src=app.get_asset_url('3.jpg'), style={'display': 'block'}),
                        abt_card,
                        html.Br(),
                        dbc.Card(about_card_content, color="primary", inverse=True, style={'display': 'block'}),
                   ],
                    # width=4,
                    xs=12, sm=12, md=10, lg=8, xl=6
                ),
            ], justify="center",
        )
    ],
    # fluid=True,
    className="dbc",
    id='content_about',
    style={'display': 'block'}
    
)
#####  ABOUT  #####


#####  PROFILE  #####
profile_card_content = [
    dbc.CardHeader("이혜경 목사"),
    dbc.CardBody(
        [
            html.H5("About me", className="card-title"),
            html.P(
                "This is some card content that we'll reuse",
                className="card-text",
            ),
        ]
    ),
]

prf_card = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                # dbc.CardBody(html.P("This has a bottom image", className="card-text")),
                                dbc.CardImg(src='./assets/5.jpg', bottom=True),
                            ],
                        )
                    ] 
                )
            ]
        ),
    ]
)

prf_card2 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                # dbc.CardBody(html.P("This has a bottom image", className="card-text")),
                                dbc.CardImg(src='./assets/8.jpg', bottom=True),
                            ],
                        )
                    ] 
                )
            ]
        ),
    ]
)


profile_card = dbc.Card(
    [
        dbc.CardHeader(
            dbc.Tabs(
                [
                    # dbc.Tab(label=["Tab 1", html.I(className="bi bi-mortarboard-fill"),], tab_id="tab-1"),
                    dbc.Tab(label=" 핸드벨 사역 ", labelClassName='bi bi-bell-fill me-2', tab_id="tab-1"),
                    dbc.Tab(label=" 선교 사역 ", labelClassName='bi bi-book me-2', tab_id="tab-2"),
                    dbc.Tab(label=" 학력 ", labelClassName='bi bi-mortarboard-fill me-2', tab_id="tab-3"),
                ],
                id="card-tabs",
                active_tab="tab-1",
            )
        ),
        dbc.CardBody(html.P(id="card-content", className="card-text")),
    ],
    style={'display': 'block'},
)

profile_content = dbc.Container(
    [
        # html.Br(),
        # html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1("대표 소개", style={'display': 'block', 'text-align': "center", 'font-weight': 'bold'}),
                        html.H3("이혜경 목사", style={'display': 'block', 'text-align': "center"}),
                        html.Br(),
                    ],  xs=12, sm=12, md=10, lg=8, xl=6
                )
            ], justify="center",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        prf_card,
                        html.Br(),
                    ], xs=12, sm=12, md=10, lg=8, xl=6
                )
            ], justify="center",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        prf_card2,
                        html.Br(),
                    ], xs=12, sm=12, md=10, lg=8, xl=6
                )
            ], justify="center",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(profile_card_content, color="primary", inverse=True, style={'display': 'block'}),
                        html.Br(),
                    ], xs=12, sm=12, md=10, lg=8, xl=6
                )
            ], justify="center",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        profile_card,
                        html.Br(),
                    ],  xs=12, sm=12, md=10, lg=8, xl=6
                )
            ], justify="center",
        ),
 
    ],
    # fluid=True,
    className="dbc",
    id='content_profile',
    style={'display': 'none'}
)
#####  PROFILE  #####


#####  HANDBELL  #####
handbell_card_content = [
    dbc.CardHeader("교회와 핸드벨"),
    dbc.CardBody(
        [
            html.H5("About me", className="card-title"),
            html.P(
                "This is some card content that we'll reuse",
                className="card-text",
            ),
        ]
    ),
]

hdb_card = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardImg(src='./assets/7.jpg', bottom=True),
                            ],
                        )
                    ] 
                )
            ]
        ),
    ]
)

handbell_content = dbc.Container(
    [
        # html.Div([html.Img(src=app.get_asset_url("logo.png"), height="30px"), "교회 핸드벨 사역원"]),
        # html.Br(),
        # html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1("교회 핸드벨 사역원", style={'display': 'block', 'text-align': "center", 'font-weight': 'bold'}),
                        html.H3("Professional Handbel", style={'display': 'block', 'text-align': "center"}),
                        html.Br(),
                        # html.Img(src=app.get_asset_url('3.jpg'), style={'display': 'block'}),
                        hdb_card,
                        html.Br(),
                        dbc.Card(handbell_card_content, color="primary", inverse=True, style={'display': 'block'}),
                   ],
                    # width=4,
                    xs=12, sm=12, md=10, lg=8, xl=6
                ),
            ], justify="center",
        )
    ],
    # fluid=True,
    className="dbc",
    id='content_handbell',
    style={'display': 'none'}
)
#####  HANDBELL  #####



#####  YOUTUBE  #####
ytb_card_content = [
    dbc.CardHeader("벨찬송"),
    dbc.CardBody(
        [
            html.H5("About me", className="card-title"),
            html.P(
                "This is some card content that we'll reuse",
                className="card-text",
            ),
        ]
    ),
]

ytb_card = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardBody(
                                    [
                                        html.Div(
                                            html.Iframe(
                                                src="https://www.youtube.com/embed/videoseries?list=PLC3qu0wtdsxW6lvWov_9oxkWDZVeby2Td", 
                                                style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'},
                                                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share",
                                            ), id='youtube_list'
                                        )
                                    ]
                                )
                            ],
                        )
                    ] 
                )
            ]
        ),
    ]
)

youtube_content = dbc.Container(
    [
        # html.Div([html.Img(src=app.get_asset_url("logo.png"), height="30px"), "교회 핸드벨 사역원"]),
        # html.Br(),
        # html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1("벨찬송", style={'display': 'block', 'text-align': "center", 'font-weight': 'bold'}),
                        html.H3("Hymn with Handbell", style={'display': 'block', 'text-align': "center"}),
                        html.Br(),
                        # html.Img(src=app.get_asset_url('3.jpg'), style={'display': 'block'}),
                        ytb_card,
                        html.Br(),
                        dbc.Card(ytb_card_content, color="primary", inverse=True, style={'display': 'block'}),
                   ],
                    # width=4,
                    xs=12, sm=12, md=10, lg=8, xl=6
                ),
            ], justify="center",
        )
    ],
    # fluid=True,
    className="dbc",
    id='content_youtube',
    style={'display': 'none'}
)
#####  YOUTUBE  #####





#####  ALERT  #####
alert_content = dbc.Container(
    [
        # html.Div([html.Img(src=app.get_asset_url("logo.png"), height="30px"), "교회 핸드벨 사역원"]),
        # html.Br(),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Alert(
                            [
                                html.H1("404: Not found", className="text-danger"),
                                html.Hr(),
                                html.P(f"The pathname was not recognised..."),
                            ]
                        )
                   ],
                    xs=12, sm=12, md=10, lg=8, xl=6
                ),
            ], justify="center",
        )
    ],
    # fluid=True,
    className="dbc",
    id='content_alert',
    style={'display': 'none'}
)
#####  ALERT  #####



# app.layout = html.Div(
#     [
#         dcc.Location(id="url"),
#         navbar,
#         about_content,
#         profile_content,
#         handbell_content,
#         youtube_content
#     ]
# )



app.layout = dbc.Container(
    [
        dcc.Location(id="url"),
        navbar,
        about_content,
        profile_content,
        handbell_content,
        youtube_content,
        alert_content,
    ], 
    fluid=True,
    className="dbc",
    style={'min-width': '700 px'}
)



# # the same function (toggle_navbar_collapse) is used in all three callbacks
@app.callback(
    Output(f"navbar-collapse", "is_open"),
    [Input(f"navbar-toggler", "n_clicks")],
    [State(f"navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output(component_id='content_about', component_property='style'),
    Output(component_id='content_profile', component_property='style'),
    Output(component_id='content_handbell', component_property='style'),
    Output(component_id='content_youtube', component_property='style'),
    Output(component_id='content_alert', component_property='style'),
    [Input(component_id="url", component_property="pathname")]
)
def show_hide_content(pathname):
    if pathname == "/about":
        return  {'display': 'block'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}
    elif pathname == "/profile":
        return  {'display': 'none'}, {'display': 'block'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}
    elif pathname == "/handbell":
        return  {'display': 'none'}, {'display': 'none'}, {'display': 'block'}, {'display': 'none'}, {'display': 'none'}
    elif pathname == "/playlist":
        return  {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'block'}, {'display': 'none'}
    elif pathname == "/":
        return  {'display': 'block'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}
    else:
        return  {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'block'}




@app.callback(
    Output(component_id="card-content", component_property="children"), 
    [Input(component_id="card-tabs", component_property="active_tab")]
)
def tab_content(active_tab):
    if active_tab == "tab-1":
      cont = html.Div([
          html.H6("tab 1", style={'display': 'block', 'text-align': "left"}),
          html.H6("tab 1", style={'display': 'block', 'text-align': "left"}) 
        ])   
    elif active_tab == "tab-2":
      cont = html.Div([
          html.H6("tab 2", style={'display': 'block', 'text-align': "left"}),
          html.H6("tab 2", style={'display': 'block', 'text-align': "left"}) 
        ]) 
    elif active_tab == "tab-3":
      cont = html.Div([
          html.H6("tab 3", style={'display': 'block', 'text-align': "left"}),
          html.H6("tab 3", style={'display': 'block', 'text-align': "left"}) 
        ])    
    
    return cont



















if __name__ == "__main__":
    app.run_server(port=8088)
    # app.run_server(port=8888)
