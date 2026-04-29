import streamlit as st
from api_client import APIHandler
import pages_config

st.set_page_config(page_title="REST API Controller", layout="wide")

# 設定画面
st.sidebar.title("App Settings")
ip_address = st.sidebar.text_input(
    "Target", 
    value="http://localhost:8888",
)
api_handler = APIHandler(base_url=ip_address)

# ページ選択
page = st.sidebar.radio("Page", ["Page1", "Info"])

if page == "Page1":
    pages_config.render_page1(api_handler)
elif page == "Info":
    pages_config.render_info(api_handler)