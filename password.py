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
    prompt = "Generate a random, meaningful password that's hard to remember, contains both uppercase and lowercase letters, as well as numbers and special characters, and is also a real English word."
    completions = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
    )

    password = completions.choices[0].text.strip()

    # add uppercase and lowercase letters, numbers, and special characters to password
    length = len(password)
    chars = string.ascii_letters + string.digits + string.punctuation
    password = password + ''.join(random.choice(chars) for i in range(length))
    password = ''.join(random.sample(password, len(password)))

    return password

# generate and print a password
password = generate_password()
print(f"Generated password: {password}")
