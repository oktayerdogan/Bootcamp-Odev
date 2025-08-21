urun1=int(input("1. ürünün fiyatını giriniz : "))
urun2=int(input("2. ürünün fiyatını giriniz : "))
urun3=int(input("3. ürünün fiyatını giriniz : "))

toplam=(urun1+urun2+urun3)

if toplam>200:
    indirimMiktari=toplam*10/100
    toplam-=indirimMiktari
print("Toplam Tutar : ",toplam)