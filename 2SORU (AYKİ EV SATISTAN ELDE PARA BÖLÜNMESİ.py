#   2.SORU:
#   Bir emlakçı satış temsilcilerine 1000TL sabit maaş ve sattığı her ev için 100TL ve satış değerinin %0.1i kadar ikramiye veriyor
#   buna göre bir satış temsilcisinin adını ve o ay sattığı evlerin adedini ve toplam değerini alan ve o ayki maaşını yazdıran program

#1.Ekrana Giriş Mesaj Yaz
print("AYKİ EV SATIŞTAN ELDE PARA BÖLÜNMESİ")

#2.Verilen sabit maaş,sabit ikramiye ve sabit ikramiye  oranı
sabit_maas=1000
her_sattigi_ev_sabit_ikramiye=100
her_sattigi_ev_ikramiye_oran=0.1

#2.Girilen Temsilcinin adını oku
tem_adi=str(input(" Temsilcinin Adını Girin : "))

#3.Girilen Satış Değerini oku
ev_degeri=float(input(" Satış Değerini Girin : "))

#4.Girilen Sattığı Ev Adedini oku
sat_adedi=int(input(" Sattığı Ev Adedini Girin : "))

#5.Toplam maaş = sabit_maas + (sat_adedi X  her_sattigi_ev_sabit_ikramiye) + (sat_adedi X  ev_degeri X her_sattigi_ev_ikramiye_oran)
toplam_maas=float(sabit_maas+(sat_adedi*her_sattigi_ev_sabit_ikramiye) + (sat_adedi*ev_degeri*her_sattigi_ev_ikramiye_oran))

#6.Toplam ondalık Yazılmalı
ondalik_toplam_maas=round(toplam_maas,2)

#7.Ekrana Toplam Temsilcinin adı ve ayki maaşını Yaz
print(tem_adi,"'in ayki Maaş ",ondalik_toplam_maas,"TL dır \n")

