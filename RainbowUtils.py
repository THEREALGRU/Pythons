class RainbowUtils():

	def reduct(self, inp, cut):
        	return inp[:-int(cut)]

	def md5(self,string):
		import hashlib
		h = hashlib.md5(str(string).encode()).hexdigest()
		return str(h)

	def chain(self,reduced,end,string):
		try:
			reduced = int(reduced)
			end = int(end)

		except ValueError:
			return "red / end must be a integer"
		string = str(string)
		for p in range(end):
			if string == '' or "":
				break
			
			string = str(reduct(string,reduced))
			
