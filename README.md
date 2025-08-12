# Multiplication Quiz

A simple interactive multiplication quiz built with Python and PyInputPlus.

---

## Overview

This program quizzes the user with 10 random multiplication questions involving single-digit numbers (0–9). The user has limited time and attempts to answer each question. At the end, the program displays the total number of correct answers and the total time taken.

---

## Features

- Random multiplication questions between 0 and 9.
- Time limit of 5 seconds per question.
- Maximum of 2 attempts per question.
- Tracks and displays the number of correct answers.
- Displays total time taken to complete the quiz.
- Graceful handling of timeout and retry limit exceptions.

---

## Requirements

- Python 3.x
- [PyInputPlus](https://pypi.org/project/PyInputPlus/)

Install PyInputPlus via pip:

```bash
pip install pyinputplus
````

---

## How to Run

1. Clone or download this repository.
2. Ensure you have Python 3 and PyInputPlus installed.
3. Run the script:

```bash
python3 multiplication_quiz.py
```

4. Answer the multiplication questions within the time and attempt limits.
5. View your score and total time at the end.

---

## Example

```
Welcome to the multiplication quiz!
You will be asked 10 questions.
Question 1: 3 * 7 = 21
Correct!
Question 2: 5 * 9 = 45
Incorrect. The correct answer is 45.
...
Quiz finished!
You answered 8 out of 10 questions correctly.
Total time taken: 55.32 seconds.
```

---

## License

This project is open source and free to use under the MIT License.

---

## Author

Your Name (TheGhostAnalyst)

---

Feel free to contribute or suggest improvements!

```

