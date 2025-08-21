vize=int(input("vize notunuzu girin : "))
final=int(input("final notunuzu girin : "))

ortalama=float((vize+final)/2)
print("ortalamanız : ",ortalama)

if ortalama>=50:
    print("Gecti")
else:
    print("kaldı")