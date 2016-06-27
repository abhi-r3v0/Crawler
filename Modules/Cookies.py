import requests 


class cookies:

	def __init__(self):
		pass

	def get_cookies(self,target):
		session = requests.Session()
		session.cookies.get_dict() { }

		response = session.get(self, target)
		return
