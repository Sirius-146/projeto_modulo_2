from functools import reduce

class Math:
	def return_value(name:str, pages:int, option:str = max):
		"""Receive a list with the names and a list with the pages.\n
		The return contains, by default, the highest value on pages list.
		To get the smallest value, use option=min.

		Returns:
						[(name, pages)]
		"""
		value = [(name[x], pages[x]) for x in range(len(pages)) if pages[x] == option(pages)]
		return value

	def calc_total_pages(pages:list):
		"""Calculate the sum of all items."""
		return sum(pages)

	def calc_mean(total_pages:int, pages:list):
		"""Calculate the mean of all items."""
		return (total_pages/len(pages))

	def std_dev(pages:list,mean:float) ->float:
		"""Calculate the standard deviation of the items."""
		test = [(x-mean)**2 if x>mean else (mean-x)**2 for x in pages]
		mean_values = sum(test)/(len(pages))
		standard_deviation = mean_values**.5
		return standard_deviation

	def list_categories(dicionary:dict):
		"""Generate a function that allows reduce_categories() to run"""
		def redutor(counter:dict, key:str):
			if dicionary[key] in counter:
				counter[dicionary[key]]+=1
			else:
				counter[dicionary[key]] = 1
			return counter
		return redutor

	def reduce_categories(grouped_categories:dict,dicionary:dict):
		"""Create a dictionary with the category values and how many times their appear on the favorites."""
		return reduce(grouped_categories,dicionary,{})

	def show_extra_info(max_results, min_results, total_pages, mean, st_dev, books_category):
		"""Print extra information from favorites to each user"""
		print(f'Maior livro: {max_results[0][0]:^20}\t Páginas: {max_results[0][1]} \nMenor livro: {min_results[0][0]:^20}\t Páginas: {min_results[0][1]}\n')
		print('Livros por categoria:')
		for category in books_category:
			print(f'{category} - {books_category[category]}')
		print(f'\nTotal de páginas: {total_pages}\t Média de páginas: {int(mean)}\t Desvio Padrão: {st_dev:.2f}')

	def get_extra_info(name, pages, category):
		"""Run all resources needed to get extra information from favorite books"""
		dicionary = dict(zip(name,category))
		max_results = Math.return_value(name,pages)
		min_results = Math.return_value(name,pages,min)
		total_pages = Math.calc_total_pages(pages)
		mean = Math.calc_mean(total_pages, pages)
		st_dev = Math.std_dev(pages, mean)
		grouped_categories = Math.list_categories(dicionary)
		books_category = Math.reduce_categories(grouped_categories,dicionary)
		Math.show_extra_info(max_results, min_results, total_pages, mean, st_dev, books_category)