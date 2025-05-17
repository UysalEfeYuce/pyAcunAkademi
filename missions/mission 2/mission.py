import pandas as pd

data = pd.read_csv("trainmedya.csv")
print("Veri Setinin ilk 5 satırı:")#İLk 5 satırı gösterir
print(data.head())
print("İstatistiksel Özet:")#Bütün bilgelerin ortalama istatiki bilgisi
print(data.describe())
print("Veri Seti Bilgisi:")#Sütünların türünü söyler
print(data.info())
print("Eksik değerlerin Sayısı:")
print(data.isnull().sum())#Hangi sütünda ne kadar girilmemiş değer olduğunu söyler
data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])#2 adet eksik değer vardı onları modu ile doldurdum
data['Cabin'] = data['Cabin'].fillna(data['Cabin'].mode()[0])#687 adet eksik değer vardı onları modu ile doldurdum
data['Age'] = data['Age'].fillna(data['Age'].mean()) #177 adet eksik değer vardı onları ortalaması ile doldurdum
print("Boşluklar başarıyla dolduruldu")
print(data.isnull().sum())
