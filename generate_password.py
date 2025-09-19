import openai_secret_manager
import openai

def generate_password():
    """
    Generates a random, meaningful password using OpenAI's GPT-3 API.
    """
    # Fetching the OpenAI API key
    assert "openai" in openai_secret_manager.get_services()
    secrets = openai_secret_manager.get_secret("openai")

    # Setting up the OpenAI API client
    openai.api_key = secrets["api_key"]

    prompt = "Generate a random, meaningful password that's hard to remember."
    completions = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
    )

    if completions.choices:
        password = completions.choices[0].text.strip()
        return password
    else:
        return "Could not generate a password."

if __name__ == "__main__":
    password = generate_password()
    print(f"Generated password: {password}")
