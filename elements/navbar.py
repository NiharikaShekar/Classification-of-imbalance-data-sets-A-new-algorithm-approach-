import dash_bootstrap_components as dbc
from dash import html
from app import app
from dash.dependencies import Input, Output, State

navbar = dbc.Navbar(
        dbc.Container(
                [
                    dbc.Row([
                        dbc.Col([
                            dbc.NavbarBrand("Dashboard", className="ms-2")
                        ],
                        width={"size":"auto"})
                    ],
                    align="center",
                    className="g-0"),

                    dbc.Row([
                        dbc.Col([
                            dbc.Nav([
                                dbc.DropdownMenu(
                                        children=[
                                            dbc.DropdownMenuItem("Show home page", href="/home"),
                                        ],
                                        nav=True,
                                        in_navbar=True,
                                        label="Home",
                                    ),
                                #dbc.NavItem(dbc.NavLink("Home", href="/home")),
                                dbc.NavItem(dbc.NavLink("Reports", href="/reports")),
                                dbc.NavItem(dbc.NavLink("Class Counts", href="/counts")),
                                dbc.NavItem(dbc.NavLink("Contact Us", href="/contacts"))
                            ],
                            navbar=True
                            )
                        ], 
                        width={"size":"auto"})
                    ],
                    align="center"),
                    dbc.Col(dbc.NavbarToggler(id="navbar-toggler", n_clicks=0)),
                    
                    dbc.Row([
                        dbc.Col(
                             dbc.Collapse(
                                dbc.Nav([
                                    #dbc.NavItem(dbc.NavLink(html.I(className="bi bi-instagram"), href="",external_link=True) ),
                                    #dbc.NavItem(dbc.NavLink(html.I(className="bi bi bi-twitter"), style={'width': '1em'}, href="",external_link=True) ),
                                    dbc.NavItem(dbc.NavLink(html.I(className="bi bi-globe"), href="https://bmsce.ac.in/",external_link=True) ),
                                    dbc.Input(type="search", placeholder="Search"),
                                    dbc.Button( "Search", color="primary", className="ms-1", n_clicks=0 ),
                                ]
                                ),
                                id="navbar-collapse",
                                is_open=False,
                                navbar=True
                             )
                        )
                    ],
                    align="center")
                ],
            fluid=True
            ),
    color="primary",
    dark=True
)


@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open