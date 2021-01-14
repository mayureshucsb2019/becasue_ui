import os
os.path.abspath

import dash_bootstrap_components as dbc


nav_bar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="#")),
        dbc.NavItem(dbc.NavLink("Page1", href="#")),
        dbc.NavItem(dbc.NavLink("Page2", href="#"))
    ],
    brand="Because Demo",
    brand_href="#",
    color="primary",
    dark=True,
)
