# Jeffrey Clabo
# 4/8/26 
# PHW1
# Score Averages



# Implementation of the algorithm
def main():
    # Step 1
    num_scores = int(input("How many scores do you want to enter? "))

    scores = []

    # Step 3
    for i in range(num_scores):
        while True:  # Loop until a valid score is entered
            score = float(input(f"Enter score #{i + 1}: "))
            if 0 <= score <= 100:  # Step 3b
                scores.append(score)  # Step 3c
                break
            else:
                print("INVALID Score entered!!!!")
                print("Score should be between 0 and 100")
    
    # Step 4a
    lowest_score = min(scores)
    
    # Step 4b
    average_score = sum(scores) / len(scores)
    
    # Step 4c
    if average_score >= 90:
        grade = 'A'
    elif average_score >= 80:
        grade = 'B'
    elif average_score >= 70:
        grade = 'C'
    elif average_score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    # Step 5
    print("\\-----------Results-----------")
    print(f"Lowest Score : {lowest_score:.1f}")
    print(f"Modified List : {scores}")
    print(f"Scores Average : {average_score:.2f}")
    print(f"Grade : {grade}")
    print("-----------------------------")

# Run the main function
main()