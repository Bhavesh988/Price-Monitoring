import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl,smtplib

ctx= ssl.create_default_context()
ctx.check_hostname = False
ctx.verifymode = ssl.CERT_NONE

smtp_server = "smtp.gmail.com"
port = 587  # For starttls

class Flip:
	def find_p(self,_new,urla,sender_email,receiver_email,password):
		req = urllib.request.Request(urla, headers={'User-Agent': 'Mozilla/5.0'})
		html=urllib.request.urlopen(req,context=ctx).read()
		soup = BeautifulSoup(html, 'html.parser')
		name=soup.find('span', attrs={'class':"_35KyD6"}).text
		price=float(soup.find('div', attrs={'class':"_1vC4OE _3qQ9m1"}).text[1:].replace(',',""))
		rating=soup.find('div',attrs={'class':"hGSR34"}).text
		check_price(_new,urla,sender_email,receiver_email,password,name,price,rating)
		

class Amz:
	def find_p(self,_new,urla,sender_email,receiver_email,password):
		req = urllib.request.Request(urla, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'})
		html=urllib.request.urlopen(req,context=ctx).read()
		soup = BeautifulSoup(html, "lxml")
		name=soup.find('span',attrs={'id':"productTitle"}).text
		price=float(soup.find('span', attrs={'id':"priceblock_ourprice"}).text[2:].replace(',',""))
		rating=soup.find('span', attrs={'data-hook':'rating-out-of-text'}).text
		check_price(_new,urla,sender_email,receiver_email,password,name,price,rating)

def check_price(_new,urla,sender_email,receiver_email,password,name,price,rating):
	if _new.price == None:
		_new.name=name
		_new.price=price
		_new.rate=rating
		print("\n\nName of product:-{fname} \nPrice of product:-Rs {fprice} \nRating of product:-{frate}\n\n".format(fname=_new.name,fprice=_new.price,frate=_new.rate))
	elif _new.price>price:
		_new.price=price
		print("\n\nName of product:-{fname} \nNew price of product:-Rs {fprice} \nRating of product:-{frate}\n\n".format(fname=_new.name,fprice=_new.price,frate=_new.rate))
		with smtplib.SMTP(smtp_server, port) as server:
			server.ehlo()
			server.starttls(context=ctx)
			server.ehlo()
			server.login(sender_email,password)
			message=("Name is {fname} and the lower price is {cheap}".format(fname=_new.name,cheap=_new.price)).encode('utf-8')
			server.sendmail(sender_email,receiver_email,message)
	elif _new.price==price:
		print("\n\nPrice didn't reduce, you will receive an email if price is reduced\n\n")