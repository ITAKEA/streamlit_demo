import streamlit as st

# skrive tekst på siden
st.title('Hello class')


""" 
# Hello world
sfkjhfksjhfksdfj

## sdkfjhdskjfhsdkjfhkdjsf
'sdjfhsdkjfhdskj
lskdfjsldkfjsdkljfs


sdlkfdjsklfjsdlkfjds
sdkjfhsdkjfhsj


"""

# input

x = st.text_input('Hvad er din alder?')

y = f"din alder er {x}"
y


antal = st.slider('Antal biler')

f'Antallet af biler i vores forretning er: {antal}'

'--------------------------------'

col1, col2 = st.columns(2)

col1.button('Click me')

col2.text_input('Hello')

st.sidebar.button('sidebar label')