# 44'
class Solution:
	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		lesson = {}
		dep_list = []
		N = 0   	# class num
		res = True
		lesson_prere = {}
		lesson_map = {}

		if not prerequisites and numCourses > 0:
			res = False
			return res
		else:
			res = True
			return res
		
		# lesson summary
		lesson = set(prerequisites[0])
		for i in prerequisites[1:]:
			# 交并集
			lesson = lesson | set(i)

		N = len(lesson)
		if N != numCourses:
			res = False
			return res

		# build prereq list
		id = 0
		for i in lesson:
			lesson_map[i] = id
			dep_list.append([])
			for j in prerequisites:
				if i in j and i != j[0]:
					end = j.index(i)
					if lesson_prere:
						lesson_prere = lesson_prere | set(j[:(end+1)])
					else:
						set(j[:(end+1)])
			dep_list[id] = lesson_prere
			id += 1
			lesson_prere = {}

		# logic check
		id  = 0
		for i in lesson:
			for j in dep_list[id]:
				if i in dep_list[lesson_map[j]]:
					res = False
					return res
			id += 1

		return res			