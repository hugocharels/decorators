"""
Auteur: Charels Hugo
Permet d'afficher le temps d'exécution d'une fonction
"""

def timer(name=""):
	def decor(func):
		def wrapper(*args, **kwargs):
			from time import time
			start = time()
			x = func(*args, **kwargs)
			end = time()
			print(f"{name} time : {end-start}s")
			return x
		return wrapper
	return decor
