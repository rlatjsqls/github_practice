'''

중복된 원소 가능
원소에 순서가 있다  -> 같은 수라도 배열이 다르면 다른 튜플
원소의 개수는 유한하다

중복이 없는 튜플이 주어질때..

특정 튜플을 표현하는 집합이 담긴 문자열 s 가 매개변수로 주어질때, s가 표현하는 튜플을 배열에 담아 return

순서가 있기때문에
1개자리 - 2개짜리에서 제외한 나머지 -> 3개에서 제외한 나머지...
'''

def solution(s):

    s = s.replace('{{','').replace('}}','')
    num = s.split('},{')

    num = [set(map(int, i.split(','))) for i in num]
    num.sort()
    res = [list(num[0])]

    for i in range(1, len(num)):
        res.append(list(num[i]-num[i-1]))
    answer = [i[0] for i in res]
    return answer


print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
