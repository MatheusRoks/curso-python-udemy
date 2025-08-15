from clear import clear_terminal
import random




execice = [
    {
        "question": "Qual é o resultado da expressão 2 + 3 * 4?",
        "options": ['20', '14', '26', '10'],
        "answer": 14,
        "explanation": "A expressão é avaliada seguindo a ordem das operações, onde a multiplicação é realizada antes da adição. Portanto, 3 * 4 = 12 e 2 + 12 = 14.",
    },
    {
        "question": "Qual é o resultado da expressão (5 + 3) * 2?",
        "options": ['16', '10', '8', '12'],
        "answer": 16,
        "explanation": "A expressão entre parênteses é avaliada primeiro. Assim, 5 + 3 = 8 e, em seguida, 8 * 2 = 16.",
    },
    {
        "question": "Qual é o resultado da expressão 10 - 2 * 3?",
        "options": ['4', '6', '8', '2'],
        "answer": 4,
        "explanation": "A multiplicação é realizada antes da subtração. Portanto, 2 * 3 = 6 e 10 - 6 = 4.",
    },
]

def run_quiz():
    clear_terminal()
    print("Bem-vindo ao Quiz de Python!")
    score = 0   
    random.shuffle(execice)
    for question_data in execice:
        print("\n" + question_data['question'])

        random.shuffle(question_data['options'])
        i = 0
        for option in question_data['options']:
            i+=1
            print(f'{i}) {option}')

        answer_input = input("\nDigite a resposta: ")
        try:
            answer = int(answer_input)

        except ValueError:
            print("Entrada inválida. Digite apenas números.")

        if answer == question_data['answer']:
            print("Resposta correta!")
            score += 1000
        else:
            print("Resposta incorreta.")
            
        print("\nExplicação:")
        print(question_data["explanation"])
        
        input("\nAperte Enter para continuar...")
        clear_terminal()
        print('Bem-vindo ao Quiz de Python!')
        
    clear_terminal()
    print("Quiz concluído!")
    print(f'Parabéns, sua pontuação final é: {score}')
    print("Obrigado por jogar!")

run_quiz()