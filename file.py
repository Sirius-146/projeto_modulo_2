import json

def add_favorite(fav_name:dict, filename='favorites.json'):
  """Write the book information in the json file.\n
  If the file does not exist, create one."""
  try:
    with open(filename, 'r', encoding='utf-8') as arquivo:
      favorites = json.load(arquivo)
  except (FileNotFoundError, json.JSONDecodeError):
    favorites = []
  favorites.append(fav_name)
  with open(filename, 'w', encoding='utf-8') as arquivo:
    json.dump(favorites, arquivo, indent=2)

def remove_favorite(fav_name:str, filename:str='favorites.json'):
    """Erase book information from the file"""
    try:
        with open(filename, 'r', encoding='utf-8') as arquivo:
            favorites = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return print('Não há livros na lista!')
    
    favorites = [book for book in favorites if book['title'].lower() != fav_name]

    with open(filename, 'w', encoding='utf-8') as arquivo:
        json.dump(favorites, arquivo, indent=2)