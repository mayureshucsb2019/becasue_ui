import base64
import datetime
import io

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import app
from components import navbar
from apps import app1, app2

# Header for the page
header = html.Div([
    dbc.Row(dbc.Col(html.H1("Because Project"))),
])

# This componenet is to get the user input
input_text = dcc.Input(
            id="input_text",
            className='input-text',
            type="text",
            placeholder="<e1> Eating </e1> too much causes <e2> stomach upset </e2>.")

# This component is to get the multiple files uploaded 
data_upload = dcc.Upload(
        id='upload-data',
        className='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        multiple=True )

# This is hte Div for file upload and the corresponding message
data_upload_div = html.Div([
        data_upload,
        html.Div(id='output-data-upload'),# This line displays the message if the file is uploaded,
        html.P(),
        html.Button("Predict From File!", id='predict-button')
    ])

# This is the Div for text input and the corresponding message
input_text_div = html.Div([
        input_text, 
        html.Div(id="input-text"), # This line displays the message if predict action is successful to wait
        html.P(),
        html.Button("Predict From Text!", id='predict-button')
    ])

plot_graph_div = html.Div(
     html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eu ultrices vitae auctor eu augue ut lectus. Pulvinar mattis nunc sed blandit. Dis parturient montes nascetur ridiculus mus mauris vitae ultricies. Amet massa vitae tortor condimentum. Eu consequat ac felis donec et odio pellentesque. Varius morbi enim nunc faucibus a pellentesque sit amet. Eget nulla facilisi etiam dignissim diam quis enim lobortis scelerisque. Nulla pharetra diam sit amet nisl suscipit. Facilisis magna etiam tempor orci eu. Lectus mauris ultrices eros in cursus. Faucibus interdum posuere lorem ipsum dolor. Ac felis donec et odio pellentesque diam volutpat commodo. Augue interdum velit euismod in pellentesque massa placerat. Augue ut lectus arcu bibendum at varius vel pharetra vel. Ultrices in iaculis nunc sed augue lacus viverra vitae congue. Egestas egestas fringilla phasellus faucibus scelerisque. Facilisi nullam vehicula ipsum a arcu cursus vitae congue mauris. Bibendum neque egestas congue quisque egestas diam. Scelerisque in dictum non consectetur a erat nam at. Enim lobortis scelerisque fermentum dui faucibus in. Id porta nibh venenatis cras sed felis eget velit aliquet. Erat nam at lectus urna duis convallis convallis tellus. Ultricies mi quis hendrerit dolor magna eget est. Ullamcorper sit amet risus nullam eget. At tellus at urna condimentum mattis pellentesque id. Feugiat scelerisque varius morbi enim nunc. Turpis massa sed elementum tempus egestas. Tristique magna sit amet purus. Viverra ipsum nunc aliquet bibendum enim facilisis gravida neque convallis. In aliquam sem fringilla ut morbi tincidunt augue interdum velit. Auctor neque vitae tempus quam. Nam at lectus urna duis convallis convallis tellus id."),
     id="graph-output",
     className="graph-data"
)

# This will be the layout of the page that will be displayed by index.py
index_layout = html.Div([
    navbar.nav_bar,
    header,
    plot_graph_div,
    html.P(),
    dbc.Row([dbc.Col(data_upload_div, width=6),dbc.Col(input_text_div, width=6)]),
    html.P(),
])

# This function decodes the input of the file and writes it to the data directory
# It also displays the success message whose CSS is put inside the assets/style.css
def get_file_contents(contents, filename, date):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    with open("./data/"+filename,"w") as file:
        file.write(str(decoded.decode('ascii')))
    file.close()
    return html.Div([
        html.H6(f"Uploaded {filename} into data directory Sucessfully!",className="success-message"),
    ])

# This is the app layout which is dynamically returned as per page 
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


click_count = 0
# Callback if user provides for the inputs in the text
@app.callback(Output("input-text", "children"),
              Input("input_text", "value"),
              Input("predict-button", 'n_clicks'))
def cb_render(value, n_clicks):
    global click_count
    if n_clicks is None:
        pass
    elif(int(n_clicks) > click_count):
        click_count += 1
        with open("./data/user_input.txt","w") as file:
            file.write(value)
        file.close()
        # Call the predict function here and get the prediction output
        return "Starting prediction please wait!"

# Callback if the files are uploaded
@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'),
              State('upload-data', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            get_file_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children


# Callback if the new pages are to be switched to 
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return index_layout
    elif pathname == '/apps/app1':
        return app1.layout
    elif pathname == '/apps/app2':
        return app2.layout
    else:
        return 'Page not found: 404'

if __name__ == '__main__':
    app.run_server(port=3000, debug=True)
