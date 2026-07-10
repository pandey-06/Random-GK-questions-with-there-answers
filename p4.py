# General Knowledge Quiz

score = 0

print("===== General Knowledge Quiz =====\n")

# Question 1
answer = input("1. What is the capital of France? ")
if answer.lower() == "paris":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is Paris.\n")

# Question 2
answer = input("2. Which planet is known as the Red Planet? ")
if answer.lower() == "mars":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is Mars.\n")

# Question 3
answer = input("3. How many days are there in a week? ")
if answer == "7":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is 7.\n")

print("===== Quiz Finished =====")
print("Your Final Score:", score, "/3")