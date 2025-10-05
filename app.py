import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello Streamlit")

st.write("Hey this is a simple app.")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.write(chart_data)
st.line_chart(chart_data)

st.bar_chart(chart_data)

name=st.text_input("Enter your name")
if name:
    st.write(f"Hello {name}!")

age = st.slider("Select your age", 0, 100, 25)
st.write(f"You are {age} years old.")

options = ['Python', 'Java', 'C++', 'JavaScript']
choice = st.selectbox("Select your favorite programming language", options)
st.write(f"You selected: {choice}")

