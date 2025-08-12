import pyinputplus as pyip
import random
import time
import sys

numberOfQuestion = 10
correctAnswers = 0

print("Welcome to the multiplication quiz!")
print(f"You will be asked {numberOfQuestion} questions.")

quiz_start_time = time.time()  # start timing the whole quiz
try:
    for i in range(numberOfQuestion):
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        prompt = f"Question ({i + 1}): {num1} * {num2} = "

        try:
        # Ask question with a 5-second timeout and max 2 tries
            answer = pyip.inputNum(prompt=prompt, timeout=5, limit=2,)
        except pyip.TimeoutException:
            print("You have exceeded the time limit. Moving to the next question.")
            continue
        except pyip.RetryLimitException:
            print("Too many attempts. Moving to the next question.")
            continue
        if answer == num1 * num2:
            print("Correct!\n")
            correctAnswers += 1
        else:
            print(f"Incorrect. The correct answer is {num1 * num2}.\n")

        time.sleep(1)  # wait for 1 second before the next question
except KeyboardInterrupt:
    print("\nQuiz interrupted by user. Exiting...")
    sys.exit()

quiz_end_time = time.time()  # end timing the quiz
elapsed_time = quiz_end_time - quiz_start_time  # calculate elapsed time

print(f"\nQuiz finished!")
print(f"You answered {correctAnswers} out of {numberOfQuestion} questions correctly.")
print(f"Total time taken: {elapsed_time:.2f} seconds.")
