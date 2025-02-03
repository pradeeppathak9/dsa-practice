def solution(s):
  res = 0
  last = 0
  for i in range(len(s)):
      if s[i] == '+':
          res += last
          last = 0
      elif s[i] == '*':
          last *= int(s[i+1])
      else:
          if last == 0:
              last = int(s[i])
  res += last
  return res

s = '4+2*3+6*2'
print(solution(s))

