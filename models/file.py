import json
class JSONLoad:
	def locate_favorite(filename:str ='favorites.json') -> str:
		"Create a new file. If the file already exists, call the writing function"
		try:
			with open(filename, 'x') as archive:
				favorites = []
				json.dump(favorites, archive, indent=2)
				return filename
		except FileExistsError:
			return filename

	def see_favorites(filename:str='favorites.json') -> dict | str:
		"""Read the file and return the content"""
		try:
			with open(filename, 'r') as archive:
				content = json.load(archive)
				if content == []:
					raise FileNotFoundError
		except FileNotFoundError:
			content = 'Sua lista está vazia'
		return content
	
	def write_favorite(item:dict, filename='favorites.json'):
		"""Write the book information in the json file."""
		with open(filename, 'r', encoding='utf-8') as archive:
			favorites = json.load(archive)
		favorites.append(item)
		with open(filename, 'w', encoding='utf-8') as archive:
			json.dump(favorites, archive, indent=2)
	
	def unwrite_favorite(fav_name:str, filename:str='favorites.json'):
		"""Erase book information from the file"""
		with open(filename, 'r', encoding='utf-8') as archive:
				favorites = json.load(archive)

		favorites = [book for book in favorites if book['title'].lower() != fav_name.lower()]

		with open(filename, 'w', encoding='utf-8') as archive:
			json.dump(favorites, archive, indent=2)