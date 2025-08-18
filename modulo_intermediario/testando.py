################ATENÇÃO################
#Esse arquivo é um arquivo de teste, não foi criado por mim em sua completude.
# criei parte da lógica e o restante foi gerado por uma IA.
#para ver o código original, acesse:
#o github mini-quiz. lá estará meu codigo original e sem ia envolvida.


import tkinter as tk
from tkinter import messagebox
import random

# Global variables to manage the quiz state
score = 0
current_question_index = 0
questions_list = []
correct_answers = 0
quantity = 0

def generate_question(difficulty):
    """
    Generates a new random mathematical expression and its result based on the difficulty.
    
    Args:
        difficulty (str): The difficulty level ('1' for easy, '2' for medium, '3' for difficult).

    Returns:
        tuple: A tuple containing the question string and the numerical result.
    """
    operators = ['+', '-', '*', '/']
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    number3 = random.randint(1, 10)
    op1 = random.choice(operators)
    op2 = random.choice(operators)
    
    if difficulty == '1':
        question_string = f"{number1} {op1} {number2}"
    elif difficulty == '2':
        question_string = f"{number1} {op1} {number2} {op2} {number3}"
    else:  # Difficulty '3'
        question_string = random.choice([
            f"{-number1} {op1} ({number2} {op2} {number3})",
            f"{number1} {op1} ({-number2} {op2} {number3})",
            f"{number1} {op1} ({number2} {op2} {-number3})",
            f"{number1} {op1} ({number2} {op2} {number3})",
            f"({number1} {op1} {number2}) {op2} {number3}",
            f"({-number1} {op1} {number2}) {op2} {number3}",
            f"({number1} {op1} {-number2}) {op2} {number3}",
            f"({number1} {op1} {number2}) {op2} {-number3}",
            f"{-number1} {op1} {number2} {op2} {number3}",
            f"{number1} {op1} {-number2} {op2} {number3}",
            f"{number1} {op1} {number2} {op2} {-number3}",
 
        ])
    
    try:
        result = eval(question_string)
        if isinstance(result, float):
            result = round(result, 2)
    except ZeroDivisionError:
        return generate_question(difficulty)
    
    return (question_string, result)

def create_question_data(difficulty):
    """
    Creates a complete dictionary for a single quiz question, with shuffled answer options.
    
    Args:
        difficulty (str): The difficulty level for the question.

    Returns:
        dict: The dictionary of question data.
    """
    question_text, correct_answer = generate_question(difficulty)
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

def start_quiz(difficulty, num_questions_str):
    """
    Initializes the quiz and the main window.
    """
    global questions_list, current_question_index, score, quantity, correct_answers
    
    try:
        quantity = int(num_questions_str)
        if quantity <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Erro de Entrada", "Número de perguntas inválido. Usando 5 por padrão.")
        quantity = 5

    # Reset quiz state
    score = 0
    correct_answers = 0
    current_question_index = 0
    questions_list = [create_question_data(difficulty) for _ in range(quantity)]
    random.shuffle(questions_list)

    # Hide start frame and show quiz frame
    start_frame.pack_forget()
    quiz_frame.pack()

    display_question()
    
def display_question():
    """
    Displays the current question and its options on the GUI.
    """
    global questions_list, current_question_index
    if current_question_index < len(questions_list):
        question_data = questions_list[current_question_index]
        question_label.config(text=f'Pergunta {current_question_index + 1} de {quantity}:\n{question_data["question"]}')
        
        for i, option in enumerate(question_data["options"]):
            option_buttons[i].config(text=option, state=tk.NORMAL)
            
        feedback_label.config(text="")
        score_label.config(text=f'Pontuação: {score}')
        
        # Enable all buttons for the new question
        for btn in option_buttons:
            btn.config(state=tk.NORMAL)
    else:
        show_final_results()

