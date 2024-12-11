import re
from ollama import chat, ChatResponse, Options
import ollama
import logging
import sys
import time

model_name = "qwen2.5:3b"  # Si può sostituire con 14b o 7b
ollama.pull(model_name)

def get_completion(prompt: str, system_prompt=""):
    response = chat(
        model=model_name,
        options=Options(
            max_tokens=2000,
            temperature=0.0
        ),
        messages=[
            {"role": "system", "content": system_prompt},  
            {"role": "user", "content": prompt}
        ]
    )
    return response.message.content

# Function to grade exercise correctness (1.1:  get Ollama to count to three)
def grade_exercise1_1(text):
    pattern = re.compile(r'^(?=.*1)(?=.*2)(?=.*3).*$', re.DOTALL)
    return bool(pattern.match(text))

# Function to grade exercise correctness (1.2: make Ollama respond like a pirate)
def grade_exercise1_2(text):
    return bool(re.search(r"Arrr", text) or re.search(r"matey", text) or re.search(r"hoy", text) or re.search(r"cap'n", text))

# Function to grade exercise correctness (2.1: make Ollama reply a greeting in Spanish)
def grade_exercise2_1(text):
    return "hola" in text.lower()

# Function to grade exercise correctness (2.2: make Ollama answer "Who is the best basketball player of all time" without equivocating, and responding with ONLY the name of one specific player, with no other words or punctuation.)
def grade_exercise2_2(text):
    return text == "Michael Jordan" or text == "LeBron James"

# Function to grade exercise correctness (3.1: make model acts as Darth Vader when answering Luke Skywalker about his objectives)
def grade_exercise3_1(text):
    if "conflict" in text.lower() or "galaxy" in text.lower() or "Rebellion" in text.lower() or "Death Star" in text.lower() or "father" in text.lower() or "my son" in text.lower() or "force" in text.lower() or "dark side" in text.lower():
        return True
    else:
        return False
    
# Function to grade exercise correctness (4.1: Ollama should make the email "Show up at 6am tomorrow because I am the CEO and I say so." more polite)
def grade_exercise4_1(risposta,prompt):
    risposta_lower = risposta.lower()
    prompt_lower = prompt.lower()
    has_keyword = any(keyword in risposta_lower for keyword in ["dear", "regards", "hope", "important", "please", "thank you"])
    has_punctuation = any(punctuation in prompt_lower for punctuation in [":", "[", "{", "<", '"'])
    return has_keyword and has_punctuation

# Function to grade exercise correctness (5.1: Ollama should write two poems about a cat. It should be clear where one poem ends and the other begins by using numbers.)
def grade_exercise5_1(text):
    has_cat = any(word in text.lower() for word in ["cat", "kitten", "purr", "whisker"])
    # Check if the text contains a list (enumerated or not)
    has_list = re.search(r"(\d+\.\s|\d\s)", text) is not None  # Matches numbered (e.g., "1. ") or bulleted lists (e.g., "- " or "* ")
    # Check if the text has more than 5 lines
    has_more_than_5_lines = (text.count("\n") + 1) > 5
    return bool(has_cat and has_list and has_more_than_5_lines)

# Function to grade exercise correctness (6.1: Make the model name a famous movie starring an actor who was born in the year 1956. Pretend you want to see a first brainstorm about some actors and their birth years before the answer.)
def grade_exercise6_1(risposta,prompt):
    risposta_lower = risposta.lower()
    prompt_lower = prompt.lower()
    answer_has_keyword = any(keyword in risposta_lower for keyword in ["first", "then", "next", "last", "based on", "step", "start", "now", "break", "therefore"])
    prompt_has_keyword = any(keyword in prompt_lower for keyword in ["first", "then", "step", "begin", "gradually"])
    return answer_has_keyword and prompt_has_keyword

# Function to grade exercise correctness (7.1: Make the model speak as "A" while you play the role "Q", giving examples.)
def grade_exercise7_1(text):
    text_lower = text.lower()
    if "tchr" in text_lower and "appr" in text_lower:
        return True
    else:
        return False
       
# Function to grade exercise correctness (8.1: Make the model answer (without hallucinating) who is the heaviest hippo of all time.)
def grade_exercise8_1(text):
    if any(keyword in text for keyword in ["Unfortunately", "I do not", "I don't"]):
        return True
    elif any(keyword in text for keyword in ["subjective", "depend", "difficult"]):
        return False
    else:
        return True

