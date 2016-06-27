import argparse
from Modules.Headers import headers
from Modules.Cookies import cookies


class Crawl:

	def __init__(self):
		self.heads = headers()
		self.cookies = cookies()
		self.target = ""

	def pwn_heads(self):
		self.heads.get_heads(self.target)

	def pwn_cookies(self):
		self.cookies.get_cookies(self.target)


def main():

	crawl = Crawl()

	parser = argparse.ArgumentParser(description = "The program help")
	parser.add_argument("-u", help="The target URL")
	parser.add_argument("-c", help="Cookies from the target URL")
	args = parser.parse_args()

	if not args.u :
		print "\nNo URL specified."

	print " \n++++++++++++++++++++   Headers  ++++++++++++++++++++ \n"
	crawl.pwn_heads(args.u)
	print " \n++++++++++++++++++++   Cookies  ++++++++++++++++++++ \n"
	crawl.pwn_cookies(args.u)


	if not

if __name__ == '__main__':
	main()
