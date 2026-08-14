import json

def load_data():
  with open('static/data/notes.json', 'r', encoding='utf-8') as f:
    content  =  json.load(f)
    return content

def create_data(name, details):
    content = {
      "titulo": name,
      "detalhes": details,
    }

    try:
       data = load_data()
    except (FileNotFoundError, json.JSONDecodeError):
       data = []
       
    data.append(content)

    with open('static/data/notes.json', 'w', encoding='utf-8') as f:
      json.dump(data, f, ensure_ascii=False, indent=2)
