import pandas as pd

data = pd.read_csv("trainmedya.csv")
print("İstatistiksel Özet:")
print(data.describe())
print("Veri Seti Bilgisi:")
print(data.info())
print("Eksik değerlerin Sayısı:")
print(data.isnull().sum())
data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])#2 adet eksik değer vardı onları modu ile doldurduk
data['Cabin'] = data['Cabin'].fillna(data['Cabin'].mode()[0])#687 adet eksik değer vardı onları modu ile doldurduk
data['Age'] = data['Age'].fillna(data['Age'].mean()) #177 adet eksik değer vardı onları ortalaması ile doldurduk
print("Boşluklar başarıyla dolduruldu")
print(data.isnull().sum())