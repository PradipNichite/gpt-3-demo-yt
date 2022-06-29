import streamlit as st
import openai
st.title('GPT-3 Demo')
user_input = st.text_area('Text to analyze',"Sundar Pichai is the CEO of Google.")

if st.button('Extract Entities') and user_input:
    st.write(user_input)
    openai.api_key = "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"

    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=f"Extract Entities from the text.\ntext: Delhi is the capital of India.\nEntities:\nDelhi: City\nIndia: Country\n##\ntext: {user_input}\nEntities:",
    temperature=0,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    st.write(response['choices'][0]['text'])
