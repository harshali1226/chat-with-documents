import streamlit as st
import time
from src.helper import get_pdf_text, get_text_chunks, get_embeddings, get_conversational_chain

def user_input(user_question):
    response = st.session_state.conversational({"question": user_question})
    
    # Update chat history in session_state
    st.session_state.chatHistory = response.get("chat_history", [])
    
    # Display messages from chat history
    for i, message in enumerate(st.session_state.chatHistory):
        if i % 2 == 0:
            st.write("🧑‍💼", message.content)
        else:
            st.write("🤖", message.content)



def main():
    st.set_page_config("Chatbot: Retrieve Information")
    st.header("Chat-with-Documents")

    user_question=st.text_input("Upload files, Hit Submit button, then ask questions.:blue[- Harshali Gaikwad]:sunglasses:")

    if "conversational" not in st.session_state:
        st.session_state.conversational = None
    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory = []
    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Menu")
        pdf_docs=st.file_uploader("Upload your PDF files and CLick on the Submit & Process Button", accept_multiple_files=True)

        if st.button("Submit"):
            with st.spinner("Processing..."):
                time.sleep(2)
                raw_text=get_pdf_text(pdf_docs)
                if raw_text:
                   text_chunks = get_text_chunks(raw_text)
                   vector_store = get_embeddings(text_chunks)
                   st.session_state.conversational = get_conversational_chain(vector_store)
                   st.success("Done")
                else:
                    st.error("No text could be extracted from the uploaded files.")


if __name__ == "__main__":
    main()