import socket,time,requests
from bs4 import BeautifulSoup
import tkinter as tk

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("www.google.com", 80))
    s.close()
    print("Bağlanılıyor")

except Exception:
    print("Lütfen internet bağlantınızı kontrol ediniz")
    time.sleep(3)
    exit()

url = "https://kur.doviz.com/"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
data = soup.find("span", {"data-socket-key": "gram-altin"}).text  #hangi verileri çekmek gerek onu söylüyoruz
data2 = soup.find("span", {"data-socket-key": "USD"}).text
data3 = soup.find("span", {"data-socket-key": "EUR"}).text
data4 = soup.find("span", {"data-socket-key": "GBP"}).text
data5 = soup.find("span", {"data-socket-key": "XU100"}).text
data6 = soup.find("span", {"data-socket-key": "bitcoin"}).text
data7 = soup.find("span", {"data-socket-key": "gumus"}).text
data8 = soup.find("span", {"data-socket-key": "BRENT"}).text


window = tk.Tk()
window.geometry("500x360")
window.title("Borsa Takip Programı ./Gürkan Ticari Otomasyon")
window.configure(background="spring green")

#window.mainloop() 

label = tk.Label(window , text = "Anlık Borsa Takip" , font= "arial 15 bold" , bg="spring green")
label.pack()

gramAltin = tk.Label(window , text="Gram Altın = " , font= "arial 12" , bg="spring green")
gramAltin.pack()
gramAltin.place( x=18 , y=45 )
goldValue = tk.Label(window , text= data , font= "arial 12" , bg="spring green")
goldValue.pack()
goldValue.place(x=105 , y=45)

dolar = tk.Label(window , text="Dolar = " , font="arial 12" , bg="spring green")
dolar.pack()
dolar.place(x = 18 , y = 90)
dolarValue = tk.Label(window , text=data2 , font="arial 12",bg="spring green")
dolarValue.pack()
dolarValue.place(x=75 , y=90)

euro = tk.Label(window , text="Euro = " , font="airal 12" , bg="spring green")
euro.pack()
euro.place(x = 18 , y = 135)
euroValue = tk.Label(window , text= data3 , font= "arial 12" , bg="spring green")
euroValue.pack()
euroValue.place(x=75 , y=135)


gbp = tk.Label(window , text="Sterlin = ", font="arial 12" , bg="spring green")
gbp.pack()
gbp.place(x =18 , y=180)
gbpValue = tk.Label(window , text = data4 , font="arial 12" , bg="spring green")
gbpValue.pack()
gbp.place(x=75 , y=180)



window.mainloop()