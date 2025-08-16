"""
Assignment 1 - Voltage Data Analysis
Python script for voltage data analysis with moving averages and peak detection
"""

import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo
from scipy.signal import find_peaks
import os

def load_and_process_data():
    """Load and preprocess the voltage data"""
    df = pd.read_csv("Sample_Data.csv")
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df.set_index('Timestamp', inplace=True)
    df_plot = df.reset_index()
    
    print(f"Data loaded successfully!")
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    
    return df, df_plot

def create_basic_voltage_plot(df_plot):
    """Create basic voltage vs time plot"""
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
        xaxis=dict(
            tickangle=90,
            nticks=60,
            tickformat='%Y-%m-%d %H:%M:%S'
        ),
        width=1000,
        height=500,
        template='plotly_white'
    )
    
    return fig1

def create_moving_average_plot(df_plot):
    """Create voltage plot with 5-sample moving average"""
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
        xaxis=dict(
            tickangle=90,
            nticks=60,
            tickformat='%Y-%m-%d %H:%M:%S'
        ),
        width=1000,
        height=500,
        template='plotly_white'
    )
    
    return fig2

def find_peaks_and_valleys(df):
    """Find local peaks and valleys in the data"""
    peaks, _ = find_peaks(df['Values'])
    lows, _ = find_peaks(-df['Values'])

    peaks_df = df.iloc[peaks][['Values']]
    lows_df = df.iloc[lows][['Values']]

    print("LOCAL PEAKS:")
    print(peaks_df)
    print(f"\nTotal peaks found: {len(peaks_df)}")

    print("\n" + "="*50)
    print("LOCAL VALLEYS:")
    print(lows_df)
    print(f"\nTotal valleys found: {len(lows_df)}")
    
    return peaks_df, lows_df

def find_voltage_below_threshold(df, threshold=20):
    """Find instances where voltage went below threshold"""
    below_threshold = df[df['Values'] < threshold]

    print(f"INSTANCES WHERE VOLTAGE < {threshold}:")
    print("="*50)
    if len(below_threshold) > 0:
        print(below_threshold)
        print(f"\nTotal instances: {len(below_threshold)}")
    else:
        print(f"No instances found where voltage < {threshold}")
    
    return below_threshold

def create_advanced_moving_averages_plot(df_plot):
    """Create plot with 1000 and 5000 value moving averages"""
    df_plot['MA1000'] = df_plot['Values'].rolling(window=1000, min_periods=1).mean()
    df_plot['MA5000'] = df_plot['Values'].rolling(window=5000, min_periods=1).mean()

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_plot['Timestamp'], 
        y=df_plot['Values'], 
        mode='lines', 
        name='Original Values',
        line=dict(color='royalblue', width=1)
    ))

    fig.add_trace(go.Scatter(
        x=df_plot['Timestamp'], 
        y=df_plot['MA1000'], 
        mode='lines', 
        name='1000 Value MA',
        line=dict(color='firebrick', width=2)
    ))

    fig.add_trace(go.Scatter(
        x=df_plot['Timestamp'], 
        y=df_plot['MA5000'], 
        mode='lines', 
        name='5000 Value MA',
        line=dict(color='mediumseagreen', width=2)
    ))

    fig.update_layout(
        title='Values with 1000 and 5000 Value Moving Averages',
        xaxis_title='Timestamp',
        yaxis_title='Values',
        xaxis=dict(
            tickangle=90,
            nticks=60,
            tickformat='%Y-%m-%d %H:%M:%S'
        ),
        legend=dict(
            title='Legend',
            orientation="v",
            yanchor="top",
            y=1,
            xanchor="left",
            x=1.02
        ),
        width=1000,
        height=500,
        template='plotly_white'
    )
    
    return fig

def main():
    """Main function to run the complete analysis"""
    print("="*60)
    print("ASSIGNMENT 1 - VOLTAGE DATA ANALYSIS")
    print("="*60)
    
    # Load and process data
    df, df_plot = load_and_process_data()
    
    # Create all plots
    fig1 = create_basic_voltage_plot(df_plot)
    fig2 = create_moving_average_plot(df_plot)
    fig3 = create_advanced_moving_averages_plot(df_plot)
    
    # Save plots as HTML files
    os.makedirs('plots', exist_ok=True)
    pyo.plot(fig1, filename='plots/basic_voltage_plot.html', auto_open=False)
    pyo.plot(fig2, filename='plots/voltage_with_ma5.html', auto_open=False)
    pyo.plot(fig3, filename='plots/advanced_moving_averages.html', auto_open=False)
    
    # Perform analysis
    peaks_df, lows_df = find_peaks_and_valleys(df)
    below_20 = find_voltage_below_threshold(df, 20)
    
    print("\n" + "="*60)
    print("ANALYSIS COMPLETE - Plots saved to 'plots' directory")
    print("="*60)
    
    return fig1, fig2, fig3, peaks_df, lows_df, below_20

if __name__ == "__main__":
    main()
