import streamlit as st
from translit_utils import transliterate

st.title("Punjabi Transliteration")
text = st.text_area("Enter Punjabi text:")
direction = st.radio("Direction", ["Gurmukhi → Shahmukhi", "Shahmukhi → Gurmukhi"])
dir_code = "g2s" if direction.startswith("Gurmukhi") else "s2g"

if st.button("Transliterate"):
    result = transliterate(text, dir_code)
    st.markdown("### Output")
    st.write(result)
