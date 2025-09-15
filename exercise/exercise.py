import streamlit as st

st.set_page_config(layout="wide")

top = st.container(border=1)
with top:
    st.header('Streamlit Widget Showcase')
    """
    Interactive components and display elements 
    """

col1, col2 = st.columns((1,3), border=True)



with col1:
    st.text('Input Widgets')
    st.text_input('Name')
    st.text_input('Age')
    st.selectbox('Favorite Color', ("Yellow", "Blue", "Red"))
    st.multiselect('Hobbies', ('Reading', 'Music', 'Hunting', 'Vibe Coding'))
    st.slider('Rating (1-10)', min_value=1, max_value=10) 
    #st.select_slider('Price range') 


with col2:
    st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

