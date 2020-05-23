class Solution:
	def isValid(self, s: str) -> bool:
		n = len(s)
		r_set = ')]}'
		#* changable str
		biase = 0
		# even check
		if n % 2 != 0:
			return False

		if n == 0:
			return True

		for i in range(1, n):
			# curren len
			m = len(s)
			id = i - biase
			#* specific l_r match
			if(s[id] in r_set and lr_match(s[id-1], s[id])):
				biase += 2
				if (id == 1):
					s = s[2:m]
				else:
					s = s[0:(id-1)] + s[(id+1):m]
			elif(s[id] in r_set and not lr_match(s[id-1], s[id])):
				return False

		if s:
			return False
		else:
			return True

def lr_match(l, r):
	if l == '(' and r == ')':
		return True
	if l == '{' and r == '}':
		return True
	if l == '[' and r == ']':
		return True

	return False
