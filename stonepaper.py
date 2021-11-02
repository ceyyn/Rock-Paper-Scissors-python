from random import choice
from time import sleep

def intr():
    red = "\033[31m"
    u = "\033[0m"
    c = "\033[95m"
    s , b = 0 , 0
    while True:
        print(c + """''Taş Kağıt Makas Oyunu''*if you want to exit enter 'E'*
        1 : Taş
        2 : Kağıt
        3 : Makas""")
        q = input("Taş-Kağıt-Makas : "+u)
        if q == "E":
            print(c + "GG. So Long."+ u)
            break
        List= ["Taş", "Kağıt","Makas"]
        List = choice(List)
        if q == "1" and List == "Taş":
            q = "Taş"
            result = "Eşit"
        elif q == "1" and List == "Kağıt":
            q = "Taş"
            result = "Bilgisayar kazandı"
        elif q == "1" and List == "Makas":
            q = "Taş"
            result = "Kazandın"
        
        elif q == "2" and List == "Taş":
            q = "Kağıt"
            result = "Kazandın"
        elif q == "2" and List == "Kağıt":
            q = "Kağıt"
            result = "Eşit"
        elif q == "2" and List == "Makas":
            q = "Kağıt"
            result = "Bilgisayar kazandı"
        
        elif q == "3" and List == "Taş":
            q = "Makas"
            result = "Bilgisayar kazandı"
        elif q == "3" and List =="Kağıt":
            q = "Makas"
            result = "Kazandın"
        elif q == "3" and List == "Makas":
            q = "Makas"
            result = "Eşit"
        else :
            result = "Anlaşılamadı"
        
        if result == "Bilgisayar kazandı":
            b += 1
        elif result == "Kazandın":
            s += 1
        elif result == "Eşit":
            b += 1
            s += 1
        if not result == "Anlaşılamadı":
            sleep(0.3)
            print(q , "—" , List)
            sleep(0.3)
            print(red + result + u)
            sleep(0.3)
            print(s , "—" , b)
            sleep(0.3)
        else:
            sleep(0.3)
            print(red + result + u)
intr()

