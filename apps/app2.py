import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output
from app import app
from components.navbar import nav_bar
from apps import app1

header = html.Div([
    dbc.Row(dbc.Col(html.H1("Machine Learning Project"))),
])

text1 = app1.doc1

query = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("QUERY", className="card-title"),
                html.P(
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do",
                    className="card-value",
                )
            ]
        ),
    ],
)

document1 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(dbc.Button("DOCUMENT 1", color="link", href="#"), className="card-title"),
                html.P(
                    text1,
                    className="card-value",
                )
            ]
        ),
    ],
)

analysis_header = [
    html.Thead(html.Tr([html.Th("Doc Score"), html.Th("Metric")]))
]

row1 = html.Tr([html.Td("1.1"), html.Td("Ranking-Score")])
row2 = html.Tr([html.Td(),html.Td()])
row3 = html.Tr([html.Td("1.1"), html.Td("Query-Score")])
row4 = html.Tr([html.Td("1.1"), html.Td("Doc-Score")])
row5 = html.Tr([html.Td("1.1"), html.Td("Matching")])
row6 = html.Tr([html.Td("1.1"), html.Td("Semantic Matching")])
row7 = html.Tr([html.Td("1.1"), html.Td("Syntactic Matching")])

analysis_body = [html.Tbody([row1, row2, row3, row4, row5, row6, row7])]

analysis = dbc.Table(
    analysis_header + analysis_body,
    bordered=True,
    dark=True,
    hover=True,
    responsive=True,
    striped=True,
)

row = dbc.Row([dbc.Col(document1, width=4), dbc.Col(analysis, width=4)])

layout = html.Div([
    nav_bar,
    header,
    query,
    html.Br(),
    row,
    html.Div(id='app-2-display-value'),
    dcc.Link('Go to App 1', href='/apps/app1')
])

@app.callback(
    Output('app-2-display-value', 'children'),
    Input('app-2-dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)
