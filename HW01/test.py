class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowels_dict = {v: [] for v in vowels}  # 簡化字典結構
        
        # 遍歷字串，記錄每個母音的索引
        for idx, letter in enumerate(s):
            if letter in vowels:
                vowels_dict[letter].append(idx)
        
        # 用於存儲第一個和最後一個母音索引
        first = []
        last = []
        
        # 檢查母音的總狀態，計算每個母音的奇偶性
        def check_even_count(vowels_dict):
            for key, value in vowels_dict.items():
                if len(value) % 2 != 0:
                    return False
            return True
        
        # 遍歷每個母音，確保母音出現偶數次
        for key, value in vowels_dict.items():
            if len(value) % 2 != 0:  # 如果某母音出現奇數次
                target = vowels_dict[key]
                if len(target) >= 2:  # 確保有足夠的元素比較
                    left = abs(target[0] - target[-2])  # 比較兩邊的距離
                    right = abs(target[1] - target[-1])
                    
                    # 嘗試移除尾部，檢查是否導致其他母音奇數次
                    if left > right:
                        original = vowels_dict[key][:]  # 暫存原始索引
                        vowels_dict[key].pop(-1)  # 移除尾部
                        
                        # 移除後檢查是否其他母音保持偶數次
                        if not check_even_count(vowels_dict):
                            vowels_dict[key] = original  # 回退操作
                            vowels_dict[key].pop(0)  # 移除頭部
                    else:
                        original = vowels_dict[key][:]  # 暫存原始索引
                        vowels_dict[key].pop(0)  # 移除頭部
                        
                        # 移除後檢查是否其他母音保持偶數次
                        if not check_even_count(vowels_dict):
                            vowels_dict[key] = original  # 回退操作
                            vowels_dict[key].pop(-1)  # 移除尾部
            
            # 保留第一個和最後一個母音索引
            if vowels_dict[key]:  # 確保列表不為空
                first.append(vowels_dict[key][0])
                last.append(vowels_dict[key][-1])
        
        if not first or not last:  # 如果所有母音沒有出現，直接返回整個字串長度
            return len(s)
        
        # 找到第一個和最後一個母音之間的最長子串長度
        first.sort()
        last.sort()
        longest_length = last[-1] - first[0] + 1
        
        return longest_length

# 測試
s = 'eleetminicoworoep'
solution = Solution()
print(solution.findTheLongestSubstring(s))