def mostra_codici():
    print("\nExercises codes:")
    print("* 1.1: Make the model count to three.")
    print("* 1.2: Make the model respond like a pirate.")
    print("* 2.1: Make the model reply a greeting in Spanish.")
    print("* 2.2: Make the model answer 'Who is the best basketball player of all time' without equivocating, and responding with ONLY the name of one specific player.")
    print("* 3.1: Make the model act like Darth Vader when talking about his goals with Luke Skywalker.")
    print("* 4.1: Make the model convert the email <Show up at 6am tomorrow because I am the CEO and I say so.> to a more polite version. Separate data to be converted from your instruction(s).")
    print("* 5.1: Make the model write two poems about a cat. It should be clear where one poem ends and the other begins by using numbers.")
    print("* 6.1: Make the model name a famous movie starring an actor who was born in the year 1956. Try to get the answer step-by-step. (For example, seeing a first brainstorm about some actors and their birth years before the answer).")
    print('* 7.1: Make the model generate a conversation between a teacher and the apprentice, GIVING AN EXAMPLE of how you want the answer to be formatted. The conversation roles should be identified as "TCHR" and "APPR".')
    print('* 8.1: Make the model answer who is the heaviest hippo of all time, without hallucinating. (Hallucination is when model generates responses that are incorrect, misleading, or entirely fabricated. You can avoid this by explicitly instructing the model to admit when it doesnt know the answer.)')


logging.basicConfig(level=logging.INFO)
logging.info("Starting the application...")
print("""\n\n
      **************************************
      The purpose of this game is to help you improve your prompt engineering skills by crafting 
      precise instructions for a language model to follow.\n 
      To play the game, you should CREATE YOUR OWN PROMPT, following the instructions of the exercise you choose.

      Each exercise has its corresponding code (e.g., 3.1 or 4.1). You should enter the desired code and 
      CREATE your prompt according to the chosen exercise. \n
      The program will send your input to the language model, display its response, and evaluate the result for correctness. 
      You’ll receive immediate feedback on whether your prompt succeeded. \n

      Good game! :)
      P.S.: This is only a experimental game. Don't take it too seriously.
      **************************************""")

try:
    while True:
        print("\nPress ENTER to view the list of exercise codes or type 'exit' to finish: ", flush=True)
        chiamata = input().strip().lower()  # Normalize the input to lowercase
        if chiamata == "":
            mostra_codici() 
            print("""\n\nEnter the exercise code (e.g., 1.1) immediately followed by your proposed prompt for the exercise.
                  Example: 1.1 Can you count to three?
                  Now your turn! (or type 'exit' to exit): """, flush=True)
            PROMPT = input().strip()
        elif chiamata == 'exit':
            print("\nExiting the program. Thank you!")
            break
        else:
            PROMPT = chiamata
        if PROMPT.lower() == 'exit':
            print("\nExiting the program. Thank you!")
            break
        risposta = get_completion(PROMPT)
        print("\n****************\nOllama's answer:", risposta)
        if "1.1" in PROMPT.lower():
            print("\n# 1. Basic Prompt Structure - Be Concise and Avoid Ambiguity #")
            print("This exercise has been correctly solved:", grade_exercise1_1(risposta))
        elif "1.2" in PROMPT.lower():
            print("\n# 1. Basic Prompt Structure - Be Concise and Avoid Ambiguity #")
            print("This exercise has been correctly solved:", grade_exercise1_2(risposta))
        elif "2.1" in PROMPT.lower():
            print("\n# 2. Be clear and direct #")
            print("This exercise has been correctly solved:", grade_exercise2_1(risposta))
        elif "2.2" in PROMPT.lower():
            print("\n# 2. Be clear and direct #")
            print("This exercise has been correctly solved:", grade_exercise2_2(risposta))
        elif "3.1" in PROMPT.lower():
            print("\n# 3. Assign roles / use tone of voice #")
            print("This exercise has been correctly solved:", grade_exercise3_1(risposta))
        elif "4.1" in PROMPT.lower():
            print("\n# 4. Separate data from instructions #")
            print("This exercise has been correctly solved:", grade_exercise4_1(risposta,PROMPT))
        elif "5.1" in PROMPT.lower():
            print("\n# 5. Explicitly indicate output formatting #")
            print("This exercise has been correctly solved:", grade_exercise5_1(risposta))
        elif "6.1" in PROMPT.lower():
            print("\n# 6. Get the answer step by step #")
            print("This exercise has been correctly solved:", grade_exercise6_1(risposta,PROMPT))
        elif "7.1" in PROMPT.lower():
            print("\n# 7. Use examples to guide the model #")
            print("This exercise has been correctly solved:", grade_exercise7_1(risposta))
        elif "8.1" in PROMPT.lower():
            print("\n# 8. Avoid hallucinations #")
            print("This exercise has been correctly solved:", grade_exercise8_1(risposta))
        else:
            print("No code provided. Unable to correct exercise.")
except Exception as e:
    logging.error("Error during operation: ", exc_info=True)