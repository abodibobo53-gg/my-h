import streamlit as st
import time

st.set_page_config(page_title="Fan Portal", layout="centered")

if 'stage' not in st.session_state:
    st.session_state.stage = 'ronaldo'

if st.session_state.stage == 'ronaldo':
    st.title("أفضل لاعب في التاريخ ⚽")
    st.image("https://upload.wikimedia.org/wikipedia/commons/8/8c/Cristiano_Ronaldo_2018.jpg")
    
    time.sleep(25)
    st.session_state.stage = 'prank'
    st.rerun()

elif st.session_state.stage == 'prank':
    st.markdown("""
        <style>
        .stApp {background-color: black; color: #00FF00; font-family: 'Courier New';}
        </style>
    """, unsafe_allow_html=True)
    
    st.title("⚠️ SYSTEM BREACHED ⚠️")
    st.write("جارٍ الوصول إلى قاعدة البيانات...")
    time.sleep(1.5)
    
    st.error("تم نسخ جميع الملفات بنجاح!")
    time.sleep(1)
    
    st.subheader("تمت العملية بواسطة: 🤖 كودات عبودي")
    st.write("---")
    st.success("لا تخافي.. تمزح معك! هذا مقلب برمجته بنفسي 😎")
    
    if st.button("اضغطي هنا للمزيد"):
        st.balloons()
        st.write("شكراً لثقتك في نظام عبودي الأمني!")
