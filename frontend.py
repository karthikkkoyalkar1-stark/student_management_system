import streamlit as st

# title
st.title("Student Management System")

# heading - if we have multiple sections,
st.header("Add student details")

# sub section
st.subheader("Students details")

# write any strings, dict, list
st.write("Welcome to the application")
st.write({"id" : 1,"name":"lahari","dept":"c"})

# how to take input and how to display it
name = st.text_input("Enter your name")
st.write(name)

age = st.number_input("Enter your age",step=1)
st.write(age)

dept = st.selectbox(
    "Select dept",
    ["python","c","java"]
)

if st.button("Add student"):
    st.success("student added")

st.error("Id not found")
st.warning("deleted the student id")

# sidebar
menu = st.sidebar.selectbox(
    "Sections",
    ["Add", "Update", "Delete" , "View"]
)
