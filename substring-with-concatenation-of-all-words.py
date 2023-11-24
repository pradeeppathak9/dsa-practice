# https://leetcode.com/problems/substring-with-concatenation-of-all-words/


def solution(s, words):
    words_len = len(words[0])
    total_words = len(words)
    words_set = {}
    for word in words:
        words_set[word] = words_set.get(word, 0) + 1 
    print(words_set)
    

    res = []
    for i in range(len(s) - words_len*total_words + 1):
        matched = words_set.copy()
        words_matched = 0
        for j in range(i, i+ words_len*total_words, words_len):
            if s[j:j+words_len] in matched and matched[s[j:j+words_len]] > 0:
                matched[s[j:j+words_len]] -= 1
                words_matched += 1
            else:
                break
        if total_words == words_matched:
            res.append(i)
    return res


s = "barfoothefoobarman" 
words = ["foo","bar"]
print(solution(s, words))

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]
print(solution(s, words))

s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
print(solution(s, words))

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
print(solution(s, words))
