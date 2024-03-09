import os, sys
import openai
import json
from pathlib import Path
from importlib import reload
src_path = Path("/content/drive/MyDrive/CALM/src/")


if str(src_path) not in sys.path:
  sys.path.append(str(src_path))
import utils
reload(utils)



def main(prompt):
  prev_response = None
  simplied_queries= utils.convert_to_multiple_simple_queries(prompt)
  print(simplied_queries)
  for query in eval(simplied_queries):
    if prev_response:
      query = prev_response + "\n" + query   
    if utils.need_external_api(query) == "1":
      prev_response = None
      print(query)
      print("Yeh sewa abhi nahin ho payega, mere dost!")
    else: 
      response = utils.query_openai_chatbot(query)
      print(query)
      print(response)
      prev_response = response



if __name__ == "__main__":
  while True:
    print("Hi, how can I help you?")
    prompt = input()
    if any(x in prompt.lower() for x in ['stop', 'exit', 'break']):
      break
    main(prompt)
    