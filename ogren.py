club = "Besiktas"
point = 15 
ratio = 3.45 
is_champion = False


teams = ["Galatasaray", "Fenerbahce", "Besiktas"]
teams[0]
teams.append("Trabzonspor")
len(teams)
print(teams)

teams1 = [
    {"name": "Kasimpasa","point": 35},
    {"name" :"Alanya", "point":39}
]

if point > 40: 
    print("Leader")

elif point > 20 :
    print("mid-table")
else: 
    print("drop zone")



for club in teams:
    print(club["name"])


def point_stats (point):
    if point > 40:
        return "leader"
    return "mid-table"

result = point_stats(17)

print( result)