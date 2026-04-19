import random
import winsound

# Sound functions
def correct_sound():
    # Trumpet-like sound
    winsound.Beep(880, 200)
    winsound.Beep(988, 200)
    winsound.Beep(1047, 300)

def incorrect_sound():
    # Buzzer sound
    winsound.Beep(200, 500)

# Trivia questions
questions = [
    {
        "question": "Which country won the FIFA World Cup in 2018?",
        "answer": "France"
    },
    {
        "question": "How many players are on a basketball court per team?",
        "answer": "5"
    },
    {
        "question": "Who holds the record for the most home runs in MLB history?",
        "answer": "Barry Bonds"
    },
    {
        "question": "In tennis, what is the term for a score of zero?",
        "answer": "Love"
    },
    {
        "question": "Which NFL team has won the most Super Bowls?",
        "answer": "Pittsburgh Steelers"
    },
    {
        "question": "What sport uses a shuttlecock?",
        "answer": "Badminton"
    },
    {
        "question": "How long is a marathon (in miles)?",
        "answer": "26.2"
    },
    {
        "question": "Which athlete is known as 'The Greatest' and 'The People's Champion'?",
        "answer": "Muhammad Ali"
    }
]

# Select 5 random questions
selected = random.sample(questions, 5)

score = 0

print("🏆 Welcome to the Sports Trivia Challenge! 🏆\n")

for i, q in enumerate(selected, 1):
    print(f"Question {i}: {q['question']}")
    user_answer = input("Your answer: ").strip()

    if user_answer.lower() == q["answer"].lower():
        print("Correct!")
        correct_sound()
        score += 1
    else:
        print(f"Incorrect! The correct answer was: {q['answer']}")
        incorrect_sound()

    print()

print(f"🎉 Game Over! Your final score is {score}/5 🎉")
