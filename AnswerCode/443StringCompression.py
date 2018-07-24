# 443. String Compression

class Solution(object):
	def compress(self, chars):
		if len(chars)<2: return len(chars)
		wpt = 0
		count = cpt =1
		word = chars[0]
		while cpt<=len(chars):
			if cpt==len(chars) or not chars[cpt]== chars[wpt]:
				if count==1:
					wpt +=1
				else:
					subs = str(count)
					chars[wpt+1:wpt+1+len(subs)] = [c for c in subs]
					wpt = wpt+1+len(subs)
				count = 1
				if cpt<len(chars):chars[wpt] = chars[cpt]
			else: count+=1
			cpt+=1
		return wpt
			
			
			
	
So = Solution()
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b","c","c","c"]
chars = ["a","b","c","c","c","d"]
print So.compress(chars)