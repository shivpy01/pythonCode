def Anagram(word1,word2):
    count1 = 0
    count2 = 0
    for i in word1:
        if i not in word2 or word1.count(i)>word2.count(i):
            count1 += 1
            word1 = word1.replace(i,'',1)
    for j in word2:
        if j not in word1 or word2.count(j)>word1.count(j):
            count2 += 1
            word1 = word1.replace(j,'',1)
    return print(count1+count2)

Anagram("abcde","ancfe")
