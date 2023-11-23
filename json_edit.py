import json

def add_favorite(fav_name, filename='favorites.json'):
  try:
    with open(filename, 'r') as arquivo:
      favorites = json.load(arquivo)
  except (FileNotFoundError, json.JSONDecodeError):
    favorites = []
  favorites.append(fav_name)
  with open(filename, 'w') as arquivo:
    json.dump(favorites, arquivo, indent=2)

def remove_favorite(fav_name, filename='favorites.json'):
    try:
        with open(filename, 'r') as arquivo:
            favorites = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return 'Não há livros na lista'
    
    favorites = [book for book in favorites if book['title'].lower() != fav_name]

    with open(filename, 'w') as arquivo:
        json.dump(favorites, arquivo, indent=2)