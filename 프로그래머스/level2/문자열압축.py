"""
예를 들어 abcdefghijk가 있다면,
n = 2일때, /ab/cd/ef/gh/ij/k 와 a/bc/de/fg/hi/jk/ 이런식으로 분리해서 이웃한 것이 같으면 붙인다
n = 3일때도, /abc/def/ghi/jk a/bcd/efg/hij/k ab/cde/fgh/ijk/
"""

def solution(s):
    answer = 0
    return answer