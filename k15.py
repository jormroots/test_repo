import random

class flashcards:
    def __init__(self):
        
        self.cards={
        'Kui palju ülesandeid oli andtud?':'15',
        'Mitu punkti oli võimalik saada kokku?':'37',
        'Lõputöö annab mitu punkti.':'7',
        'Ülessanded annavad kokku ... punkte(number).': '30',
        'Õppilased osalevad Cleveroni Akadeemia ... lennus.': 'teises',
        'Õppimine kestad mitu aastat?(number).':'3',
        'Esimene tund oli RT-...(number).':'012',
        'Mis linnas õppimine toimub.':'Viljandi',
        'Mis RT-s on kõige rohkem õpetajaid?':'037',
        'MItu õpilast valiti(number)?':'20'}


print("RT-012 quiz")
fc=flashcards()
fc.quiz()