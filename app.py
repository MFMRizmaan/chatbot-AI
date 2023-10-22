import streamlit as st
from Chatter import ChatBot

def main():
    st.title("ChatBot with Streamlit")

    # Create an instance of your ChatBot
    ai = ChatBot(name="Dave")

    # Input box for user to type messages
    user_input = st.text_input("You:", "")

    if st.button("Send"):
        ai.text_input(user_input)
        response = ai.respond()

        # Display the response from the ChatBot
        st.write("Dev:", response)

if __name__ == '__main__':
    main()
