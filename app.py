from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI

from knowledge import knowledge
from intents import greetings, help_words, bye_words, small_talk

model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.7
)

print("="*50)
print("🤖 Welcome to AI Chatbot")
print("Type 'exit' to quit.")
print("="*50)


while True:

    user = input("\nYou : ")

    if user.lower()=="exit":
        print("Bot : Goodbye 👋")
        break

    with open("history.txt","a") as file:
        file.write(f"\nUser : {user}")

    message=user.lower()

    # Greeting
    if message in greetings:
        response="Hello! How can I help you today?"

    # Help
    elif message in help_words:
        response="I can answer greetings, AI questions, Python, SQL and more."

    # Bye
    elif message in bye_words:
        response="Goodbye! Have a great day."

    # Small Talk
    elif message in small_talk:
        response=small_talk[message]

    # Knowledge Base
    elif message in knowledge:
        response=knowledge[message]

    # Otherwise use Mistral
    else:

        ai_response=model.invoke(user)

        response=ai_response.content

    print("\nBot :",response)

    with open("history.txt","a") as file:
        file.write(f"\nBot : {response}\n")