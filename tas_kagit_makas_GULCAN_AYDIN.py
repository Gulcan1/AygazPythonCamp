# -*- coding: utf-8 -*-
"""Colaboratory'ye Hoş Geldiniz

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

import random

def tas_kagit_makas_GULCAN_AYDIN():
    # Oyunun tanıtımı
    print("Taş, Kağıt, Makas Oyununa Hoşgeldiniz!")
    print("Kurallar: Taş makası kırar, makas kağıdı keser, kağıt taşı sarar.")
    print("İlk iki turu kazanan oyunun galibi olur. Başarılar!")

    # Seçenekler listesi
    options = ["taş", "kağıt", "makas"]

    # Sayaçlar
    oyun_sayisi = 0
    oyuncu_galibiyet = 0
    bilgisayar_galibiyet = 0

    # Oyunun ana döngüsü
    while True:
        oyun_sayisi += 1
        print(f"\nOyun {oyun_sayisi} başlıyor!")

        # Tur sayaçlarını sıfırla
        oyuncu_tur_sayaci = 0
        bilgisayar_tur_sayaci = 0

        # Turların döngüsü
        while oyuncu_tur_sayaci < 2 and bilgisayar_tur_sayaci < 2:
            # Oyuncu seçimi
            oyuncu_secimi = input("Taş, Kağıt, Makas seçin: ").lower()
            while oyuncu_secimi not in options:
                print("Geçersiz seçenek! Lütfen tekrar seçin.")
                oyuncu_secimi = input("Taş, Kağıt, Makas seçin: ").lower()

            # Bilgisayar seçimi
            bilgisayar_secimi = random.choice(options)
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")

            # Turun sonucunu belirleme
            if oyuncu_secimi == bilgisayar_secimi:
                print("Bu tur berabere!")
            elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or \
                 (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt") or \
                 (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş"):
                print("Bu turu siz kazandınız!")
                oyuncu_tur_sayaci += 1
            else:
                print("Bu turu bilgisayar kazandı!")
                bilgisayar_tur_sayaci += 1

            # Güncel skorları göster
            print(f"Skor: Oyuncu {oyuncu_tur_sayaci} - Bilgisayar {bilgisayar_tur_sayaci}")

        # Genel galibi belirleme
        if oyuncu_tur_sayaci == 2:
            print("Tebrikler! Bu oyunu siz kazandınız!")
            oyuncu_galibiyet += 1
        else:
            print("Bilgisayar bu oyunu kazandı!")
            bilgisayar_galibiyet += 1

        # Oyuna devam etme isteği
        devam = input("Başka bir oyun oynamak ister misiniz? (evet/hayır): ").lower()
        bilgisayar_devam = random.choice(["evet", "hayır"])
        print(f"Bilgisayarın devam etme isteği: {bilgisayar_devam}")

        if devam == "hayır" or bilgisayar_devam == "hayır":
            break

    # Sonuçları gösterme
    print("\nOyun Bitti!")
    print(f"Oynanan toplam oyun sayısı: {oyun_sayisi}")
    print(f"Toplam oyuncu galibiyeti: {oyuncu_galibiyet}")
    print(f"Toplam bilgisayar galibiyeti: {bilgisayar_galibiyet}")
    print("Teşekkürler, tekrar görüşmek üzere!")

# Oyunu başlat
tas_kagit_makas_GULCAN_AYDIN()