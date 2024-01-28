import streamlit as st
import img2pdf

st.title('------IMG TO PDF ------')
uploaded_file = st.file_uploader("Upload your file here...", type=['png', 'jpeg', 'jpg'])

if uploaded_file is not None:
    st.image(uploaded_file)
    fn = uploaded_file.name
    pdf_bytes = img2pdf.convert(uploaded_file)
    btn = st.download_button(
                label="Download Pdf",
                data=pdf_bytes,
                file_name=f"{fn}.pdf",
                mime="application/pdf"
            )

st.text('$/$ Made with ❤ By Cyper24 $/$')