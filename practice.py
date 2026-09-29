
team = "Galatasaray"
print(team)

points = 42
ratio = 3.5
is_champion = False

print (points)
print (ratio)
print(is_champion)

# type() : Python sana her değişkenin tipini söylüyor.
print(type(team))  
print(type(points))
print(type(ratio))
print(type(is_champion))

teams = ["Galatasaray", "Besiktas", "Fenerbahce"]
print(teams)

print(teams[0])
print (len(teams)) # kac eleman var listede 

teams.append ("Trabzonspor") # listeye eleman ekleme
print(teams)
print(len(teams))

#Buradaki kilit nokta: liste sıralıdır ve elemanlara sayıyla erişilir. Bir sonraki adımda dict göreceksin, orada sıra değil isim var.

team_info = {
    "name": "Galatasaray",
    "founded" : 1905,
    "points": 42 
}

print(team_info)
print(team_info["name"])    # Burada ["name"] var, [0] değil. Çünkü dict'te sıra yok, anahtar var.

team_info["coach"] = "Okan Buruk"
team_info["points"] = 45 # Olmayan anahtar yazarsan ekler, olan anahtarı yazarsan günceller.
print(team_info)

#Dict'i iyi öğren, çünkü JSON'un Python karşılığı bu. 
#FastAPI'da endpoint'lerden döndüreceğin şey dict olacak, frontend'e giden veri bu yapıda gidecek. 
#Frontend-backend ilişkisinin Python tarafı burada başlıyor.


league = [
    {"name": "Galatasaray", "points": 42},
    {"name": "Fenerbahce", "points": 39},
    {"name": "Kasimpasa", "points": 15}
]

print(league) 
print(league[0])
print(league[0]["name"])     # Soldan sağa oku: önce listeden 0. elemanı al, sonra o dict'ten "name" anahtarını al.
print(league[2]["points"])

for team in teams:
    print(team) # Python listeyi baştan sona geziyor. Her turda bir elemanı alıp team değişkenine koyuyor, sonra girintili satırı çalıştırıyor. Dört eleman varsa dört tur döner.


for team in league:
    print(team["name"])

    print(team["name"] ,team["points"])         # print içinde virgülle birden fazla şey yazdırabilirsin, aralarına boşluk koyar.

points = 42 

if points > 42:
    print("leader")

else:
    print("not leader")


points = 15

if points > 40:
    print("leader")
elif points > 20:
    print("mid-table")
else:
    print("drop zone")


if team_info["name"] == "Galatasaray":   # Metin karşılaştırmasında da == kullanılır, büyük/küçük harf duyarlıdır.
    print("this is my team")


def greet():
    print("hello") 

greet()  # def bloğu sadece tanımlar, çalıştırmaz. Tarif yazmak gibi, yemek pişmez. Alttaki greet() satırı onu çağırır, işte o zaman çalışır.


# Parametre — dışarıdan veri alma
def greet_team(name):
    print("hello" + name)

greet_team("Galatasaray")     #name bir parametre — fonksiyonun içinde kullanılan geçici bir isim

# Return — sonuç geri verme
def get_status(points):
    if points > 40:
        return "leader"
    elif points > 20:
        return "mid-table"
    else:
        return "drop-zone"

result = get_status(42)
print(result)         # Bir detay: return çalıştığı anda fonksiyon biter. Altındaki satırlara bakılmaz.

# print ekrana yazar, return değeri geri verir. print edilen şeyi saklayamazsın, return edilen şeyi bir değişkene koyabilirsin, başka bir fonksiyona verebilirsin, listeye ekleyebilirsin.
# FastAPI'da yazacağın her endpoint bir fonksiyon olacak ve return ile veri döndürecek. print ile değil.


for team in league : 
    status = get_status(team["points"])
    print(team["name"], status)

