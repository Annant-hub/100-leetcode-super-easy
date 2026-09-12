class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        new_s=""
        for i in s:
            freq[i]=freq.get(i,0)+1
        sorted_freq=dict(sorted(freq.items(),key = lambda item:item[1], reverse=True))
        for key in sorted_freq:
            i=sorted_freq[key]
            new_s=new_s + key * i
        return new_s
        
