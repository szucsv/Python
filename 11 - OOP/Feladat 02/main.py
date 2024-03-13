from edzes import Mell
from edzes2 import Hat
from edzes3 import Kar

hetfo:Mell = Mell()
hetfo.First = "Bench press"
hetfo.Second = "Döntött pados bench press"
hetfo.Third = "Tárogatás"
hetfo.Fourth = "Tricepsz"

szerda: Hat = Hat()
szerda.First = "lehuzas"
szerda.Second = "Bicepsz egyenes ruddal"
szerda.Third = "Kalapacs bicepsz"
szerda.Fourth = "Evezes"

pentek: Kar = Kar()
pentek.First = "Bicepsz egyenes rúddal"
pentek.Second = "Bicepsz egykezes súlyokkal"
pentek.Third = "tricepsz"
pentek.Fourth = "Váll"

print(f"Kedd:\n{hetfo.First}\n{hetfo.Second}\n{hetfo.Third}\n{hetfo.Fourth}\n\nSzerda:\n{szerda.First}\n{szerda.Second}\n{szerda.Third}\n{szerda.Fourth}\n{szerda.Fifth}\n\nCsütörtök:\n{pentek.First}\n{pentek.Second}\n{pentek.Third}\n{pentek.Fourth}")