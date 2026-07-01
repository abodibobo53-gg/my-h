import streamlit as st
import time

st.set_page_config(page_title="Fan Portal", layout="centered")

if 'stage' not in st.session_state:
    st.session_state.stage = 'breach'

if st.session_state.stage == 'breach':
    st.markdown("""
    <style>
    .stApp {background-color: black; color: #00FF00; font-family: 'Courier New';}
    </style>
    """, unsafe_allow_html=True)
    
    st.title("⚠️ SYSTEM BREACHED ⚠️")
    st.write("جاري الوصول إلى قاعدة البيانات...")
    st.write("تم ضخ جميع الملفات بنجاح.")
    st.write("تمت العملية بواسطة: كودات عبودي")
    
    time.sleep(25)
    
    st.session_state.stage = 'safe'
    st.rerun()

elif st.session_state.stage == 'safe':
    st.markdown("""
    <style>
    .stApp {background-color: white; color: black; font-family: sans-serif;}
    </style>
    """, unsafe_allow_html=True)
    
    st.success("✅ حالة النظام: آمنة")
    st.write("لا تقلق، هذا مجرد مقلب من عبودي! 😄")
