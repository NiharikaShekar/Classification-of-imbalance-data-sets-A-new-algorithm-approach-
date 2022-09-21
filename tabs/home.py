#from typing_extensions import Required
from pydoc import classname
from sre_parse import State
from dash import html
from app import app
from dash import dcc
import dash_bootstrap_components as dbc
import os
from urllib.parse import quote as urlquote
import base64
from dash.dependencies import Input, Output
from flask import Flask, send_from_directory

UPLOAD_DIRECTORY = os.getcwd()+"/preprocessing/datafiles/"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)



home_layout = html.Div(children=[
    html.H1("Classification of imbalanced dataset",style={'text-align':'center'}),
    html.P(id="no",children="An imbalanced classification problem is an example of a classification problem where the distribution of examples across the known classes is biased or skewed. The distribution can vary from a slight bias to a severe imbalance where there is one example in the minority class for hundreds, thousands, or millions of examples in the majority class or classes.Imbalanced classifications pose a challenge for predictive modeling as most of the machine learning algorithms used for classification were designed around the assumption of an equal number of examples for each class. This results in models that have poor predictive performance, specifically for the minority class. This is a problem because typically, the minority class is more important and therefore the problem is more sensitive to classification errors for the minority class than the majority class."),
    html.H2("Upload"),
        dcc.Upload(
            id="upload-data",
            children=html.Div(
                ["Drag and drop or click to select a file to upload."]
            ),
            style={
                "width": "100%",
                "height": "60px",
                "lineHeight": "60px",
                "borderWidth": "1px",
                "borderStyle": "dashed",
                "borderRadius": "5px",
                "textAlign": "center",
                "margin": "10px",
            },
            multiple=True,
        ),
        html.H2("File List"),
        html.Ul(id="file-list"),
    dbc.Button(
        "Delete files",
        id="delete",
        className="me-2",
        n_clicks=0,
    ),
    html.Img(src="https://datascience.aero/wp-content/themes/yootheme/cache/imbalancedata-6e7d6903.png",style={'height':'400px','width':'500px','margin-left':'300px'})
])



def save_file(name, content):
    """Decode and store a file uploaded with Plotly Dash."""
    data = content.encode("utf8").split(b";base64,")[1]
    with open(os.path.join(UPLOAD_DIRECTORY, name), "wb") as fp:
        fp.write(base64.decodebytes(data))


def uploaded_files():
    """List the files in the upload directory."""
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
            print(files)
    return files


def file_download_link(filename):
    """Create a Plotly Dash 'A' element that downloads a file from the app."""
    location = "/download/{}".format(urlquote(filename))
    return html.A(filename, href=location)


@app.callback(
    Output("file-list", "children"),
    [Input("upload-data", "filename"), Input("upload-data", "contents"),Input("delete","n_clicks")],
)
def update_output(uploaded_filenames, uploaded_file_contents,n):
    """Save uploaded files and regenerate the file list."""

    if n>0:
        if os.path.exists(os.getcwd()+"/preprocessing/datafiles/data.csv"):
            os.remove(os.getcwd()+"/preprocessing/datafiles/data.csv")
        else:
            pass

    if uploaded_filenames is not None and uploaded_file_contents is not None:
        for name, data in zip(uploaded_filenames, uploaded_file_contents):
            save_file(name, data)

    files = uploaded_files()
    if len(files) == 0:
        return [html.Li("No files yet!")]
    else:
        return [html.Li(file_download_link(filename)) for filename in files]


''''
@app.callback(
    Output("file-list","children"),
    [Input("delete","n_clicks")]
)

def delete_file(n):
    if n>0:
        os.remove(os.getcwd()+"/preprocessing/datafiles/data.csv")
        '''