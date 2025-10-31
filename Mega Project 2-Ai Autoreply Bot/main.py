import pyautogui
import pyperclip
import time
import google.generativeai as genai

# Step 1: Click on chrome icon at cordinates (956, 1045)  
pyautogui.click(956, 1045)
time.sleep(2)

def is_last_message_from_sender(chat_log, sender_name = "sender_name_here"):
    # Split each chat log into individual messages 
    messages = chat_log.strip().split("/2025] ")[-1]
    if sender_name in messages:
        return True
    return False


while True:
    # Configure Gemini with your Google API key
    genai.configure(api_key="API_KEY_HERE")

    # Step 2: Drag the mouse from (900, 289) to (1713, 902) to select the text
    pyautogui.moveTo(900, 289)
    pyautogui.dragTo(1713, 902, duration=1.0, button='left')

    # Step 3: Copy the selected text to the clip board
    pyautogui.hotkey("ctrl", 'c')
    time.sleep(2) # Wait for one second to ensure the copy command is completed
    pyautogui.click(1725, 762) # click to unselect the selected text

    # Step 4: Retrive the text from clipboard and store it in a variable 
    chat_history = pyperclip.paste()

    # Print the copied text to verify
    print(chat_history)

    if is_last_message_from_sender(chat_history):
        # Create the model (you can use gemini-2.5-flash or gemini-2.5-pro)
        model = genai.GenerativeModel("gemini-2.5-flash")

        # Generate the response
        message = model.generate_content([
            "You are a person name Sanaullah Mughal who speak urdu and english. You are from Pakistan. You analyze the chat hisory and respond like Sanaullah Mughal,respond like a normal friend and have to keep the message short don't add the time and name at the start of your message.",
            chat_history
        ])

        response_text = message.text if hasattr(message, "text") else str(message)
        pyperclip.copy(response_text)

        # Step 5: Click at cordinate (1280, 945)
        pyautogui.click(1280, 945) 

        # Step 6: Paste the text
        pyautogui.hotkey('ctrl', 'v')

        # Step 7: Press Enter

        pyautogui.press('enter')
