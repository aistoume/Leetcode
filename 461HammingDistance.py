### Youbin 2017/06/19
### 4610 Hamming Distance

def hammingDistance(self, x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    r = 0
    b = bin(x^y)
    for i in range(2,len(b)):
        r+= int(b[i])
    return r
