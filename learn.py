"""
    Latihan
"""

player1 = {"name":"songoku", "power":100}
player2 = {"name":"trunks", "power":250}

def train(player):
  player['power'] += 100
  
def deffence(player):
  player['power'] += 50
  
  
def attack(attacker, defender):
  if(attacker['power'] > defender['power']
     print('serangan berhasil! selamat untuk', attacker['name'])
  else:
     print('serangan gagal! kamu lemah', attacker['name'])
     
train(player1)
train(player1)
deffence(player2)     
attack(player1, player2)
     
