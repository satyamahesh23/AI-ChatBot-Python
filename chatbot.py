from datetime import datetime
import webbrowser
name=input("enter your name  : ")
print("\n====================================")
print(' Welcome to smart AI chatbot')
print("====================================")
print(f"hello {name}! iam your AI chatbot")
print('type "bye" anything to exit\n')
while True:
    user=input("you :").lower()
    #greeting
    if user=='hello' or user=='hi':
        print("Bot: hello! Nice to meet you")
    elif "good morning" in user:
        print("Bot: Good Morning! Have a wonderful day.")
    elif "good afternoon" in user:
        print("Bot: Good Afternoon!")
    elif "good night" in user:
        print("Bot: Good Night! Sweet dreams.")
    #personal questions
    elif "your name" in user:
        print("Bot: My name is SmartBot.")
    elif "who made you" in user:
        print("Bot: I was created by Satya using Python.")
    elif "how are you" in user:
        print("Bot: I am doing great! Thank you for asking.")

    elif "what can you do" in user:
        print("Bot: I can answer questions, tell time and date, perform calculations, and open websites.")
    #ai and python
    elif user==" ai" or "artificial intelligences" in user:
        print("Bot: AI stands for Artificial Intelligence. It enables machines to think and learn.")
    elif "python" in user:
          print("Bot: Python is a powerful and beginner-friendly programming language.")
    #date and time
    elif "time" in user:
        current_time=datetime.now().strftime("%I:%M:%S %p")
        print("Bot: Current time is", current_time)
    elif "date" in user:
        current_date=datetime.now().strftime("Bot: Current time is", current_time)
        print("Bot: Today's date is", current_date)
        #jjjokes
    elif "joke" in user:
        print("Bot: Why do programmers prefer Python?")
        print("Bot: Because they don't like Java problems!")
   # Open Websites
    elif "open youtube" in user:
        print("Bot: Opening YouTube...")
        webbrowser.open("https://www.youtube.com")
    elif "open google" in user:
        print("Bot: Opening Google...")
        webbrowser.open("https://www.google.com")
    elif "open github" in user:
        print("Bot: Opening GitHub...")
        webbrowser.open("https://github.com")
    # User Name
    elif "my name" in user:
        print(f"Bot: Your name is {name}.")

    # Thank You
    elif "thank you" in user or "thanks" in user:
        print("Bot: You're welcome!")

    # Exit
    elif user == "bye":
        print(f"Bot: Goodbye {name}! Have a nice day.")
        break
    else:
        print("Bot: Sorry, I don't understand that. Please ask something else.")





         