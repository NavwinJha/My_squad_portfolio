import smtplib as sp, ssl


def email_sent(user_text):
    host = "smtp.gmail.com"
    port = 465
    user_name = "naveenaccolite05@gmail.com"
    password = "mganwwsjznlvmdhe"
    receiver_email = "naveenaccolite05@gmail.com"
    content = ssl.create_default_context()

    with sp.SMTP_SSL(host, port, context=content) as mail:
        mail.login(user_name, password)
        mail.sendmail(user_name, receiver_email, user_text)



