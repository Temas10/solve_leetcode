class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        results = {}
        for word in strs:
            counts = [0] * 26                        # пока что пустой список для всех букв алфавита
            for char in word:
                counts[ord(char) - ord("a")] += 1    # ord() возвращает числовой код символа в Юникоде
            key = tuple(counts)
            if key not in results:
                results[key] = []
            results[key].append(word)    

        return list(results.values())