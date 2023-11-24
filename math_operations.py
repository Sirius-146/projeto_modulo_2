from functools import reduce

def return_max_min(name,pages):
  maximo = None
  minimo = None
  for i in range(len(pages)):
    if pages[i] == max(pages):
      maximo = (name[i], pages[i])
  for i in range(len(pages)):
    if pages[i] == min(pages):
      minimo = (name[i], pages[i])
  return [maximo,minimo]

def calc_median_total_pages(pages):
  total_pages = reduce(lambda x,y: x+y, pages, 0)
  median = (total_pages/len(pages))
  return total_pages, median

def std_dev(pages,median):
  test = [(x-median)**2 if x>median else (median-x)**2 for x in pages]
  sum_values = sum(test)/(len(pages))
  standard_deviation = sum_values**.5
  return standard_deviation

def list_categories(dicionary):
    def reduce(counter, key):
        if dicionary[key] in counter:
            counter[dicionary[key]]+=1
        else:
            counter[dicionary[key]] = 1
        return counter
    return reduce

def reduce_categories(grouped_categories,dicionary):
   return reduce(grouped_categories,dicionary,{})