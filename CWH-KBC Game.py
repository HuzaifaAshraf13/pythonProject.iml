def ask_question(question, answer, prize_money):
    user_response = input(question + " ")
    if user_response.lower() == answer.lower():
        print("Moj karadi Beta! You earned {} RS. 1000".format(prize_money))
        return True
    else:
        print("Beta tum se na huga ! The correct answer was: {}".format(answer))
        return False

if __name__ == "__main__":
    print("Welcome to the Kya Bana ga Cororpati!")
    print("Answer each question correctly to win prize money.\n")
    print("Be honest, and no cheating!\n")
    questions_and_answers = [
        ("Q1: What were the two major superpowers during the Cold War?", "US and Soviet Union", 1000),
        ("Q2: What was the capital of Poland during the Cold War?", "Warsaw", 1000),
        ("Q3: Which famous speech started with 'I have a dream'?", "Martin Luther King Jr.'s speech", 1000),
        ("Q4: What is the largest planet in our solar system?", "Jupiter", 1000),
    ]

    total_prize_money = 0

    for question, answer, prize_money in questions_and_answers:
        if ask_question(question, answer, prize_money):
            total_prize_money += prize_money

    print("\nYou earned a total of {} RS.".format(total_prize_money))


