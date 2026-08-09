# Number Guessing Game 🎮

A simple interactive command-line Number Guessing Game written in Python. The program generates a random number between 1 and 25, and the player attempts to guess it using helpful directional hints.

---

## Features

* **Random Target Generation:** Uses Python's `random` module to pick a secret number from 1 to 25.
* **Interactive Hints:** Informs the player if their guess is too high or too low.
* **Menu Options:** Provides a simple starting menu to begin the game or exit immediately.

---

## How to Run

### Prerequisites

Make sure you have **Python 3.x** installed on your system.

### Steps

1. Clone or download this repository.
2. Open your terminal or command prompt in the directory containing `game.py`.
3. Run the script:

```bash
python game.py

```

---

## How to Play

1. Select **`1`** from the main menu to **Start The Game**, or **`2`** to **Quit**.
2. Enter your numerical guess when prompted.
3. Read the hint:
* **Too High:** Select a smaller number.
* **Too Low:** Select a larger number.


4. Keep guessing until you hit the correct number and win!

---

## Code Preview

```python
import random 

num = random.randint(1, 25)

print("\n1. Start The Game .. ")
print("2. Quit ...")
choice = int(input("\nEnter Your Choice : "))

while True:
    if choice == 1:
        g = int(input("Enter Your Guess Number : "))
        if g == num:
            print("Congratulations .... You Won the Game ...")
            break       
        elif g > num:
            print("Your Guess Number Is larger than the Correct Number ...")        
        else:
            print("Your Guess Number Is smaller than the Correct Number ...")
    elif choice == 2:
        print("\nThank You for Playing....\n") 
        break
    else:
        print("\nInvalid Choice...")
        break

```
