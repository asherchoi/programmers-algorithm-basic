
def solution(n):
    return bin(n).count('1')


print(solution(5)) # 2
print(solution(6)) # 2
print(solution(5000)) # 5
