
# Game sederhana

from time import sleep
import random,os,sys

# Warna

D = '\033[0m'  # white (default)
M  = '\033[1;31m' # red
I = '\033[1;32m' # green bold
Y  = '\033[1;33m' # yellow
B  = '\033[1;34m' # blue
P  = '\033[1;35m' # purple
C  = '\033[1;36m' # cyan
GR = '\033[1;37m' # gray


print(C+"===============Game Sederhana================")
print(Y+"pilih mau yang mana  : \n1. Batu\n2. Kertas\n3. Gunting\n")

# Fungsi

def game():
    
    nama = str(input(I+"masukan nama kamu dulu : "))
    pilihan = int(input(I+"masukan nomor : "))
    kom = random.choice (["kertas" , "batu", "gunting"])
    if pilihan == 1:
        sleep(1)
        print (P+"Tuan  "+ nama +" pilih : batu")
        sleep(1)
        print (C+"komputer : " , kom)
        if kom == "batu" :
            print (I+"draw")
            sleep(1)
            ulang()
            
        elif kom == " kertas" :
            print (M+"ya lo ama komputer aja kalah wkwk")
            ulang()
        else:
            print(I+"lo menang bro!!")
            ulang()
    
    elif pilihan == 2:
        sleep(1)
        print(P+"Tuan  "+ nama +" pilih : kertas")
        sleep(1)
        print(C+"komputer : ", kom)
        if kom == "batu":
            print(I+"kamu menang")
            sleep(1)
            ulang()
        elif kom == "kertas":
            print(I+"draw bro!!!")
            sleep(1)
            ulang()
        else:
            print(M+"bot menang, lu kalah wkwk")
            sleep(1)
            ulang()
    
    elif pilihan == 3:
        sleep(1)
        print (P+"Tuan  :  "+ nama +" pilih :  gunting")
        sleep(1)
        print (C+"komputer : " , kom)
        
        if kom == "batu":
           print (M+"kamu kalah")
           sleep(1)
           ulang()
           
        elif kom == "kertas":
           print (I+"kamu menang")
           os.system("clear")
           sleep(1)
           ulang()
        else:
           print(I+"lo draw bro!!")
           sleep(1)
           ulang()
    
    else:
        print(M+"opsi cuma ada 3 bro")
        sleep(1)
        os.system("clear")
        sys.exit()         

def ulang():
    pilihan = str(input(Y+"mau maen lagi? >> "))
    while True:
        if pilihan == 'y':
            print(C+"oke kita maen!")
            sleep(1)
            os.system("clear")
            game()
        elif pilihan == 't':
            print(B+"Good bye :)")
            sleep(1)
            sys.exit()
        else:
            print(M+"opsi hanya ada 2 : [y/t]")
            sleep(1)
            sys.exit()


game()