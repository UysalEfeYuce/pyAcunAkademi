sayiAl = int(input("En son hangi değere kadar toplansın?\n"))#Kuallanıcıdan bir sayı alıyoruz
toplam = 0
for i in range(sayiAl + 1):#Range ile 1 ile 100 i nin for döngüsünde gezmesini sağlıyoruz
    toplam += i

print("Toplamı:",toplam)