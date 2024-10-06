import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")
with col2:
    st.title("Dario Galvagno")
    content = """
    Hi there! I’m Dario, an analyst with a strong background in project management and a passion for music. 
    When I’m not diving into data, you’ll find me playing the bass or practicing boxing and kickboxing. 
    I’m currently expanding my skills by learning Python, and this webpage is where I showcase all my projects.
    Thanks for stopping by, and I hope you enjoy exploring my work!
    """
    st.info(content)
with st.container():
    st.write("Below you can find some of the apps I have built in Python. Feel free to contact me!")

col3, col4 = st.columns(2)

try:
    df = pd.read_csv('data.csv', sep=",", encoding='utf-8')
except Exception as e:
    st.error(f"Error loading data: {e}")
    df = None  # Ensure df is defined

if df is not None:
    with col3:
        for index, row in df[:5].iterrows():
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/" + row["image"])
            st.write(f"[Url link]({row['url']})")

    with col4:
        for index, row in df[6:].iterrows():
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/" + row["image"])
            st.write(f"[Url link]({row['url']})")
else:
    st.warning("No data available to display.")
