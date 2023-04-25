# AIPasswordGenerator
This Python program generates random, meaningful, hard-to-remember passwords using OpenAI's GPT-3 API.

## Prerequisites
To run this program, you'll need to have the following:

1. Python 3.6 or later installed on your computer
2. An API key for OpenAI's GPT-3 API

## Installation
1. Clone this repository to your local machine
2. Install the required packages by running pip install -r requirements.txt
3. Set up your OpenAI API key by following the instructions in the OpenAI Secret Manager repository and adding the key to your environment variables as OPENAI_API_KEY

## Usage
To generate a random, meaningful, hard-to-remember password, simply run the following command:

<pre>
python generate_password.py
</pre>

The program will then use the GPT-3 API to generate a random password and print it to the console in the following format:

<pre>
Generated password: [password]
</pre>

To generate multiple passwords that contain both upper and lower case characters, run the following command:

<pre>
python generate_multiple_passwords.py
</pre>

The program will generate 5 passwords and print them to the console, each containing both upper and lower case characters.

## License
This program is licensed under the MIT License.

## Credits
This program was created by Abdur Rahman Mansoor.
