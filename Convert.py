import json
import streamlit as st
from streamlit_lottie import st_lottie
col1, col2 = st.columns(2)
with col1:

    st.markdown("""## Gray code Converter by Sudhanshu""")


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)



with col1:
    lottie_now = load_lottiefile("file/code.json")
st_lottie(
    lottie_now,
    speed=1,
    reverse=False,
    loop=True,
    quality="low",
    height=300,
    key=None,

)


st.success("Choose one of them")
op1="Binary to Gray"
op2="Gray to Binary"
selected_option = st.radio( (""),(op1, op2))

if selected_option == op1:
    binary = st.text_input("Enter that binary code")
    gray = binary[0]
    for i in range(1, len(binary)):
        gray = gray + str(int(binary[i - 1]) ^ int(binary[i]))
    st.write("Binary code that you provide")
    st.success(binary)
    st.write("Converted Gray Code")
    st.success(gray)

elif selected_option == op2:
    gray = st.text_input("Enter that Gray code")
    binary = gray[0]
    for i in range(1, len(gray)):
        binary = binary + str(int(binary[i - 1]) ^ int(gray[i]))

    st.write("Gray code that you provide")
    st.success(gray)
    st.write("Converted Binary Code")
    st.success(binary)

else:
    st.write("You Choose something that Wrong")
