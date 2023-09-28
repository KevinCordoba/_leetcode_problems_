class Solution(object):
    def decodeAtIndex(self, s, k):
        word = ""
        numbers = ["1","2","3","4","5","6","7","8","9"]
        for i in s:
            if (not(i in numbers)):
                word += i
            else:
                n = int(i)
                word *= n            
        return word
#ineficiente en memoria

