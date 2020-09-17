import streamlit as st
import pandas as pd
import numpy as np

DATA_URL = ( "\\F:\\Data\\Motor_Vehicle_Collisions_-_Crashes.csv")

st.title("Motor Vehichle collisions in New York City")
st.markdown("This application is a streamlit dashboard that can be "
"used to analyze motor vehichle collisions in NYC💥🚗")

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows, parse_dates=[['CRASH_DATE','CRASH_TIME']])
    