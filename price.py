import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/dp/B00RJQ8XHU/?coliid=I277Q723DRM1CP&colid=3BPRLHQ5R23QK&psc=1&ref_=lv_ov_lig_dp_it'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers =headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()

    price = soup.find(id="priceblock_ourprice").get_text()

    converted_price = float(price[2:5])

    if(converted_price > 650):
        send_mail()


    print(converted_price)
    print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()


    server.login('xx@xx.com', 'password123')

    subject = 'Price for Jopasu Car Duster has fallen down!'
    body = f'Check the Amazon Link {URL}'

    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        'mailFrom',
        'mailTo',
        msg
    )

    print('Email has been sent')

    server.quit


check_price()