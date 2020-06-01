class Solution:
	def hammingDistance(self, x:int, y: int) -> int:
		# init
		res = 0
		xstr = bin(x)[2:]
		ystr = bin(y)[2:]

		Nx = len(xstr)
		Ny = len(ystr)

		if Nx > Ny:
			ystr = '0' * (Nx-Ny) + ystr
		else:
			xstr = '0' * (Ny-Nx) + xstr

		for i in range(len(xstr)):
			res += abs(int(xstr[i]) - int(ystr[i]))

		return res