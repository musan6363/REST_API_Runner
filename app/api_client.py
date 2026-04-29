import requests
from typing import Any

class APIHandler:
    """
    API 送信処理
    """

    def __init__(self, base_url: str) -> None:
        self.base_url: str = base_url

    def get_user_info(self) -> dict[str, Any]:
        """ユーザー情報を取得する例"""
        url: str = f"{self.base_url}/users/1"
        response: requests.Response = requests.get(url)
        return response.json()

    def add_user_info(self, id: int, name: str, email: str, role: str) -> dict[str, int]:
        """ユーザー情報を追加する例"""
        url: str = f"{self.base_url}/add_user"
        user_data: dict[str, Any] = {
            "id": id,
            "name": name,
            "email": email,
            "role": role
        }
        response: requests.Response = requests.post(url, json=user_data)
        return {
            "response": response.status_code
        }

    def post_status(self, message: str) -> dict[str, int]:
        """ステータスを更新する例"""
        url: str = f"{self.base_url}/status"
        payload: dict[str, str] = {"message": message}
        response: requests.Response = requests.post(url, json=payload)
        return {
            "response": response.status_code
        }
