import google.generativeai as genai
import os
import json

from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro-latest")

def process_json_file(json_file):
  """Lê e processa um arquivo JSON contendo perguntas e respostas."""
  try:
    with open(json_file, "r", encoding="utf-8") as file:
      data = json.load(file)

    formatted_data = []
    for subject, qa_list in data.items():
      for qa in qa_list:
        if isinstance(qa, list) and len(qa) == 2:
          question, answer = qa
          formatted_data.append({"question": question, "answer": answer, "subject": subject})
    return formatted_data

  except FileNotFoundError:
    print(f"Erro: O arquivo '{json_file}' não foi encontrado.")
    return []
  except json.JSONDecodeError:
    print("Erro ao decodificar o JSON. Verifique a estrutura do arquivo.")
    return []

def get_response(formatted_data, question):
  """Busca a resposta no JSON baseado na pergunta do usuário."""
  for item in formatted_data:
    if item["question"].lower() == question.lower():
      return item['answer']
  return

def main():
  """Loop principal do chatbot."""
  """Chatbot versão terminal."""
  json_file = "perguntas_escolares_com_respostas.json"
  formatted_data = process_json_file(json_file)

  if not formatted_data:
    print("Encerrando o programa devido a erro no carregamento do JSON.")
    return

  history = []
  chat = model.start_chat(history=history)

  while True:
    input_user = input("Faça uma pergunta (ou digite 'sair' para encerrar): ")

    if input_user.lower() == "sair":
      print("\nHistórico da conversa:")

      for entry in history:
        print(f"Usuário: {entry['user']}")
        print(f"Bot: {entry['bot']}\n")

      print("\nEncerrando o programa.")

      break
  
    response = get_response(formatted_data, input_user)

    if response:
      print(response)

    else:
      try:
        response = chat.send_message(input_user)
        response_text = response.text if hasattr(response, "text") else str(response)
        print(f"\n{response_text}\n")

        history.append({"user": input_user, "bot": response_text})
      except Exception as e:
        print(f"Erro ao conectar com o Gemini: {e}")

def chatbot_response(input_user, history):
  """Chatbot para versão web."""
  json_file = "perguntas_escolares_com_respostas.json"
  formatted_data = process_json_file(json_file)

  if not formatted_data:
    print("Encerrando o programa devido a erro no carregamento do JSON.")
    return

  response = get_response(formatted_data, input_user)

  if response:
    return response

  else:
    try:
      chat = model.start_chat(history=history)
      response = chat.send_message(input_user)
      response_text = response.text if hasattr(response, "text") else str(response)

      return response_text
    except Exception as e:
      print(f"Erro ao conectar com o Gemini: {e}")
      return f"Erro ao conectar com o Gemini: {e}"

if __name__ == "__main__":
  main()