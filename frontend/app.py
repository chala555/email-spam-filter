import streamlit as st
import requests
st.title('Spam Email Classifier')
st.write('Please write a message below to check if it looks like spam.')

user_input = st.text_area('Message text')

if st.button('Check'):
    if user_input.strip() == '':
        st.warning('Please enter a message first.')
    else:
        result = requests.post('http://spam-filter-api-container:8000/predict', json={'text': user_input})
        prediction = result.json()["prediction"]  
        if prediction == 'Spam':
            st.error(f'Prediction: {prediction}')
        else:
            st.success(f'Prediction: {prediction}')