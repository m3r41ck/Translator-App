import streamlit as st
from transformers import pipeline
from languages import LANG_OPTIONS


@st.cache_resource(show_spinner=False)
def cache_model(input_lang, target_lang):
    model_name = f"Helsinki-NLP/opus-mt-{input_lang}-{target_lang}"
    pipe = pipeline("translation", model=model_name)
    reset_chat()
    return pipe

def translate_message(model, message):
    translated_message=model(message)
    return translated_message[0].get('translation_text')

def reset_chat():
    st.session_state.messages = []

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages=[]

def main():
    initialize_session_state()

    st.title('Translator')
    st.button("Reset", on_click=reset_chat)

    col1, col2 = st.columns(2)
    with col1:
        input_lang = st.selectbox(label="Input Language", placeholder="Choose a language", options=LANG_OPTIONS.keys(), key="input_lang", index=None)
    with col2:
        trans_lang = st.selectbox(label="Translation Language", placeholder="Choose a language", options=LANG_OPTIONS.keys(), key="trans_lang", index=None)

    try:
        if input_lang != None and trans_lang != None:
            if input_lang == trans_lang and input_lang != None:
                st.error('Language selection cannot be the same. Please pick a different language.', icon="🚨")
            else:
                with st.spinner("Loading language model..."):
                    trans_model = cache_model(LANG_OPTIONS[input_lang], LANG_OPTIONS[trans_lang])
    except EnvironmentError:
        st.error('Unfortunately current translation model doesnt support your selected languages. Please select a different languages!', icon="🚨")


    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])    

    if prompt := st.chat_input('Enter text: '):
        with st.chat_message("user"):
                st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        response = translate_message(trans_model, prompt)
        with st.chat_message("assitant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    main()