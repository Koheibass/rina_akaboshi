from fastapi import FastAPI
import os
import resend
from fastapi.responses import HTMLResponse

resend.api_key = os.environ["RESEND_API_KEY"]

app = FastAPI()


@app.get("/api/contact")
async def read_root(name: str, email: str, message: str):
    # メール送信
    result = resend.Emails.send(
        {
            "from": "onboarding@resend.dev",  # テスト用: ドメイン認証が不要な resend.dev ドメインで送信
            "to": [email],
            "subject": "お問い合わせありがとうございます",
            "html": f"""
<div><span>email</span><strong>{email}</strong></div><br>
<div><span>name</span><strong>{name}</strong></div><br>
<div><span>message</span><strong>{message}</strong></div>""",
        }
    )

    # thank you の HTML ファイルの内容を読み込む
    with open("./thankyou_contact.html", "r", encoding="utf-8") as f:
        html = f.read()

    # TODO: 読み込んだHTMLの中の文字列を置換する
    # {
    #     "name": name,
    #     "email": email,
    #     "message": message,
    #     "result": result,
    # }

    # HTML を返す
    return HTMLResponse(content=html)
