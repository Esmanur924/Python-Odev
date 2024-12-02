# 1- "Toyota, Bmw, Renault, Mercedes" elemanlarına sahip markalar isimli bir liste oluşturunuz.

markalar=["Toyota" , "Bmv" , "Renault" , "Mercedes"]
sonuc=len(markalar)
sonuc= markalar + ["Go" , "Delphi"]
print(markalar)
# 2- Liste kaç elemanlıdır?
print(len(markalar))
# 3- Listenin ilk ve son elemanı nedir?
print(markalar[0])
print(markalar[3])
# 4- "Renault" markasını "Togg" ile güncelleyiniz.
sonuc= "Renault" in markalar
sonuc= "React" in markalar
markalar[2]= "Togg"
print(markalar)
# 5- "Togg" listenin bir elemanı mıdır?
print(markalar[2])
# 6- Listenin sonuna "Ford" ve "Citroen" markalarını ekleyiniz.
markalar.append("Ford")
markalar.append("Citroen")
print(markalar)
# 7- Listenin son elemanını siliniz.
del(markalar[5])
print(markalar)
# 8- Aşağıdaki verileri liste içerisinde saklayınız (Liste içinde liste mümkündür.).


    # öğrenci1: Yiğit Bilgi 2010 [70,80,90]
    # öğrenci2: Ada Bilgi   2011 [70,70,80]
    # öğrenci3: Çınar Turan 2017 [60,60,90]

ogrenci1="Yiğit", "Balcı" ,2010 , [70,80,90]
ogrenci2="Ada" , "Balcı" , 2011 , [70,70,80]
ogrenci3="Çınar" ,"Turan" , 2017 , [60,60,90]

# 9- Öğrencilerin yaşlarını hesaplayınız.
ogrenci1yas= 2024-ogrenci1[2]
ogrenci2yas= 2024-ogrenci2[2]
ogrenci3yas= 2024-ogrenci3[2]
print(ogrenci1yas)
print(ogrenci2yas)
print(ogrenci3yas)
# 11- Öğrencilerin not ortalamalarını hesaplayınız.
ogrenci1ort= (ogrenci1[3][0] + ogrenci1[3][1] + ogrenci1[3][2])/ 3
ogrenci2ort= (ogrenci2 [3][0] + ogrenci2[3][1] + ogrenci2[3][2])/ 3
ogrenci3ort= (ogrenci3[3][0] + ogrenci3[3][1] + ogrenci3 [3][2])/ 3
print(ogrenci1ort)
print(ogrenci2ort)
print(ogrenci3ort)