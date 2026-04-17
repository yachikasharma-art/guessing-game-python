# 🎮 Number Guessing Game

A fun and interactive Python game where you try to guess a randomly chosen number between 1 and 100!

## 📋 Overview

This is a simple command-line guessing game that challenges you to find the secret number with helpful hints. The game keeps track of how many attempts you take and lets you play multiple rounds.

## ✨ Features

- 🎲 Random number generation between 1-100
- 💡 Helpful hints (higher/lower)
- 📊 Tracks number of guesses
- 🔄 Play again option
- 😊 Fun emojis and interactive messages
- 🎯 Simple and beginner-friendly code

## 🚀 Quick Start

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yachikasharma-art/guessing-game-python.git
cd guessing-game-python
```

2. Run the game:
```bash
python guessing_game.py
```

## 🎯 How to Play

1. Run the program
2. The computer picks a random number between 1 and 100
3. You make a guess by entering a number
4. The game tells you if your guess is too high or too low
5. Keep guessing until you find the correct number!
6. Try to guess it in as few attempts as possible
7. Play again or exit when done

## 💡 Example Gameplay
hiii!, welcome to the guesseing game
I have picked number from 1 to 100
LET'S START
enter number you guessed: 50
😊 higher number please!
enter number you guessed: 75
😇 lower number please!
enter number you guessed: 63
🎉yayyyyyy!!!🎉 you gussed  it right!!!
you got it with 3 guesses

Phir khelna hai? (y/n): y

## 🎮 Game Rules

- Guess a number between **1 and 100**
- You get unlimited attempts
- The game will tell you:
  - 😊 **"higher number please!"** - Your guess is too low
  - 😇 **"lower number please!"** - Your guess is too high
  - 🎉 **"you guessed it right!"** - You found it!
- Try to guess in as few attempts as possible!

## 🛠️ Code Structure

The game uses:
- `random.randint()` for generating random numbers
- `while True` loop for continuous gameplay
- Recursive function call for replay functionality
- Input validation and user interaction

## 🎯 Tips to Win

- Start with 50 (middle of the range)
- Use binary search strategy
- Always guess the middle of the remaining range
- Pay attention to the hints!

## 🚀 Future Enhancements

- [ ] Difficulty levels (Easy/Medium/Hard with different ranges)
- [ ] High score tracking
- [ ] Limited number of attempts mode
- [ ] Timer to track how fast you can guess
- [ ] Leaderboard system
- [ ] GUI version with Tkinter
- [ ] Multiplayer mode


## 👨‍💻 Author

Yachika Sharma - [@yachikasharma-art](https://github.com/yachikasharma-art)

## 🙏 Acknowledgments

- Built with Python's `random` module
- Perfect for Python beginners learning loops and conditionals

---

⭐ If you enjoyed this game, please give it a star! Happy Guessing! 🎲
