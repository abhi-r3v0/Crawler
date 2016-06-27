import requests 


class headers:
	def __init__(self):       
		pass

	def get_heads(self, target):
		r = requests.head(target)
		print(r.headers)
		return
