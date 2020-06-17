#!/usr/bin/python3
#Created by Kanti
import os
import time
import pyshorteners
from time import sleep

os.system('clear')

def Main():
    print("\033[93m--------------------------------------------")
    print("                URLKANTI v1.0                   ")
    print("   დამალეთ თქვენი URL სოციალური ინჟინერიის გამოყენებით   ")
    print("                           @KantiMRX   ")
    print("--------------------------------------------")
    print("\n[*1]  Google")
    print("[*2]  Youtube")
    print("[*3]  Spotify")
    print("[*4]  Instagram")
    print("[*5]  Facebook")
    print("[*7]  Personalized")
    print("\n[*99]  პროგრამის გამორთვა")
    Selector()


def Selector():
    select = int(input("\nაირჩიეთ პარამეტრი: "))
    if select == 1:
        EnlaceGoogle()
    elif select == 2:
        EnlaceYoutube()
    elif select == 3:
        EnlaceSpotify()
    elif select == 4:
        EnlaceInstagram()
    elif select == 5:
        EnlaceFacebook()    
    elif select == 7:
        EnlacePersonalized()
    elif select == 99:
        os.system('clear')
        print("ნახვამდის...")
        sleep(1)
        os.system('clear')
        exit()
    else:
        os.system('clear')
        print("შეცდომა,სცადეთ თავიდან...")
        sleep(1)
        os.system('clear')
        Main()


def EnlaceGoogle():
    os.system('clear')
    print("თქვენ აირჩიეთ Google")
    OriginalLink = str(input("\nნადმვილი URL: "))
    
    print("\nშეიყვანეთ მსგავსი წინადადება:rogor-daviklot-wonashi")
    Postlink = str(input("\nლინკზე არსებული წინადადება,წინადადება აუცილებლად შეიყვანეთ ლათინური ალფაბეტით: "))
    os.system('clear')
    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.chilpit.short(OriginalLink)
    Withouthttp = EndLink[7:]
    print(f"\nთქვენი ლინკი: https://www.google.com-{Postlink}@{Withouthttp}")
    Other()

def EnlaceYoutube():
    os.system('clear')
    print("თქვენ აირჩიეთ Youtube.")
    OriginalLink = str(input("\nნამდვილი URL: "))
    
    print("\nშეიყვანეთ რაიმე მსგავსი: vaime-xalxo-saswaulia")
    Postlink = str(input("\nლინკზე არსებული წინადადება,წინადადება აუცილებლად შეიყვანეთ ლათინური ალფაბეტით: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.chilpit.short(OriginalLink)
    Withouthttp = EndLink[7:]
    os.system('clear')
    print(f"\nთქვენი ლინკი: https://www.youtube.com-video-{Postlink}@{Withouthttp}")
    
    Other()

def EnlaceSpotify():
    os.system('clear')
    print("თქვენ აირჩიეთ Spotify ")
    OriginalLink = str(input("\nOriginal URL: "))
    
    print("\nშეიყვანეთ რაიმე მსგავსი:axali-simgera-naxet-yvelam")
    Postlink = str(input("\n:ლინკზე არსებული წინადადება,წინადადება აუცილებლად შეიყვანეთ ლათინური ალფაბეტით: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.chilpit.short(OriginalLink)
    Withouthttp = EndLink[7:]
    os.system('clear')
    print(f"\nთქვენი ლინკი: https://www.spotify.com-video-{Postlink}@{Withouthttp}")
    
    Other()

def EnlaceInstagram():
    os.system('clear')
    print("თქვენ აირჩიეთ ინსტაგრამი")
    OriginalLink = str(input("\nნადმვილი URL: "))
    
    print("\nშეიყვანეთ რაიმე მსგავსი: axali-foto-pizza")
    Postlink = str(input("\nლინკზე არსებული წინადადება,წინადადება აუცილებლად შეიყვანეთ ლათინური ალფაბეტით: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.chilpit.short(OriginalLink)
    Withouthttp = EndLink[7:]
    os.system('clear')
    print(f"\nთქვენი ლინკი: https://www.instagram.com-photo-{Postlink}@{Withouthttp}")
    
    Other()

def EnlaceFacebook():
    os.system('clear')
    print("თქვენ აირჩიეთ Facebook")
    OriginalLink = str(input("\nნამდვილი URL: "))
    
    print("\nშეიყვანეთ რაიმე მსგავსი: naxet-rogor-cxovroben-kaxetshi")
    Postlink = str(input("\nლინკზე არსებული წინადადება,წინადადება აუცილებლად შეიყვანეთ ლათინური ალფაბეტით: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.chilpit.short(OriginalLink)
    Withouthttp = EndLink[7:]
    
    print(f"\nთქვენი ლინკი: https://www.facebook.com-profile-{Postlink}@{Withouthttp}")
    os.system('clear')
    Other()


def EnlacePersonalized():
    os.system('clear')
    print("თქვენ აირჩიეთ CUSTOM")
    Domain = str(input("Example.com/es... შეიყვანეთ დომენი: "))
    OriginalLink = str(input("\nნამდვილი URL: "))
    
    print("\nშეიყვანეთ რაიმე მსგავსი: news-in-forntite ")
    Postlink = str(input("\nლინკზე არსებული წინადადება,წინადადება აუცილებლად შეიყვანეთ ლათინური ალფაბეტით: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.chilpit.short(OriginalLink)
    Withouthttp = EndLink[7:]
    os.system('clear')
    print(f"\nთქვენი ლინკი: https://www.{Domain}-{Postlink}@{Withouthttp}")
    
    Other()

def Other():
    print("\033[93m\nგინდათ პროგრამის თავიდან ჩატვირთვა?")
    print("დიახ [*1] \nარა  [*2]")
    select=int(input("\nაირჩიეთ : "))
    if select == 1:
        os.system('clear')
        Main()
    else:
        os.system('clear')
        exit()

#SYSCALL

Main()
