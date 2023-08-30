import streamlit as st
import pandas

col1, col2 = st.columns(2)

with col1:
    st.image("Prudential-Logo-horizontal.png")

with col2:
    st.title("OldPulse Squad5 Team")
    st.info("""
    Hi ! This squad is awsome""")

st.write("Lets meet the members of the squad.")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("squad5.csv", sep=",")
with col3:
    for index, row in df[ :4].iterrows():
        st.header(row["name"])
        st.subheader(row["position"])
        st.image("jpg2png/" + row["images"])
        st.write(f"[Know more]({row['linkdinurl']})")

with col4:
    for index, row in df[4:].iterrows():
        st.header(row["name"])
        st.subheader(row["position"])
        #st.write(row["position"])
        st.image("jpg2png/" + row["images"])
        st.write(f"[Know more]({row['linkdinurl']})")

