import streamlit as st
import pandas as pd
from PIL import Image
st.title('streamlit 超入門')

st.write ('interative Widgets')

option = st.selectbox(
    'あなたが好きな数字を教えてくだい。',
    list(range(1, 11))
)
'あなたの好きな数字は、', option, 'です。'
condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション:', condition

if st.checkbox('Show Image'):
    img = Image.open('sample.jpeg' )
    st.image(img, caption='チビマル', use_column_width=True)




