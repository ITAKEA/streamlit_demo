# Streamlit demo
Demonstration af streamlit frontend framework

Dokumentation:    
https://docs.streamlit.io/    

Gennemgang af:

* Install og import af streamlit
* requirements.txt 

## Text elementer: 

""" Hello world  """   
st.write()    
f"Hello {name}"

## Slider: 
x = st.slider('Antal biler')

## input
y = st.text_input('Hvad er din alder?')

## Selectbox
s = st.selectbox('Hvad er din alder?', [12, 13, 33, 66])

f'Hello {s}' if s >= 18 else 'nono'

## Columns
col1, col2 = st.columns(2)
col1.button('Click me')
col2.write('# Hello there')

## pages 
put the in a **pages** folder


<!--  #st.sidebar.selectbox('Hvordan vil kun kontake os', ['email', 'phone']) -->