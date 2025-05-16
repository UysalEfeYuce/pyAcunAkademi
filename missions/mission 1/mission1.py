sayi1=int(input("1. Sayıyı giriniz:"))#Kullanıcıdan bir sayı alıyoruz
sayi2=int(input("2. Sayıyı giriniz:"))#Kullanıcıdan bir sayı alıyoruz

işlem=int(input("Yapıcağınız işlemi seçin\n(1-Toplama 2-Çıkarma 3-Çarpma 4-Bölme 5-Mod alma 6-Üs alma:)"))#Yapacağı işlemi seçtirip if elseye yönlendiriyorum

if(işlem==1):#Eğer seçtiği işlem 1 ise bu blok çalışır
    print("Sonuc:",sayi1+sayi2)
elif(işlem==2):#Eğer seçtiği işlem 2 ise bu blok çalışır
    print("Sonuc:",sayi1-sayi2)
elif(işlem==3):#Eğer seçtiği işlem 3 ise bu blok çalışır
    print("Sonuc:",sayi1*sayi2)
elif(işlem==4):#Eğer seçtiği işlem 4 ise bu blok çalışır
    print("Sonuc:",sayi1/sayi2)
elif(işlem==5):#Eğer seçtiği işlem 5 ise bu blok çalışır
    print("Sonuc:",sayi1%sayi2)
else:#Eğer seçtiği işlem 6 veya başka sayı ise bu blok çalışır
    print("Sonuc:",sayi1**sayi2)