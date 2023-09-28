class Solution(object):
    def sortArrayByParity(self, nums):
        pares = []
        impares = []
        if (len(nums) == 0):
            return [0]
        else:
            for i in nums:
                if (i % 2) == 0:
                    pares.append(i)
                else:
                    impares.append(i)
        lista = pares + impares
        return lista