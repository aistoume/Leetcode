# 690 Employee Importance
# Youbin Mo 11/26/2017

# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution(object):
	def getImportance(self, employees, id):
		dict = {}
		for Em in employees:
			dict[Em.id] = Em
		return self.getSubImp(dict,id)
	def getSubImp(self, dict, id):
		Imp = dict[id].importance
		if not (dict[id].subordinates):
			return Imp
		else:
			for k in dict[id].subordinates:
				Imp+= self.getSubImp(dict,k)
			return Imp
	
	
s = Solution()
inf = []
inf.append(Employee(1,5,[2,3]))
inf.append(Employee(2,3,[4]))
inf.append(Employee(3,4,[]))
inf.append(Employee(4,1,[]))
r = s.getImportance(inf, 1)
print r