def check_answer(user_answer_value):
    """
    Checks the user's answer, updates the score, and displays feedback.
    """
    global score, current_question_index, correct_answers
    question_data = questions_list[current_question_index]
    
    # Disable all buttons after an answer is selected
    for btn in option_buttons:
        btn.config(state=tk.DISABLED)

    if user_answer_value == question_data['answer']:
        feedback_label.config(text="Correto!", fg="green")
        correct_answers += 1
        if difficulty_var.get() == '1':
            score += 100
        elif difficulty_var.get() == '2':
            score += 500
        else:
            score += 1000
    else:
        feedback_label.config(text=f"Incorreto. A resposta correta era {question_data['answer']}.", fg="red")

    score_label.config(text=f'Pontuação: {score}')
    window.after(1500, next_question) # Wait 1.5 seconds before moving to next question

def next_question():
    """
    Moves to the next question in the list.
    """
    global current_question_index
    current_question_index += 1
    display_question()

def show_final_results():
    """
    Displays the final results of the quiz.
    """
    quiz_frame.pack_forget()
    results_frame.pack()
    
    total_questions = len(questions_list)
    if total_questions > 0:
        percentage_correct = (correct_answers / total_questions) * 100
    else:
        percentage_correct = 0

    results_label.config(text="Quiz Concluído!")
    final_score_label.config(text=f'Sua pontuação final é: {score}')
    correct_answers_label.config(text=f'Você acertou {correct_answers} de {total_questions} perguntas ({percentage_correct:.2f}%).')

def reset_quiz():
    """
    Resets the quiz to the start screen.
    """
    results_frame.pack_forget()
    start_frame.pack()

# Create the main window
window = tk.Tk()
window.title("Quiz de Matemática")
window.geometry("500x400")
window.resizable(False, False)

# --- Start Screen widgets ---
start_frame = tk.Frame(window, padx=20, pady=20)
start_frame.pack()

tk.Label(start_frame, text="Bem-vindo ao Quiz de Matemática!", font=('Arial', 14)).pack(pady=10)
tk.Label(start_frame, text="Escolha a dificuldade e a quantidade de perguntas:").pack()

# Difficulty selection
difficulty_var = tk.StringVar(value='1')
difficulty_frame = tk.Frame(start_frame)
difficulty_frame.pack(pady=5)
tk.Radiobutton(difficulty_frame, text="Fácil", variable=difficulty_var, value='1').pack(side=tk.LEFT)
tk.Radiobutton(difficulty_frame, text="Médio", variable=difficulty_var, value='2').pack(side=tk.LEFT)
tk.Radiobutton(difficulty_frame, text="Difícil", variable=difficulty_var, value='3').pack(side=tk.LEFT)

# Number of questions
num_questions_label = tk.Label(start_frame, text="Número de perguntas:")
num_questions_label.pack()
num_questions_entry = tk.Entry(start_frame)
num_questions_entry.insert(0, "5") # Default value
num_questions_entry.pack()

# Start button
start_button = tk.Button(start_frame, text="Começar Quiz", command=lambda: start_quiz(difficulty_var.get(), num_questions_entry.get()))
start_button.pack(pady=10)

# --- Quiz Screen widgets ---
quiz_frame = tk.Frame(window, padx=20, pady=20)

score_label = tk.Label(quiz_frame, text="", font=('Arial', 12))
score_label.pack()

question_label = tk.Label(quiz_frame, text="", font=('Arial', 12), wraplength=450)
question_label.pack(pady=20)

options_frame = tk.Frame(quiz_frame)
options_frame.pack()
option_buttons = [tk.Button(options_frame, text="", width=15, command=lambda i=i: check_answer(questions_list[current_question_index]["options"][i])) for i in range(4)]
for btn in option_buttons:
    btn.pack(side=tk.LEFT, padx=5, pady=5)

feedback_label = tk.Label(quiz_frame, text="", font=('Arial', 12, 'bold'))
feedback_label.pack(pady=10)

# --- Results Screen widgets ---
results_frame = tk.Frame(window, padx=20, pady=20)
results_label = tk.Label(results_frame, text="Quiz Concluído!", font=('Arial', 14, 'bold'))
results_label.pack(pady=10)
final_score_label = tk.Label(results_frame, text="", font=('Arial', 12))
final_score_label.pack()
correct_answers_label = tk.Label(results_frame, text="", font=('Arial', 12))
correct_answers_label.pack()
play_again_button = tk.Button(results_frame, text="Jogar Novamente", command=reset_quiz)
play_again_button.pack(pady=10)

# Start the main event loop
window.mainloop()

