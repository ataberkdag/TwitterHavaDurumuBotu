from datetime import datetime
import tweepy
import requests
from bs4 import BeautifulSoup
import urllib3
import time

urllib3.disable_warnings()
auth = tweepy.OAuthHandler("","")
auth.set_access_token("","")
api = tweepy.API(auth)
def main():
    deneme =0
    while True:
        saat = datetime.now()
        if saat.minute == 15 or saat.minute == 30 or saat.minute == 45 or saat.minute == 0:
            ankara = Ankara()
            istanbul = İstanbul()
            izmir = İzmir()
            kirikkale = Kirikkale()
            eskisehir = Eskişehir()
            konya = Konya()
            antalya = Antalya()
            if saat.minute == 0:
                tarih2 = (str(saat.hour) + ":" + "00")
            else:
                tarih2 = (str(saat.hour) + ":" + str(saat.minute))
            api.update_status(str(ankara) + "\n" + str(istanbul) + "\n" + str(izmir) + "\n" + str(kirikkale) + "\n" + "Saat: " + tarih2 + "\n" + "#HavaDurumu")
            api.update_status(str(eskisehir) + "\n" + str(konya) + "\n" + str(antalya) + "\n" + "Saat: " + tarih2 + "\n" + "#HavaDurumu")            
            print("Tweet Gönderildi.")
            print(ankara + "\n" + istanbul + "\n" + izmir)
            print(tarih2)
            print("Tweet Gönderildi.")
            print(str(eskisehir) + "\n" + str(konya) + "\n" + str(antalya) + "\n" + "Saat: " + tarih2 + "\n" + "#HavaDurumu")
            print(tarih2)
            time.sleep(55)
def Ankara():
    istek = requests.get("https://www.yahoo.com/news/weather/turkey/ankara/ankara-2343732",verify=False)
    soup = BeautifulSoup(istek.text,"html.parser")
    a = soup.find_all("div",{"now Fz(8em)--sm Fz(10em) Lh(0.9em) Fw(100) My(2px) Trsdu(.3s)"})
    for i in a:
        degisken = i.text
        degisken = degisken.rstrip("°FC")
    degisken = ((float(degisken))-32)/1.8
    degisken = int(degisken)
    return "Ankara Hava Durumu: " + str(degisken) + "°"
def İstanbul():
    istek = requests.get("https://www.yahoo.com/news/weather/turkey/istanbul/istanbul-2344116",verify=False)
    soup = BeautifulSoup(istek.text,"html.parser")
    a = soup.find_all("div",{"now Fz(8em)--sm Fz(10em) Lh(0.9em) Fw(100) My(2px) Trsdu(.3s)"})
    for i in a:
        degisken = i.text
        degisken = degisken.rstrip("°FC")
    degisken = ((float(degisken))-32)/1.8
    degisken = int(degisken)
    return "İstanbul Hava Durumu: " + str(degisken) + "°"
        
def İzmir():
    istek = requests.get("https://www.yahoo.com/news/weather/turkey/izmir/izmir-2344117",verify=False)
    soup = BeautifulSoup(istek.text,"html.parser")
    a = soup.find_all("div",{"now Fz(8em)--sm Fz(10em) Lh(0.9em) Fw(100) My(2px) Trsdu(.3s)"})
    for i in a:
        degisken = i.text
        degisken = degisken.rstrip("°FC")
    degisken = ((float(degisken))-32)/1.8
    degisken = int(degisken)
    return "İzmir Hava Durumu: " + str(degisken) + "°"
def Kirikkale():
    istek = requests.get("https://www.yahoo.com/news/weather/turkey/kirikkale/kirikkale-2344196",verify=False)
    soup = BeautifulSoup(istek.text,"html.parser")
    a = soup.find_all("div",{"now Fz(8em)--sm Fz(10em) Lh(0.9em) Fw(100) My(2px) Trsdu(.3s)"})
    for i in a:
        degisken = i.text
        degisken = degisken.rstrip("°FC")
    degisken = ((float(degisken))-32)/1.8
    degisken = int(degisken)
    return "Kırıkkale Hava Durumu: " + str(degisken) + "°"
def Eskişehir():
    istek = requests.get("https://www.yahoo.com/news/weather/turkey/eskisehir/eskisehir-2343980",verify=False)
    soup = BeautifulSoup(istek.text,"html.parser")
    a = soup.find_all("div",{"now Fz(8em)--sm Fz(10em) Lh(0.9em) Fw(100) My(2px) Trsdu(.3s)"})
    for i in a:
        degisken = i.text
        degisken = degisken.rstrip("°FC")
    degisken = ((float(degisken))-32)/1.8
    degisken = int(degisken)
    return "Eskişehir Hava Durumu: " + str(degisken) + "°"
def Konya():
    istek = requests.get("https://www.yahoo.com/news/weather/turkey/konya/konya-2344210",verify=False)
    soup = BeautifulSoup(istek.text,"html.parser")
    a = soup.find_all("div",{"now Fz(8em)--sm Fz(10em) Lh(0.9em) Fw(100) My(2px) Trsdu(.3s)"})
    for i in a:
        degisken = i.text
        degisken = degisken.rstrip("°FC")
    degisken = ((float(degisken))-32)/1.8
    degisken = int(degisken)
    return "Konya Hava Durumu: " + str(degisken) + "°"
def Antalya():
    istek = requests.get("https://www.yahoo.com/news/weather/turkey/antalya/antalya-2343733",verify=False)
    soup = BeautifulSoup(istek.text,"html.parser")
    a = soup.find_all("div",{"now Fz(8em)--sm Fz(10em) Lh(0.9em) Fw(100) My(2px) Trsdu(.3s)"})
    for i in a:
        degisken = i.text
        degisken = degisken.rstrip("°FC")
    degisken = ((float(degisken))-32)/1.8
    degisken = int(degisken)
    return "Antalya Hava Durumu: " + str(degisken) + "°"
main()
       
