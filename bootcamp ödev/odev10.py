import datetime

guncelYil=datetime.datetime.now().year

dogumYil=int(input("Lütfen doğum yılınızı giriniz : "))

if guncelYil-dogumYil>0 and guncelYil-dogumYil<=12:
    print("Çocuksunuz")
elif guncelYil-dogumYil>12 and guncelYil-dogumYil<=17:
    print("Ergensiniz")
else:
    print("Yetişkinsiniz")