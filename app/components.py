import streamlit as st
from typing import Callable, Any

class ApiButton:
    """
    API を実行するボタンの管理
    """
    
    def __init__(
        self, 
        label: str, 
        api_func: Callable[..., Any], 
        args: dict[str, Any] | None = None, 
        use_container_width: bool = True
    ) -> None:
        self.label = label
        self.api_func = api_func
        self.args = args or {}
        self.use_container_width = use_container_width  # 親要素の幅に合わせる

    def render(self) -> None:
        if st.button(self.label, use_container_width=self.use_container_width):
            try:
                result: Any = self.api_func(**self.args)
                st.success(f"Success: {self.label}")
                st.json(result)
            except Exception as e:
                st.error(f"Error occurred: {e}")