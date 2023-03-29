from dash import Dash, html, dcc, Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import dash_gif_component as gif
import flask
from flask import Flask, Response
import numpy as np
from PIL import Image
from io import BytesIO
import base64

import tensorflow as tf
model = tf.keras.models.load_model('./assets/CNN_3Class_Best.h5')
predict_dict = {0: 'Compost', 1: 'Recyclable', 2: 'Trash'}

server = Flask(__name__)
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, './assets/style.css'], server=server, title='Garbage classifier')

app.layout = html.Div(children=[
    dbc.Row([
        dbc.Col(gif.GifPlayer(gif='assets/logo_small.gif', still='assets/logo_small.gif'), width='auto')
    ], justify='center'),
    dbc.Row([
        dbc.Card(
        [            
            dbc.CardBody(
                [
                    html.H4('Garbage classifier', className="card-title"),                    
                    dbc.Row([
                            dbc.Col(html.P('Take a picture of a single object with your phone\'s camera', className='card-text'), width='auto'),
                        ], justify='left'),
                    dbc.Row([     
                        html.Div(id='classified-label', children=[]),
                        dbc.CardImg(id='still-image', src='', top=False),                                 
                    ]),
                    dcc.Upload(
                        id='upload-data',
                        children=html.Div(['Tap here to bring up the camera']),
                        style={
                            'width': '100%',
                            'height': '60px',
                            'lineHeight': '60px',
                            'borderWidth': '1px',
                            'borderStyle': 'dashed',
                            'borderRadius': '5px',
                            'textAlign': 'center',
                            'margin': '10px'
                        },
                        multiple=False
                    )
                ]
            ),
        ],
        style={ 'width': '800px' }), 
    ], justify='center'),
])

@app.callback(
    Output('still-image', 'src'),
    Output('upload-data', 'style'),
    Output('classified-label', 'children'),
    Input('upload-data', 'contents')
    )
def classify_from_cam(img):
    if img != None:
        try:
            style_base={
                    'background-color' : 'white',
                    'font-size' : 'x-large',
                }
            style_with_bold = style_base.copy()
            style_with_bold['font-weight'] = 'bold'                        
            img = Image.open(BytesIO(base64.b64decode(img.split(';')[1].split(',')[1])))
            resize = tf.image.resize(img, (256,256))
            yhat = model.predict(np.expand_dims(resize/255, 0)).reshape(-1)
            winner = predict_dict[np.argmax(yhat)]
            children = [dbc.Row(f'{l} ({round(100*y)}%)', 
                                justify='center', 
                                style=style_base if l != winner else style_with_bold) 
                                for l,y in zip(['Compost', 'Recyclable', 'Trash'], yhat)]
            return (img, { 'visibility' : 'hidden' }, 
                    html.Div(children, 
                             style={
                                'position' : 'absolute',
                                'z-index'  : 10,
                                'top'      : '25%',
                                'left'     : '25%',
                                'background-color' : 'white',
                                'font-size' : 'x-large',
                                'opacity'  : 0.8,
                                'width'    : '50%'
                             }))
        except Exception as e:
            pass
    raise PreventUpdate

if __name__ == '__main__':
    app.run_server()