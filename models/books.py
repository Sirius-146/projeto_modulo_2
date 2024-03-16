class Book:
	favorites = []
	def __init__(self, book_dict:dict):
		self._title = book_dict['title'].title()
		self._author = book_dict['author'].title()
		self._publisher = book_dict['publisher'].title()
		self._pages = book_dict['pages']
		self._category = book_dict['category']
		self._description = book_dict['description']
		self._favorite = False

	def __str__(self) -> str:
		"""Return a string with information of a book"""
		string = f"""{self._title} \nAutor: {str(self._author).ljust(15)} | Editora: {str(self._publisher).ljust(15)} | Páginas: {(self._pages)} | Categoria: {str(self._category).ljust(15)} \nDescrição: \n{self._description}"""
		return string

	def edit_favorite(self):
		self._favorite = not self._favorite
		if (self._favorite):
			Book.favorites.append(self)
		else:
			Book.favorites.remove(self)
	
	def to_dict(self) -> dict:
		"""Convert the object into a dictionary in order to be saved in the JSON file."""
		book = {
			'title': self._title,
			'author': self._author,
			'publisher': self._publisher,
			'pages': self._pages,
			'category': self._category,
			'description': self._description
			}
		return book
	
	@classmethod
	def print_names(cls):
		"""Return all the titles from the books in favorites' list."""
		for book in cls.favorites:
			print(book._title)
	
	def search_book(fav_name:str):
		"""Search the value of a key that matches user input.\n
		Return a dictionary with the corresponding values."""
		book = next(filter(lambda book: book._title.title()==fav_name.title(), Book.favorites))
		return book