import os
import json
from openai import OpenAI
from pathlib import Path


keys_path = Path("/content/drive/MyDrive/Tutorial/key.json")


def load_api_key(filename):
    try:
        with open(filename, 'r') as f:
            api_key = json.load(f)
            return api_key['openai']
    except FileNotFoundError:
        print(f"API key file {filename} not found.")


os.environ['OPENAI_API_KEY'] = load_api_key(keys_path)
client = OpenAI()

def query_openai_chatbot(prompt, max_tokens=50):  
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a helpful assistant"},
      {"role": "user", "content": prompt}
    ]
  )
  return completion.choices[0].message.content

def convert_to_multiple_simple_queries(query, max_tokens = 500):
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "Convert the query into a list data \
      structure in python where each element in the list is string representing a simple \
      easy to understand query that can be fed into any LLM"},
      {"role": "user", "content": query}
    ]
  )
  return completion.choices[0].message.content

def need_external_api(query, max_tokens = 500):
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "if the query requires calling an external \
      api other than openai then return 1 otherwise 0"},
      {"role": "user", "content": query}
    ]
  )
  return completion.choices[0].message.content
   
      