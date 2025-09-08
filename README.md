# 🎲 Number Guessing Game

A fun and interactive number guessing game built with **Flask**.  
You have **10 attempts** to guess the secret number between **1 and 100**.  
Get real-time feedback if your guess is **too high**, **too low**, or **correct**! 🎉

---

## 🚀 Features
- Random secret number generation (1–100)
- 10 attempts per game
- Real-time feedback (too high/low/correct)
- Session-based gameplay
- Game over message when attempts run out

---

## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone <your-repo-url>
cd <repo-folder>
pip install flask
```

---

## ▶️ How to Run

Run the Flask app:

```bash
python app.py
```

The app will start at:

```
http://127.0.0.1:5000/
```

---

## 🎮 How to Play
1. Start the game — a secret number will be generated.
2. You have **10 attempts** to guess the number.
3. After each guess, you'll see one of the following:
   - ⬆️ *Too low! Try higher.*
   - ⬇️ *Too high! Try lower.*
   - 🎉 *Correct! You win!*
4. If you run out of attempts, the game ends with a **Game Over** message.

---

## 📂 Project Structure

```
├── app.py           # Main Flask backend
├── templates/
│   └── index.html   # Frontend UI
```

---

## ⚡ Example API Endpoints
- **POST** `/start` → Starts a new game
- **POST** `/guess` → Submit a guess (JSON: `{ "guess": 42 }`)

---

## 🛠 Tech Stack
- **Python 3**
- **Flask**
- **HTML/CSS/JS** (frontend)

---

## 👩‍💻 Author
Developed by **Nidhi Kulkarni (https://github.com/Nidhirk2113)** ✨
