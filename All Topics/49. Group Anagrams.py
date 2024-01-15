from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for each_str in strs:
            chars = [0] * 26

            for each_char in each_str:
                chars[ord(each_char) - ord("a")] += 1

            result[tuple(chars)].append(each_str)
