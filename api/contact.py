from fastapi import FastAPI
import os
import resend
from fastapi.responses import HTMLResponse

resend.api_key = os.environ["RESEND_API_KEY"]

app = FastAPI()


@app.get("/api/contact")
async def read_root(name: str, email: str, message: str, type: str):
    # メール送信
    if name == "RobertErero":
        return
    if type == "????":
        return
    result = resend.Emails.send(
        {
            "from": "info2@rina-akaboshi.com",
            "to": [email],
            "bcc": "kouheihand@yahoo.co.jp",
            "subject": "【赤星里奈】お問い合わせありがとうございます",
            "html": f""" <div><span></span><strong>{name}様</strong></div>
      <p>この度は、お問い合わせいただきまして誠にありがとうございます。</p>
      <p>以下の内容でお問い合わせを受付いたしました。</p>
      <p>担当者より改めてご連絡させていただきます。</p>
      <div><span>お名前：</span><strong>{name}</strong></div><br>
<div><span>メール：</span><strong>{email}</strong></div><br><div><span>お問い合わせの種別：</span><strong>{type}</strong></div><br>
<div><span>お問い合わせ内容：</span><strong>{message}</strong></div>""",
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
