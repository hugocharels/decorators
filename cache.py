
def cache(func):
	def wrapper(arg):
		if "_cache_data" not in globals():
			globals()["_cache_data"] = {}
		if arg in _cache_data:
			ret = _cache_data[arg]
		else:
			ret = func(arg)
			_cache_data[arg] = ret
		return ret
	return wrapper
