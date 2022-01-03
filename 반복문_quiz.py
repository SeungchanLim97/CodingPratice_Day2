# Quiz) 당신은 cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건 1: 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건 2: 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

## my answer
# from random import *
# seq = 0

# for i in range(1, 51):
#     travelTime = randint(5, 51)
#     seq += 1
#     print("{}째 손님 (소요시간 :{}분)".format(seq, travelTime))


## answer
from random import *
cnt = 0 # 총 탑승 승객 수
for i in range(1, 51): # 1 ~ 50이라는 수 (승객)
    time = randrange(5, 51) # 5분 ~ 50분 소요 시간
    if 5 <= time <= 15: # 5분 ~ 15분 이내의 손님 (매칠성공), 탑승 승객 수 증가 처리
        print("[0] {0} 째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else: # 매칭 실패
        print("[] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0} 분".format(cnt))