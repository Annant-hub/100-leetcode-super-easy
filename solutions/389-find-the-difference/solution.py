from collections import Counter
s= "ank"
j="anki"
count_s= Counter(s)
count_j= Counter(j)
print(count_s)
print(count_j)
for i in count_j:
    if count_j[i]>count_i[i]:
        print(i)
