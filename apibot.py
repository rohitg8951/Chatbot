from openai import OpenAI


client = OpenAI(
    api_key="GROQ_API_KEY",
    base_url="https://api.groq.com/openai/v1"
)

while True:
    user_input = input("You: ")
    if (user_input.lower() == "quit"):
        print("Bot : Goodbye!")
        break
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "Answer me only regarding to Sports Topic Not out of it"},
            {"role": "user", "content": user_input}
            ]
        )
    print("Bot:", response.choices[0].message.content)