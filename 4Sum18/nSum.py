class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        num.sort()
        def ksum(num, k, target):
            i = 0
            result = set()
            if k == 2:
                j = len(num) - 1
                while i < j:
                    if num[i] + num[j] == target:
                        result.add((num[i], num[j]))
                        i += 1
                    elif num[i] + num[j] > target:
                        j -= 1
                    else:
                        i += 1
            else:
                while i < len(num) - k + 1:
                    newtarget = target - num[i]
                    subresult = ksum(num[i+1:], k - 1, newtarget)
                    if subresult:
                        result = result | set( (num[i],) + nr for nr in subresult)
                    i += 1
                
            return result
        
        return [list(t) for t in ksum(num, 4, target)]