# AygazPythonCamp
Aygaz Python Camp
Bu Python kodu, Taş, Kâğıt, Makas oyununun kurallarına göre oynanmasını sağlayan bir oyun oluşturur. Kodu parça parça açıklayalım:
1. Gerekli Modül ve Fonksiyon Tanımları
import random
•	random modülü, bilgisayarın seçimlerini rastgele yapabilmesi için kullanılır.
2. Ana Fonksiyon: tas_kagit_makas_GULCAN_AYDIN
def tas_kagit_makas_GULCAN_AYDIN():
•	Bu fonksiyon, oyunun tamamını kontrol eder. Kullanıcı bu fonksiyonu çalıştırarak oyunu başlatabilir.
3. Oyunun Tanıtımı
    print("Taş, Kağıt, Makas Oyununa Hoşgeldiniz!")
    print("Kurallar: Taş makası kırar, makas kağıdı keser, kağıt taşı sarar.")
    print("İlk iki turu kazanan oyunun galibi olur. Başarılar!")
•	Bu kısımda, kullanıcıya oyunun kuralları ve nasıl oynanacağı hakkında bilgi verilir.

5. Seçenekler ve Sayaçlar
    options = ["taş", "kağıt", "makas"]

    oyun_sayisi = 0
    oyuncu_galibiyet = 0
    bilgisayar_galibiyet = 0
•	options: Oyuncunun ve bilgisayarın seçebileceği üç seçenek tanımlanır.
•	oyun_sayisi: Oynanan oyunların toplam sayısını takip eder.
•	oyuncu_galibiyet ve bilgisayar_galibiyet: Oyuncu ve bilgisayarın kazandığı oyunların sayısını takip eder.
6. Oyunun Ana Döngüsü
    while True:
        oyun_sayisi += 1
        print(f"\nOyun {oyun_sayisi} başlıyor!")
•	while True: Bu döngü, kullanıcı ve bilgisayar "devam etmek istemediğini" belirtmediği sürece sürekli çalışır. Her döngü yeni bir oyunu temsil eder.
7. Tur Döngüsü ve Oyun İşleyişi
        oyuncu_tur_sayaci = 0
        bilgisayar_tur_sayaci = 0

        while oyuncu_tur_sayaci < 2 and bilgisayar_tur_sayaci < 2:
            oyuncu_secimi = input("Taş, Kağıt, Makas seçin: ").lower()
            while oyuncu_secimi not in options:
                print("Geçersiz seçenek! Lütfen tekrar seçin.")
                oyuncu_secimi = input("Taş, Kağıt, Makas seçin: ").lower()

            bilgisayar_secimi = random.choice(options)
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")
•	oyuncu_tur_sayaci ve bilgisayar_tur_sayaci: Her oyun iki turu kazanan tarafından kazanılır, bu sayaçlar bu durumu izler.
•	while oyuncu_tur_sayaci < 2 and bilgisayar_tur_sayaci < 2: Bu döngü, biri iki tur kazanana kadar devam eder.
•	input: Kullanıcıdan seçim yapması istenir. Eğer geçersiz bir seçim yapılırsa, tekrar seçim yapması istenir.
•	random.choice(options): Bilgisayarın seçimi rastgele yapılır.
7. Tur Sonucunu Belirleme
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

            print(f"Skor: Oyuncu {oyuncu_tur_sayaci} - Bilgisayar {bilgisayar_tur_sayaci}")
•	Bu kısımda, oyuncunun seçimi ile bilgisayarın seçimi karşılaştırılır ve turun galibi belirlenir. Galip olanın tur sayacı artırılır ve skor ekranda gösterilir.
8. Genel Galibi Belirleme
        if oyuncu_tur_sayaci == 2:
            print("Tebrikler! Bu oyunu siz kazandınız!")
            oyuncu_galibiyet += 1
        else:
            print("Bilgisayar bu oyunu kazandı!")
            bilgisayar_galibiyet += 1
•	Bir oyuncu iki tur kazandığında oyunun galibi belirlenir ve genel galibiyet sayısı güncellenir.
9. Oyuna Devam Etme İsteği
        devam = input("Başka bir oyun oynamak ister misiniz? (evet/hayır): ").lower()
        bilgisayar_devam = random.choice(["evet", "hayır"])
        print(f"Bilgisayarın devam etme isteği: {bilgisayar_devam}")

        if devam == "hayır" or bilgisayar_devam == "hayır":
            break
•	Kullanıcı ve bilgisayara oyuna devam etmek isteyip istemedikleri sorulur. Eğer herhangi biri devam etmek istemezse döngü sona erer.
10. Sonuçları Gösterme
    print("\nOyun Bitti!")
    print(f"Oynanan toplam oyun sayısı: {oyun_sayisi}")
    print(f"Toplam oyuncu galibiyeti: {oyuncu_galibiyet}")
    print(f"Toplam bilgisayar galibiyeti: {bilgisayar_galibiyet}")
    print("Teşekkürler, tekrar görüşmek üzere!")
•	Oyun bittiğinde, oynanan oyun sayısı ve kazananların sayısı gösterilir.
Bu kod, Python'un temel yapı taşlarını kullanarak, eğlenceli bir şekilde taş, kâğıt, makas oyununu simüle eder. Oyun akışı hem kullanıcıya hem de bilgisayara adil bir şekilde sağlanır.
