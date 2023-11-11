
import random

sdgs = {
    1: {"title": "No Poverty",
        "description": "Eliminate poverty everywhere. Ensure that everyone has access to the things they need for a better life, such as food, healthcare, education, and equality."},
    4: {"title": "Quality Education",
        "description": "Make sure everyone gets a great education regardless of identity. This means offering equal, inclusive, high-quality education so that everyone has an equal opportunity to learn and develop."},
    13: {"title": "Climate Action",
         "description": "Take urgent action to combat climate change and its impacts. To preserve our planet and guarantee a sustainable future for everybody."},
    16: {"title": "Peace, Justice, and Strong Institutions",
         "description": "Focus on inclusive and peaceful societies. Promote unity, diversity, and adaptability to create communities where all members can prosper."},
    3: {"title": "Good Health and Well-being",
        "description": "Ensure that everyone, regardless of age, is happy and healthy. Prioritize preventing health problems, offering easily accessible healthcare, and fostering everyone's general well-being."},
}
score = 0

questions = {
    "easy": [
        {
            "question": "Easy Question: What is the primary focus of SDG {sdg}?",
            "options": {
                "A": "No Poverty",
                "B": "Quality Education",
                "C": "Climate Action",
                "D": "Good Health and Well-being",
            },
            "correct_answer": "A"
        },
        {
            "question": "Easy Question: Which of the following is a key goal of SDG {sdg}?",
            "options": {
                "A": "Ending poverty",
                "B": "Ensuring clean water",
                "C": "Reducing inequality",
                "D": "Promoting peace",
            },
            "correct_answer": "A"
        },

    ],
    "intermediate": [
        {
            "question": "Intermediate Question: What is one of the specific targets of SDG {sdg}?",
            "options": {
                "A": "Eradicating extreme poverty",
                "B": "Ensuring clean water and sanitation",
                "C": "Promoting gender equality",
                "D": "Combating climate change",
            },
            "correct_answer": "C"
        },
        {
            "question": "Intermediate Question: Which international organization is closely associated with SDG {sdg}?",
            "options": {
                "A": "UNESCO",
                "B": "WHO",
                "C": "UNICEF",
                "D": "UNDP",
            },
            "correct_answer": "D"
        },

    ],
    "difficult": [
        {
            "question": "Difficult Question: What is the timeline for achieving SDG {sdg}?",
            "options": {
                "A": "2030",
                "B": "2050",
                "C": "2100",
                "D": "Unspecified",
            },
            "correct_answer": "A"
        },
        {
            "question": "Difficult Question: What is the primary indicator used to measure progress for SDG {sdg}?",
            "options": {
                "A": "GDP per capita",
                "B": "Life expectancy",
                "C": "HDI (Human Development Index)",
                "D": "Poverty headcount ratio",
            },
            "correct_answer": "D"
        },

    ]
}


def display_sdg_info(sdg):
    print(f"Let's talk about SDG {sdg}: {sdgs[sdg]['title']}")


def ask_question(question, options, correct_answer):
    global score
    print(question)
    for option, text in options.items():
        print(f"{option}. {text}")
    user_answer = input("Select the correct option (A, B, C, or D): ").upper()

    if user_answer == correct_answer:
        print("Correct! You earn 5 points.")
        score += 5
    else:
        print(f"Sorry, that's incorrect. The correct answer is: {correct_answer}")

def provide_sdg_info(sdg):
    display_sdg_info(sdg)
    more_info = input("Would you like to learn more about this SDG? (yes/no): ").lower()
    if more_info == "yes" or more_info == "y":
        print(sdgs[sdg]['description'])
        input("Once you finished reading please press enter.")
    else:
        return


def sdg_quiz():
    print("Welcome to the best SDG quiz bot ever made!")

    print("Please, inform me of your name.")
    name = input('Enter Here: ')
    print(f"Hello, {name}! Let's get started.")

    while True:
        print("Please select an SDG to learn about:")
        for sdg in sdgs:
            print(f"{sdg}. {sdgs[sdg]['title']}")

        sdg_choice = input("Enter the number corresponding to your choice: ")
        if sdg_choice.isdigit() and int(sdg_choice) in sdgs:
            selected_sdg = int(sdg_choice)
            break
        else:
            print("Invalid choice. Please enter the number corresponding to your choice.")

    provide_sdg_info(selected_sdg)

    while True:
        print("Please choose your prefered level of difficulty.")
        print("1. Easy")
        print("2. Intermediate")
        print("3. Difficult")
        print("Enter the number corresponding to your choice: ")
        dif_choice = input(': ')
        if dif_choice.isdigit() and int(dif_choice) in [1, 2, 3]:
            d = int(dif_choice)
            break
        else:
            print("You have selected a number that is not 1, 2, 3. Please pick one of those relative to your prefered difficulty")
    questions_for_level = questions["easy"]
    if d == 2:
        questions_for_level = questions["intermediate"]
    elif d == 3:
        questions_for_level = questions["difficult"]

    for question_data in questions_for_level:
        question = question_data["question"].replace("{sdg}", str(selected_sdg))
        opt = question_data["options"]
        correct_answer = question_data["correct_answer"]

        ask_question(question, opt, correct_answer)

    print(f"Congratulations, {name}! Your score is {score}/15.")
    if score >= 15:
        print("You've successfully completed the challenge! You're a Sustainable Development Goal master!")
    elif score >= 10:
        print("Congratulations! You passed! Keep learning the SDGs to improve your score and become the SDG Master!")
    else:
        print("Looks like you did not pass. Learn more about the SDGs to improve your score!")


def main():
    sdg_quiz()


if __name__ == "__main__":
    main()