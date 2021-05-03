class Player:
    def __init__(self,name,countries,age,countryfrom):
        self.name = name
        self.countries = countries
        self.age = age 
        self.countryfrom = countryfrom


def countPlayers(players,country_name):
    count = 0
    for player in players:
        if player.countryfrom == country_name:
            count += 1
    return count

def getPlayerPlayedForMaxCountry(players):
    players = sorted(players,key=lambda x:len(x.countries))
    return players[-1].name

n=int(input())
p_list=[]
for i in range(n):
    kp=[]
    name=input()
    k=int(input())
    for j in range(k):
        kp.append(input())
    age=int(input())
    country=input()
    p_list.append(Player(name,kp,age,country))
icountry=input()
print(countPlayers(p_list,icountry))
print(getPlayerPlayedForMaxCountry(p_list))