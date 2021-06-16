import smtplib
import datetime as dt
import random


my_email = "############@gmail.com"
password = "##########"

with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    now = dt.datetime.now()
    if now.weekday() == 6:
        with open("quotes.txt", "r") as f:
            data = f.readlines()
            quote = random.choice(data)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="f20190518@hyderabad.bits-pilani.ac.in",
                msg=f"Subject:KOMPRI MOTIVATION!\n\n{quote}"
            )
        print(quote)
