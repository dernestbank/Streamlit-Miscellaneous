#a simple streamlit page with columns
import streamlit as st
import pandas as pd

st.title('Remove Streamlit Icons')
st.markdown("""
This app removes the icons from the Streamlit logo.
""")

#import css style
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)   
    

col1, col2, col3 = st.columns(3)
with col1:
    st.write(' column 1') 
with col2:
    st.write(' Column 2')
with col3:
    st.write('Column 3')

st.image('https://streamlit.io/images/brand/streamlit_logo.png', width=150)     

