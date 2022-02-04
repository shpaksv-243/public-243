import streamlit as st

def uploader_callback():
    print('Uploaded file')

st.file_uploader(
    label='File uploader',
    on_change=uploader_callback,
    key='file_uploader'
)

st.text_input(label='Textbox 1', key='first')
