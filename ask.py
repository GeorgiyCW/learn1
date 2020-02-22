ask_answer_dict = {"Wie gehts?": "Gut!", "Was machst du?": "Ich programmiere"} 

def ask_user(ask_answer_dict):
    while True:
        try:
            answer = input('Stellen Sie eine Frage:\n')
            print(ask_answer_dict.get(answer, 'Verstehe nicht'))
        except KeyboardInterrupt:
            print('Tschüss!')
            break

ask_user(ask_answer_dict)
