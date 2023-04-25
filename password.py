import openai_secret_manager
import openai
import random
import string

# Fetching the OpenAI API key
assert "openai" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secret("openai")

# Setting up the OpenAI API client
openai.api_key = secrets["api_key"]

# generate a random, meaningful password using OpenAI's GPT-3
def generate_password():
    prompt = "Generate a random, meaningful password that's hard to remember."
    completions = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
    )

    password = completions.choices[0].text.strip()
    return password

# generate multiple passwords that contain both upper and lower case characters
num_passwords = 5
passwords = []
for i in range(num_passwords):
    while True:
        password = generate_password()
        if any(c.isupper() for c in password) and any(c.islower() for c in password):
            passwords.append(password)
            break

# print the generated passwords
print("Generated passwords:")
for password in passwords:
    print(password)
