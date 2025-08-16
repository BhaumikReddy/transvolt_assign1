"""
Flask Web Application for Voltage Data Analysis
Assignment 1 - Web Dashboard
Optimized for PythonAnywhere deployment
"""

from flask import Flask, render_template, jsonify
import pandas as pd
import plotly.graph_objs as go
import plotly.utils
from scipy.signal import find_peaks
import json
import os

app = Flask(__name__)

def load_data():
    """Load and preprocess the voltage data"""
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, "Sample_Data.csv")
    
    df = pd.read_csv(csv_path)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df.set_index('Timestamp', inplace=True)
    df_plot = df.reset_index()
    return df, df_plot

def create_all_plots():
    """Create all plots for the dashboard"""
    df, df_plot = load_data()
    
    # Basic voltage plot
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(
        x=df_plot['Timestamp'],
        y=df_plot['Values'],
        mode='lines',
        name='Voltage',
        line=dict(color='blue', width=1)
    ))
    fig1.update_layout(
        title="Voltage vs Time",
        xaxis_title="Time",
        yaxis_title="Voltage",
        xaxis=dict(tickangle=90, nticks=60, tickformat='%Y-%m-%d %H:%M:%S'),
        template='plotly_white'
    )
    
    # Moving average plot
    df_plot['MA5'] = df_plot['Values'].rolling(window=5).mean()
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(
        x=df_plot['Timestamp'],
        y=df_plot['Values'],
        mode='lines',
        name='Voltage',
        line=dict(color='blue', width=1)
    ))
    fig2.add_trace(go.Scatter(
        x=df_plot['Timestamp'],
        y=df_plot['MA5'],
        mode='lines',
        name='5-sample MA',
        line=dict(color='red', width=2)
    ))
    fig2.update_layout(
        title="Voltage vs Time with 5-sample Moving Average",
        xaxis_title="Time",
        yaxis_title="Voltage",
        xaxis=dict(tickangle=90, nticks=60, tickformat='%Y-%m-%d %H:%M:%S'),
        template='plotly_white'
    )
    
    # Advanced moving averages
    df_plot['MA1000'] = df_plot['Values'].rolling(window=1000, min_periods=1).mean()
    df_plot['MA5000'] = df_plot['Values'].rolling(window=5000, min_periods=1).mean()
    
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(
        x=df_plot['Timestamp'], y=df_plot['Values'], mode='lines', 
        name='Original Values', line=dict(color='royalblue', width=1)
    ))
    fig3.add_trace(go.Scatter(
        x=df_plot['Timestamp'], y=df_plot['MA1000'], mode='lines', 
        name='1000 Value MA', line=dict(color='firebrick', width=2)
    ))
    fig3.add_trace(go.Scatter(
        x=df_plot['Timestamp'], y=df_plot['MA5000'], mode='lines', 
        name='5000 Value MA', line=dict(color='mediumseagreen', width=2)
    ))
    fig3.update_layout(
        title='Values with 1000 and 5000 Value Moving Averages',
        xaxis_title='Timestamp',
        yaxis_title='Values',
        xaxis=dict(tickangle=90, nticks=60, tickformat='%Y-%m-%d %H:%M:%S'),
        template='plotly_white'
    )
    
    # Analysis results
    peaks, _ = find_peaks(df['Values'])
    lows, _ = find_peaks(-df['Values'])
    peaks_df = df.iloc[peaks][['Values']]
    lows_df = df.iloc[lows][['Values']]
    below_20 = df[df['Values'] < 20]
    
    return {
        'plot1': json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder),
        'plot2': json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder),
        'plot3': json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder),
        'peaks_count': len(peaks_df),
        'valleys_count': len(lows_df),
        'below_20_count': len(below_20),
        'data_shape': df.shape,
        'min_voltage': df['Values'].min(),
        'max_voltage': df['Values'].max(),
        'avg_voltage': df['Values'].mean()
    }

@app.route('/')
def index():
    """Main dashboard page"""
    plots_data = create_all_plots()
    return render_template('index.html', **plots_data)

@app.route('/api/data')
def api_data():
    """API endpoint for data analysis results"""
    plots_data = create_all_plots()
    return jsonify(plots_data)

if __name__ == '__main__':
    # For local development
    app.run(debug=True, host='0.0.0.0', port=5000)
else:
    # For production deployment (PythonAnywhere)
    app.debug = False
