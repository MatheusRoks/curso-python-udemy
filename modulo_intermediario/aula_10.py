from clear import clear_terminal
import random


def generate_question():
    operators = ['+', '-', '*', '/']
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    number3 = random.randint(1, 10)
    op1 = random.choice(operators)
    op2 = random.choice(operators)
    
    question_string = f"{number1} {op1} {number2} {op2} {number3}"
    
    try:
        result = eval(question_string)
        if isinstance(result, float):
            result = round(result, 2)
    except ZeroDivisionError:
        return generate_question()
    
    return (question_string, result)

def create_question_data():
    question_text, correct_answer = generate_question()
    options = [correct_answer]
    while len(options) < 4:
        distractor = correct_answer + random.randint(-5, 5)
        if distractor != correct_answer and distractor not in options:
            options.append(distractor)

    random.shuffle(options)
    
    return {
        "question": f'Qual é o resultado da expressão {question_text}?',
        "options": options,
        "answer": correct_answer,
        "explanation": f"A expressão é avaliada seguindo a ordem das operações. Portanto, o resultado é {correct_answer}.",
    }

def run_quiz():
    clear_terminal()
    print("Bem-vindo ao Quiz de Python!")
    print("Vamos ver quantas perguntas você acerta!")
    score = 0
    quantity = input("Quantas perguntas você gostaria de responder? (Digite um número): ")
    try:
        quantity = int(quantity)
        if quantity <= 0:
            raise ValueError("O número deve ser maior que zero.")
    except ValueError as e:
        print(f"Entrada inválida: {e}. Usando 5 perguntas por padrão.")
        quantity = 5


    input("Aperte Enter para começar...")

    exercice = [create_question_data() for _ in range(quantity)]

    random.shuffle(exercice)
    
    for question_data in exercice:
        clear_terminal()
        print("\n" + question_data['question'])

        for i, option in enumerate(question_data['options'], 1):
            print(f'{i}) {option}')

        user_answer_value = None
        
        while True:
            answer_input = input("\nDigite o número da resposta: ")
            try:
                answer_index = int(answer_input)
                if 1 <= answer_index <= len(question_data['options']):
                    user_answer_value = question_data['options'][answer_index - 1]
                    break 
                else:
                    print(f"Por favor, digite um número entre 1 e 4.")
            except ValueError:
                print("Entrada inválida. Por favor, digite apenas números.")
            

        if user_answer_value == question_data['answer']:
            print("Resposta correta!")
            score += 1000
        else:
            print("Resposta incorreta.")
            
        print("\nExplicação:")
        print(question_data["explanation"])
        
        input("\nAperte Enter para continuar...")
        
    clear_terminal()
    print("Quiz concluído!")
    print(f'Parabéns, sua pontuação final é: {score}')
    print("Obrigado por jogar!")

if __name__ == "__main__":
    run_quiz()
