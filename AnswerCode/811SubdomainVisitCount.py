class Solution(object):
	def subdomainVisits(self, cpdomains):
		Lib = {}
		for s in cpdomains:
			[n, addr] = s.split(' ')
			n = int(n)
			while addr.find('.')>0:
				if addr in Lib:
					Lib[addr] += n
				else:
					Lib[addr] = n
				addr = addr[(addr.find('.')+1):]
			if addr in Lib:
				Lib[addr] += n
			else:
				Lib[addr] = n
		result = []
		for key in Lib:
			result.append(str(Lib[key])+' '+key)
		return result
	
	
	
S = Solution()
Input = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print S.subdomainVisits(Input)