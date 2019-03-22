classList = ["AMOURA Louis",

		      "AUBINEAU Charles",

			    "BAUDOIN Matthias",

			    "BLANC Thomas",

			    "CAMACHO Jean-Baptiste",

			    "COLA Raphael",

			    "DETOLLE Thomas",

			    "FOURMOND Mael",

			    "FUSTER Alexandre",

			    "GOSSEZ Eliott",

			    "GOURRAT Bastien",

			    "MARROC Olivier",

			    "MONNET Luc",

			    "NATHIER Tom",

			    "PRALON Olivier",

			    "ROSENACKER Nathan",

			    "SAINT-AURET Sylvain",

			    "TAMBURI Tom",

			    "VALLERY Alexandre",

			    "VALLON Maxence",

			    "VEBER Charles",

			    "VEISSID Tom",

			    "WEISS Julien",

			    "WILD Luc"]

import random
def randomGroupGenerator(classList, groupSize):
  x,y,Listfin=1,0,[]
  random.shuffle(classList)
  while len(Listfin) != int(len(classList)/groupSize)+1:
    if groupSize*x>len(classList):
      Listfin.append(classList[groupSize*y:])
    else:
      Listfin.append(classList[groupSize*y:groupSize*x])
    x+=1
    y+=1
  return Listfin
  
print(randomGroupGenerator(classList, 3))