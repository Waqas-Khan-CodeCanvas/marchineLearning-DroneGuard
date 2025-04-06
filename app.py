from flask import Flask, request, jsonify
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from ml_model import DroneAttackDetector
import json
from datetime import datetime

# Initialize Flask and Dash
server = Flask(__name__)
app = Dash(__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Load the trained model
try:
    detector = DroneAttackDetector.load_model('drone_attack_model.joblib')
except:
    detector = DroneAttackDetector()

# Store recent predictions for visualization
recent_predictions = []
MAX_STORED_PREDICTIONS = 100

# Dashboard layout
app.layout = html.Div([
    html.H1("Drone Network Attack Detection Dashboard", className="text-center mb-4"),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Real-time Attack Detection"),
                dbc.CardBody([
                    html.H2(id='current-status', className="text-center"),
                    dcc.Interval(id='interval-component', interval=1000, n_intervals=0)
                ])
            ])
        ], width=12)
    ], className="mb-4"),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Attack History"),
                dbc.CardBody([
                    dcc.Graph(id='attack-history-graph')
                ])
            ])
        ], width=12)
    ])
])

@server.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint for making predictions on new data
    """
    try:
        data = request.json
        df = pd.DataFrame([data])
        prediction = detector.predict(df)[0]
        
        # Store prediction for visualization
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        recent_predictions.append({
            'timestamp': timestamp,
            'prediction': prediction
        })
        
        # Keep only recent predictions
        if len(recent_predictions) > MAX_STORED_PREDICTIONS:
            recent_predictions.pop(0)
        
        return jsonify({
            'status': 'success',
            'prediction': prediction,
            'timestamp': timestamp
        })
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'error': str(e)
        }), 400

@app.callback(
    [Output('current-status', 'children'),
     Output('attack-history-graph', 'figure')],
    [Input('interval-component', 'n_intervals')]
)
def update_dashboard(n):
    """
    Update dashboard components
    """
    # Update current status
    if recent_predictions:
        latest = recent_predictions[-1]
        current_status = f"Latest Detection: {latest['prediction']}"
    else:
        current_status = "No attacks detected"
    
    # Update history graph
    df = pd.DataFrame(recent_predictions)
    if not df.empty:
        fig = px.line(df, x='timestamp', y='prediction', 
                     title='Attack Detection History')
    else:
        fig = px.line(title='No data available')
    
    return current_status, fig

if __name__ == '__main__':
    app.run(debug=True, port=8050) 