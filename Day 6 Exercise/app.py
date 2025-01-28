from dotenv import load_dotenv
import streamlit as st
import chain


load_dotenv()

def quiz_generator_app():
    '''
    function to generate quiz with level and field
    '''
    st.title("🎓 Quiz Generator")
    st.markdown("""
    Welcome to the **Quiz Generator App**!  
    Select a difficulty level and enter a field of study to generate a customized quiz.
    """)
    with st.form("quiz_generator"):
        levels=["Hard","Medium","Easy"]
        level = st.selectbox("📊 Select Difficulty Level for Quiz", levels)
        field = st.text_input("📘 Enter the Field of Study (e.g., Science, Maths, History)")
        submitted=st.form_submit_button("Generate quiz")

        if(submitted):
            response=chain.generate_quiz(level,field)
            st.info(response)


quiz_generator_app()