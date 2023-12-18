from typing import List, Dict
import os
import requests


class OpenAIError(Exception):
    pass


# - get prev formatted messages list
# - format final prompt from prompt and messages list
# - send out
# - process response
# - add response to messages list


class LLMGeneration:
    def __init__(self, prompt: str):
        self.prompt: str = prompt

    def pre_run_callback(self):
        # get and set messages for this generation
        pass

    def post_run_callback(self):
        # get and set messages for this generation
        pass

    def format_prompt(self):
        # get orevious_messages attr and format prompt
        return self.prompt

    def run(self):
        prompt = self.format_prompt()
        return self.generate(prompt)

    def process_response(self, response: Dict) -> str:
        return response["choices"][0]["text"]

    def generate(self, prompt: str) -> str:
        response = self.request_generation(prompt)
        # save the messages here
        return self.process_response(response)

    def request_generation(prompt: str) -> Dict:
        # Get the OpenAI API key from the environment variable
        api_key = os.environ.get("OPENAI_API_KEY")

        if not api_key:
            raise ValueError(
                "OpenAI API key not found in environment variable OPENAI_API_KEY"
            )

        # Set the OpenAI API endpoint
        api_endpoint = "https://api.openai.com/v1/chat/completions"

        # Set the payload with the prompt
        data = {
            "prompt": prompt,
            "max_tokens": 50,
        }

        # Set the headers with your API key
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        }

        # Make the HTTP POST request to the OpenAI API
        response = requests.post(api_endpoint, json=data, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Return the generated completion
            return response.json()
        else:
            # Raise an exception with the error message
            raise OpenAIError(f"Error: {response.status_code}\n{response.text}")
