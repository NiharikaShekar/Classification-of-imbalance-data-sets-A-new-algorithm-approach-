import dash
import plotly.express as px
import pandas as pd
from app import app
from dash import dcc, Output, Input, html
import dash_bootstrap_components as dbc    
import os,flask
import plotly
import plotly.graph_objects as go

#layout of the reports tab:

dir=os.listdir(os.getcwd()+'/preprocessing/datafiles/')
print(dir)
print(len(dir))

if len(dir)==0:
    counts_layout=([
        html.H1("No csv file uploaded")
    ])
else:
    from preprocessing import arka_preprocessing

    df,df_count,df_countover,df_countunder,df_countcombo=arka_preprocessing.get_dataframe()
    counts_layout = ([
            #html.Div([
                #html.Label(['X-axis categories to compare:'],style={'font-weight': 'bold'}),
                #dcc.Dropdown(
                #    id="dropdown",
                #    options=[
                #        {'label':'oversampling','value':'oversampling'},
                #        {'label':'undersampling','value':'undersampling'},
                #    ],
                #    value='oversampling',
                #    multi=False,
                #    clearable=False,
                #    style={'width':'50%'}
                #),
            #]),
            html.Div([
                dcc.Graph(
                    id='bar_chart1',
                    figure=px.bar(
                        data_frame=df_count,
                        x=["0","1"],
                        y=["Class Instances"],
                        barmode='group'
                    )
                )
            ]),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Div([
                dcc.Graph(
                    id='bar_chart2',
                    figure=px.bar(
                        data_frame=df_countover,
                        x=["0","1"],
                        y=["Class Instances"],
                        barmode='group'
                        
                    ),
                )
            ]),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Div([
                dcc.Graph(
                    id='bar_chart3',
                    figure=px.bar(
                        data_frame=df_countunder,
                        x=["0","1"],
                        y=["Class Instances"],
                        barmode='group'
                    )
                )
            ]),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Div([
                dcc.Graph(
                    id='bar_chart4',
                    figure=px.bar(
                        data_frame=df_countcombo,
                        x=["0","1"],
                        y=["Class Instances"],
                        barmode='group'
                    )
                )
            ])
    ])

