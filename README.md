# REST API 操作アプリ

任意の REST API が実行可能なアプリ

## 環境

- Python
  - mise
  - uv


## 使い方

```bash:
# mock server
mise run server

# app
mise run app
```

## 実装

各ファイルの役割は以下の通り．

```bash
├── README.md  # 本ファイル
├── app  # アプリ本体
│   ├── api_client.py  # 送信するAPIの定義
│   ├── app.py  # アプリホーム画面のデザイン
│   ├── components.py  # Streamlit Element の wrapper
│   └── pages_config.py  # 各ページのデザイン
├── mock  # テスト用
│   └── server.py  # APIのモックレスポンスを定義
├── pyproject.toml
└── uv.lock
```

### チュートリアル

1. `app/components.py` には， Streamlit の Element をベースに，APIを実行，結果をハンドリングする処理を定義する．
2. `app/api_client.py` には，送信したいAPIのRequestを定義する．
3. `app/pages_config.py` に描画するページのデザインを定義する．このとき，`app/components.py` で用意した部品を使う．
4. `app/app.py` に，`app/pages_config.py` で定義した各ページを並べる．

### デザイン

- Streamlit が利用可能 (streamlit>=1.57.0)
  - [Streamlit API reference](https://docs.streamlit.io/develop/api-reference)
