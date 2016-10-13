import math

#   1.SORU:
#   kullanıcının şu anki zamanın saat ve dakıka ayrı tam sayılar olarak kullanan,
#   ayrıca eklenecek dakıka sayısını kullanan ve şu anki zamana bu dakıkaların eklenmesi ile bulunacak zaman yazdıran program.

#1.Ekrana Açıklama Mesaj Yaz
print("ŞU ANKİ ZAMANA DAKIKALARI EKLEYEN PROGRAM")

#2.Girilen Şu anki Saati oku
suanki_saat=int(input(" Şu anki Saati girin : "))

#3.Girilen saati kontrol et : suanki_saat>24 ya da suanki_saat<0 iken Ekrana hata mesaji Yaz. Değilse Devam edin
while((suanki_saat>24) or (suanki_saat<0)):
    print(" Geçersiz Saat giriş. Tekrar Deneyin")
    suanki_saat=int(input(" Şu anki Saati girin : "))

#4.Girilen Şu anki dakıkayı oku
suanki_dakika=int(input(" Şu anki Dakıkayı girin : "))

#5.Girilen dakıkayı kontrol et : suanki_dakika<0 ya da suanki_dakika>=60 iken Ekrana hata mesaji Yaz. Değilse Devam edin
while(suanki_dakika<0 or suanki_dakika>=60):
    print(" Geçersiz Dakika giriş. Tekrar Deneyin")
    suanki_dakika=int(input(" Şu anki Dakıkayı girin : "))

#6.Ekrana şu anki zamanı Yaz
print(" ŞU ANKİ ZAMAN ",suanki_saat,":",suanki_dakika," dir")

#7.Girilen Eklenen dakıkayı oku
eklenen_dakika=int(input(" Eklenecek Dakıkayı girin : "))

#8.Dakika Toplami = eklenen_dakika + suanki_dakika
dakika_toplam=suanki_dakika+eklenen_dakika
    
#9.Girilen eklenecek dakıka ve şu anki dakıka Toplamını kontrol et : Eğer eklenen_dakika>=60 ise dakıkalardan saatlere dönüştür
if(dakika_toplam>=60):
    suanki_dakikadan_bulunan_saat=math.trunc(dakika_toplam/60)
    yeni_dakika=dakika_toplam%60
    yeni_saat=suanki_saat+suanki_dakikadan_bulunan_saat
else:
    yeni_dakika=dakika_toplam
    yeni_saat=suanki_saat

#10.Aldığımız yeni saati kontrol et : Eğer yeni_saat>=24 ise saatlerden günlere dönüştür
#    Daha Uzun olacağı için böşver buna <.^|^.> Ama mantıklı olması için yapmalıyız
#    çünkü Eğer çok dakakı olursa saatler de arttırır da 24'ten daha saat olacak
#    Mesela 26:45 Aklımıza geliyor mi ?

#4.Ekrana Yeni zamanı Yaz
print("\n YENI ZAMAN ",yeni_saat,":",yeni_dakika," dir\n")


