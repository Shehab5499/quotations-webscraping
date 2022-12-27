import pandas as pd
import streamlit as st
from random import randint
df = pd.read_csv('quotes.csv')

st.write('# Welcome to Mr. Quotes Program')
with st.form('form1'):
    submit = st.form_submit_button('Give me a quote!')
    if submit:
        random_num =randint(0, len(df)) 
        st.write('## "'+df['Quote'][random_num]+' "')
         
        
        'By '+df['Author'][random_num]

st.write('Did you know that I\'ve collected these quotes from approximately **2500 pages from passiton.com/inspirational-quotes website**')
st.write('In a few minutes actually through **webscraping**.')
st.write('## Oh, you don\'t even know me?!')
st.write('I am Shehab Soliman from Alexandria Egypt. I am a chemical engineering fresh graduate and learning data analyst.')