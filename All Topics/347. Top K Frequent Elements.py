class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # result = {}    
        # for i in nums:
        #     if i in result:
        #         result[i] += 1
        #     else:
        #         result[i] = 1

        # final = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
        # return list(final.keys())[:k] 

        count = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for each_num in nums:
            count[each_num] = 1 + count.get(each_num, 0)

        for n,c in count.items():
            frequency[c].append(n)

        result = []
        for i in range(len(frequency)-1, 0, -1):
            for each_element in frequency[i]:
                result.append(each_element)
                if len(result) == k:
                    return result


        
