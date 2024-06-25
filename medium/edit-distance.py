# https://leetcode.com/problems/edit-distance/

def solution(word1, word2, memo={}):
    i = 0
    while i < min(len(word1), len(word2)) and word1[i] == word2[i]:
        i+=1

    w1, w2 = word1[i:], word2[i:]
    if (w1, w2) in memo:
        return memo[(w1, w2)]
    
    if len(w1) == 0: 
        res = len(w2)
    elif len(w2) == 0: 
        res = len(w1) 
    else:
        res = 1 + min(
            # insert 
            solution(w2[0] + w1, w2, memo),        
            # delete
            solution(w1[1:], w2, memo),
            # replace
            solution(w2[0] + w1[1:], w2, memo)
        )
    memo[(w1, w2)] = res
    return res


word1 = "intention"
word2 = "execution"

assert solution(word1, word2) == 5

word1 = "horse"
word2 = "ros"

assert solution(word1, word2) == 3

word1 = "dinitrophenylhydrazine"
word2 = "acetylphenylhydrazine"

assert solution(word1, word2) == 6
print("Test Cases Successfull!")
