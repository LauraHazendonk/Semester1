import os
import re

print("##########################################")
print("#      A       t         PPP  DDD  FFFFF #")
print("#     AA       t         P  P D  D   F   #")
print("#    A A       ttt   oo  P  P D  D   F   #")
print("#   AAAA u  u  t    o  o PPP  D  D   FFF #")
print("#  A   A u  u  t    o  o P    D  D   F   #")
print("# A    A  uuuu  ttt  oo  P    DDD    F   #")
print("##########################################")
print()

pfad = os.getcwd()
login = os.getlogin() # liest Nutzername aus.

print("Hallo",login+"!!!")
print("Suche Bilder im akuellen Ordner (" + pfad + ") ...")
dir = os.listdir()
bilder = list(filter(lambda x: re.match(r".*jpg",x.lower()), dir))

print("Erstelle TEX-Datei...")

dateiInhalt = """
"""