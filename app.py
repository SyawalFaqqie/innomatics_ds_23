import streamlit as st


st.title("My :green[Data App] :rice_cracker:")
st.header("Data Science Internship")

st.snow()

btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("You clicked me :sunglasses:")
    st.balloons()
