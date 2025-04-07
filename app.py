# Importing necessary packages
import streamlit as st
import pandas as pd
from utils import api_extracter

# Cerate an instance/object of the class
client = api_extracter()

# Cerate website title
st.title("IMDB top Movies Project")
