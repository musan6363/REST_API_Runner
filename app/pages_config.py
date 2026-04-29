import streamlit as st
from components import ApiButton
from api_client import APIHandler

"""
描画対象のページ管理
"""

def render_page1(api_handler: APIHandler) -> None:
    st.header("API Runner 1")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # get user
        get_user_btn = ApiButton(
            "ユーザー取得", 
            api_handler.get_user_info
        )
        get_user_btn.render()
        
        # add user
        with st.popover("ユーザー追加"):
            st.markdown("### 新規ユーザー")
            new_id: int = st.number_input("ID", min_value=0, step=1)
            new_name: str = st.text_input("Name")
            new_email: str = st.text_input("Email")
            new_role: str = st.selectbox("Role", ["Admin", "User", "Guest"])
            add_user_btn = ApiButton(
                "登録",
                api_handler.add_user_info,
                args={
                    "id": new_id,
                    "name": new_name,
                    "email": new_email,
                    "role": new_role
                }
            )
            add_user_btn.render()
        
    with col2:
        # greet
        greet_btn = ApiButton(
            "挨拶を送る", 
            api_handler.post_status, 
            args={"message": "Hello!"}
        )
        greet_btn.render()
        

def render_info(api_handler: APIHandler) -> None:
    st.header("Info")
    st.info(f"現在の接続先: {api_handler.base_url}")