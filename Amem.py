import json
import random
from googletrans import Translator
import goslate


linguas = open('Txt/linguas.json', encoding="utf8")
lingua = json.load(linguas)
tam = len(lingua)

gs = goslate.Goslate()
ale = random.randint(1,tam)

biblia = open('Txt/bible.txt','r')
versiculos = biblia.read().split('\n\n')
num = random.randint(1,versiculos.__len__())
print("====================================================================")
print(versiculos[num])
print("====================================================================")
