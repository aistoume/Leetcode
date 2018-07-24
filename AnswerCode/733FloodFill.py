#733. Flood Fill


class Solution(object):
	def floodFill(self, image, sr, sc, newColor):
		stack = [(sr,sc)]
		visited = []
		neigh = ((-1,0),(1,0),(0,-1),(0,1))
		while stack:
			x,y = stack[0]
			if not stack[0] in visited:
				visited.append(stack[0])
			for r,c in neigh:
				if 0<=x+r<len(image) and 0<=y+c<len(image[0]) and not (x+r,y+c) in visited and image[x+r][y+c]==image[x][y]:
					stack.append((x+r,y+c))
			del stack[0]
		for x,y in visited:
			image[x][y] = newColor
		return image
	
	
image = [[1,1,1],[1,1,0],[1,0,1]]
sr,sc = 1, 1
newColor = 2

So = Solution()
print So.floodFill(image, sr,sc, newColor)