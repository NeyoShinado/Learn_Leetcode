class Solution:
	def searchMatrix(self, matrix, targer):
		"""
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #init
        res = False
        M = len(matrix)
        step = 1
        if M == 0:
        	return res
        if matrix[0]:
        	N = len(matrix[0])
        	if N == 0:
        		return res
        else:
        	return res

        # main_body diag search
        if M > N:
        	step = int(M/N)