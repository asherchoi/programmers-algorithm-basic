'''
(1)
 어떤 임의의 수열 A={a1... an}에서 이 수들을 가지고 구간합 [1, S]까지의 수들을
모두 표현할 수 있다고 가정할 때, 이 수열에 S+1를 추가하면
수열 끝에 S+1이 추가된 수열 A(after)={a1. an, S+1}은
추가되지 않은 수열 A(before)={a1.. an}이 구간 [1, S]까지 표현이 가능하니까
1.. S까지 각각 S+1을 더한 [S+2, 2S+1]를 추가로 표현할 수 있게됨
따라서 [1, 2S+1]까지 수들을 누락없이 모두 표현이 가능해진다.


(2)
 그러면 이 수열A에 S+2를 추가할 경우를 살펴보면
수열끝에 S+2이 추가된 {a1.. an, S+2}은
수열 {a1.. an}이 구간 [1, S]까지 표현이 가능하니까
1.. S까지 각각 S+2을 더한 [S+3, 2S+2]를 추가로 표현할 수 있게됨
[1, S] + [S+2, S+2] + [S+3, 2S+2] == [1, 2S+2]는 거짓

반례) 구간[S+1]을 표현하지 못함.
      S+3을 추가할경우 [S+1, S+2] / S+4를 추가할 경우 [S+1, S+3]에 대해서
      계속 불만족되는 구간이 생김

따라서 수열 {a1, a2, ..an}이 구간합 S까지 표현을 할 수 있을때
S+1보다 큰 수를 수열에 넣으면 표현을 하지 못하는 구간이 생기게 되며
표현하지 못하는 최소구간은 S+1부터이다.
'''

def solution(weights):
    weights.sort()
    S = weights.pop(0)
    for w in weights:
        if w > S+1:
            break
        else:
            S += w
    return S+1

print(solution([3, 1, 6, 2, 7, 30, 1])) #21
print(solution([1, 1, 3])) #6
print(solution([1, 1, 1, 1, 1, 1])) #7
