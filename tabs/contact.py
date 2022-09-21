#from typing_extensions import Required
from pydoc import classname
from dash import html
from app import app
from dash import dcc
import dash_bootstrap_components as dbc
import os
from urllib.parse import quote as urlquote
import base64
from dash.dependencies import Input, Output
from flask import Flask, send_from_directory
import smtplib
import ssl


email_input = dbc.Row([
        dbc.Label("Email"
                , html_for="example-email-row"
                , width=2),
        dbc.Col(dbc.Input(
                type="email"
                , id="example-email-row"
                , placeholder="Enter email"
            ),width=10,
        )],className="mb-3"
)
user_input = dbc.Row([
        dbc.Label("Name", html_for="example-name-row", width=2),
        dbc.Col(
            dbc.Input(
                type="text"
                , id="example-name-row"
                , placeholder="Enter name"
                , maxLength = 80
            ),width=10
        )], className="mb-3"
)
message = dbc.Row([
        dbc.Label("Message"
         , html_for="example-message-row", width=2)
        ,dbc.Col(
            dbc.Textarea(id = "example-message-row"
                , className="mb-3"
                , placeholder="Enter message"
                , required = True)
            , width=10)
        ], className="mb-3")

def contact_form():
    markdown = ''' ### Send a message if you have a comment, question,or concern. Thank you!'''   
    form = html.Div([ dbc.Container([
            dcc.Markdown(markdown)
            , html.Br()
            , dbc.Card(
                dbc.CardBody([
                     dbc.Form([email_input
                        , user_input
                        , message])
                ,html.Div(id = 'div-button', children = [
                    dbc.Button('Submit'
                    , color = 'primary'
                    , id='button-submit'
                    , n_clicks=0)
                ]) #end div
                ])#end cardbody
            )#end card
            , html.Br()
            , html.Br()
        ])
        ])
    
    return form

@app.callback(Output('div-button', 'children'),
    Input("button-submit", 'n_clicks')
    ,Input("example-email-row", 'value')
    ,Input("example-name-row", 'value')
    ,Input("example-message-row", 'value')
    )
def submit_message(n, email, name, message):
    
    port = 465  # For SSL
    sender_email = email
    receiver_email = 'niharikabs.cs19@bmsce.ac.in'
      
    # Create a secure SSL context
    context = ssl.create_default_context()       
    
    if n > 0:
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("niharikabs.cs19@bmsce.ac.in", 'ni@9663081711rika')
            server.sendmail(sender_email, receiver_email, message)
            server.quit()
        return [html.P("Message Sent")]
    else:
        return[dbc.Button('Submit', color = 'primary', id='button-submit', n_clicks=0)]