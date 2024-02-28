import streamlit as st
import predictor

st.title('URL Predictor -- Malicious/Benign')

# Define a function to perform URL prediction
def predict_url(url):
    prediction = predictor.prediction(url)
    return prediction

# UI elements
url_input = st.text_input('Enter URL')

if st.button('Predict'):
    if url_input:
        prediction = predict_url(url_input)
        st.write(f'Prediction: {prediction}')
    else:
        st.write('Please enter a URL')

# Function to clear the output
def clear_output():
    st.session_state.output = ""

# Display a clear button
if st.button('Clear'):
    clear_output()
