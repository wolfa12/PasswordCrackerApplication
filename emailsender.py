import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "actualnotfaketwitter@gmail.com"
receiver_email = "johnson.6973@osu.edu"
password = "g0buckeyes"
message = """\
Subject: URGENT: PASSWORD COMPROMISED

Valued User

We have detected suspicious activity on you're account. Update your password to avoid your data being compromised."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

print("sent")
