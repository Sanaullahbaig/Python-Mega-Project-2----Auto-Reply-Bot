🧠 Python Mega Project 2 – Auto Reply Bot

This project is an Auto Reply Bot built using Python, Google Gemini AI, and PyAutoGUI. It automatically reads messages from a chat window (like WhatsApp Web), analyzes the latest message, and replies intelligently in a human-like tone — all hands-free!

🚀 Features

🤖 Reads chat text automatically using PyAutoGUI

🧩 Analyzes messages and generates intelligent replies using Google Gemini AI

💬 Responds in a friendly tone as Sanaullah Mughal (Urdu + English mix)

🪄 Automatically pastes and sends the reply in chat

🖱️ Includes a separate cursor position script to find screen coordinates

🧰 Requirements

Install all required packages using:

pip install -r requirements.txt


Your requirements.txt should include:

pyautogui
pyperclip
google-generativeai
time

⚙️ Setup

Clone the repository:

git clone https://github.com/your-username/auto-reply-bot.git
cd auto-reply-bot


Add your Gemini API key:
Replace

genai.configure(api_key="API_KEY_HERE")


with your real API key from Google AI Studio
.

Get your chat window coordinates:
Run the following helper script to find your cursor positions:

import pyautogui

while True:
    print(pyautogui.position())


Move your mouse where you want to click or drag, and note down the coordinates shown in the terminal.

Update coordinates in the main script where necessary:

pyautogui.click(956, 1045)   # Example: Chrome icon
pyautogui.dragTo(1713, 902)  # Example: Chat selection area

💡 How It Works

The bot opens Chrome using PyAutoGUI click commands.

It selects and copies the chat text from the screen.

The copied text is sent to Gemini AI for response generation.

The AI-generated message is automatically pasted and sent in the chat.

🖥️ Example Workflow

Open your chat window (e.g., WhatsApp Web).

Run the script.

The bot will:

Copy the last message

Generate a reply

Send it automatically

🧭 Cursor Position Finder

Use this small script to get your screen coordinates for automation setup:

import pyautogui

while True:
    a = pyautogui.position()
    print(a)


💡 Move your mouse anywhere — the terminal will print the (x, y) position.

⚠️ Notes

This script automates your mouse and keyboard — don’t move your cursor while it runs.

Works best when the chat window stays in the same position each time.

Use it responsibly and only in your own chat environments.

🧑‍💻 Author

Sanaullah Baig
Python Developer 🇵🇰
📧 sanaullahmughal49@gmail.com
