class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        fs = ""
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        dsorted = dict(sorted(d.items(), key = lambda item: item[1], reverse = True))
        for i in dsorted:
            fs += i*dsorted[i]
        return fs