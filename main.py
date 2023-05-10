import time

def ceviri(girdi):
    liste = girdi.split(":")
    toplam_saniye = (int(liste[0]) * 3600 + int(liste[1]) * 60 + int(liste[2]))
    return toplam_saniye

print("""
kaç saat kaç dakika olacağını aralarında : olacak şekilde giriniz
""")

girdi = input()
t = ceviri(girdi)

while  t >= 0:
    bolum, secs = divmod(t, 60)
    hours, mins  = divmod(bolum, 60)
    print(f"{hours}:{mins}:{secs}",end="\r")
    time.sleep(1)
    t -= 1
print("time is over")