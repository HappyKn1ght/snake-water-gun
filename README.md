# 🐍💧🔫 Snake Water Gun Game (Python CLI)

A command-line Snake Water Gun game built in Python. Created to practice dictionaries, the `random` module, `while` loops, `try / except` input validation, and score tracking.

## ✨ Features
- **Classic Game Rules:** Snake drinks Water, Water douses Gun, and Gun shoots Snake.
- **Randomized Opponent:** Uses `random.randint()` to generate unpredictable computer choices every round.
- **Input Validation:** Handles non-numeric inputs (`ValueError`) and out-of-range numbers (`< 1` or `> 3`) without crashing the game.
- **Live Scoreboard & Quit Anytime:** Tracks user wins, computer wins, and draws across rounds, displaying the final scoreboard whether you finish or press `'q'` to quit.

## 🚀 How to Run
1. **Clone the repository:**
   ```bash
   git clone https://github.com/HappyKn1ght/snake-water-gun
   ```
2. **Navigate into the project folder:**
   ```bash
   cd snake-water-gun
   ```
3. **Run the game:**
   ```bash
   python main.py
   ```

## 🖥️ Example Output

```text
Snake Water Gun Game
1 for Snake
2 for Water
3 for Gun
Enter Your Choice or 'q' to quit: 1
You chose Snake
Computer Chose Water
You Win!
Do you want to try again? (y/n): n
----------------------------------------
FINAL SCOREBOARD
----------------------------------------
User Score  Computer Score  Match Draw
   1              0             0

----------------------------------------
🏆 You Are the Overall Winner!
----------------------------------------

GAME OVER...
Thanks for playing!
```