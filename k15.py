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
    
    def quiz(self):
        flag = False
        user_answer = ''
        if(flag == False or flag == True):
            question, answer = random.choice(list(self.cards.items()))
            while(user_answer != 'exit' and flag == False or flag == True):
                if(user_answer != 'exit' and flag == False):
                    last_question = question
                    last_answer = answer
                    print("  ")
                    row = len(question)
                    h = ''.join(['+'] + ['-' *row] + ['+'])
                    result = h + '\n'"|"+question+"|"'\n' + h
                    print(result)

                    print('turn = flip to answer side, exit = exits the program')
                    print('')
                    print(answer)
                    print('Sisesta vastus: ')
                    user_answer = input()
                else:
                    print("  ")
                    row = len(answer)
                    h = ''.join(['+'] + ['-' *row] + ['+'])
                    result = h + '\n'"|"+answer+"|"'\n' + h
                    print(result)

                    print('turn = flip to question side, exit = exits the program')
                    print('')
                    print('Sisesta vastus: ')
                    user_answer = input()
             
                if(user_answer.lower() == answer.lower() or user_answer.upper() == answer.upper() or user_answer == answer):
                    print("  ")
                    print("Correct answer")
                    print("  ")
                    flag = False
                    question, answer = random.choice(list(self.cards.items()))
                    if(last_question == question and last_answer == answer):
                        question, answer = random.choice(list(self.cards.items()))
                elif(user_answer == 'exit'):
                    return 0
                elif(user_answer == 'turn' and flag == False):
                    flag = True
                elif(user_answer == 'turn' and flag == True):
                    flag = False
                else:
                    print("  ")
                    print("Wrong answer")
                    print("  ")
        else:
            return 0

print("RT-012 quiz")
fc=flashcards()
fc.quiz()