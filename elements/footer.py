from dash import html


footer=html.Div(className="footer",children=[
    html.Footer(children=["For feedback feel free to contact",
                               html.Br(),
                               html.Div(html.A(("Arka  "),href="mailto:arkasinha.cs19@bmsce.ac.in",target="_blank",style={'color':'blue'})),
                               html.Div(html.A(("Niharika  "),href="mailto:niharikabs.cs19@bmsce.ac.in",style={'color':'blue'})),
                               ])
])