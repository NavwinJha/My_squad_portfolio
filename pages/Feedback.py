import streamlit as st
import user_email as ue

st.header("Pls share your review.")

with st.form(key="feedback_formS"):
    user_email = st.text_input("Enter your email address :")
    user_text = st.text_area("Pls Enter your feedback on team :")
    user_text = f"""\
Subject : Mail from {user_email}
From : {user_email}
{user_text}
"""
    button = st.form_submit_button()
    if button:
        ue.email_sent(user_text)
        st.info("Got your email. Thanks for feedback :)")