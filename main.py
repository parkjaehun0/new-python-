import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
import csv

# ex79)
# C: C# ASP.NET
# Java: JSP
# Python: Django

# import django
# print(django.get_version())            # 3.2.6
# django-admin startproject pn01
# + pythonProject001
#    + pn01
#       +pn01
#         __init__.py
#         asgi.py
#         setting.py
#         urls.py
#         wsgi.py
#       manage.py






"""
# ex78)
# 행정 안전부 >> 정책자료 >> 통계 >> 주민등록 인구통계 >> csv파일 다운
# >> 적절하게 파일명을 변경하고 >> 메모장에서 다른이름으로 저장 >> utf-8로 재 저장
# >> 프로잭트에 복사 혹은 드레그


# 1)
f = open('202107_202107.csv', 'r', encoding='utf-8')
lines = csv.reader(f)
# 1줄만 읽었다.
header = next(lines)

# 나머지 줄을 읽을 것이다.
list_data= []
for x in lines:
    list_data.append(x)
f.close()

# 2-1) header에 대한 정보 출력
print(header)
for x in header:
    print(x)
print(end='\n\n')

# 2-2) list_data 대한 정보 출력
for x in list_data:
    print(x)
print(end='\n\n')

# 3)
# 경우1) 리스트 >> 딕셔너리 >> DataFrame
# 경우2) 리스트 >>   (x)   >> DataFrame
# 경우3)  (x)  >> 딕셔너리 >> DataFrame

# 3-1) 문법 설명
k = ['key0', 'key1', 'key2']
v = [10, 20, 30]
result = dict(zip(k, v))
# 최종 결과는 2개의 리스트의 딕셔너리로 생성
print(result, end='\n\n')

# 3-2)
k = ['key0', 'key1', 'key2']
# 위의 list_data와 동일한 구조를 가지고있다.
v = [
    [1, 2, 3],    # key0
    [4, 5, 6],    # key1
    [7, 8, 9],    # key2
    [9, 7, 8]
]

result = dict(zip(k, v))
# 비스무리하게 나오기는 했지만, 내가 원하는 결과가 아니다.
# 실제 원하는 결과는
# {
#     'key0': [1, 4, 7, 9],
#     'key1': [2, 5, 8, 7],
#     'key2': [3, 6, 9, 8]
#
# }
print(result, end='\n\n')

# 여기서 전치를 시킨다.
v = np.array(v).T
print(v)

# 딕셔너리로 변경
result = dict(zip(k, v))
print(result, end='\n\n')

# 3-3)
k = ['이름', '나이', '급여']
v = [['호랑이', 10, 2000],
     ['독수리', 20, 3000],
     ['코끼리', 30, 4000],
     ['앵무새', 40, 5000]]
v = np.array(v).T
result = dict(zip(k, v))
print(result, end='\n\n')

# 판다스로 변경
df = pd.DataFrame(result)
print(df, end='\n\n')

# 3-4) list_data를 판다스로 변경
list_data = np.array(list_data).T
result = dict(zip(header, list_data))
df = pd.DataFrame(result)
print(df, end='\n\n')

# 3-5) 컬럼명 변경
df.columns = ['구역', '인구', '세대수', '세대당 인구', '남자수', '여자수', '비율']
print(df, end='\n\n')
print(df.head(3), end='\n\n')
print(df.loc[1])

# 4) 판다스의 인구데이터의 콤마를 제거
df['인구'] = df['인구'].apply(lambda x: x.replace(',', ''))
print(df.loc[1], end='\n\n')

# 출력 참고
print(df.iloc[:, 0:2])

# 5)
result = df.sort_values(by=['인구'], ascending=False)
print(result.iloc[:, 0:2])

# 왜 정렬이 안되었다.
# 인구 컬럼은 object타입이다. 숫자 타입이 아니다.
print(df['인구'].dtype)

# 컬럼의 타입 변경
df['인구'] = pd.to_numeric(df['인구'])
print(df['인구'].dtype)

result = df.sort_values(by=['인구'], ascending=False)
print(result.iloc[:, 0:2])

# 6) 전국 레코드 삭제
result = result.drop(0)
print(result.iloc[:, 0:2], end='\n\n')

# 7) 전체 인구수 합을 구한다.
print(result['인구'].sum())

# 8) 시각화
from matplotlib import rc
rc('font', family='Malgun Gothic')
result.plot.bar(rot=0)
plt.show()
"""


"""
# ex77)
# 1)
a = [
    {'이름': '1길동', '주소': '서울', '성별': '남'},
    {'이름': '2길동', '주소': '부산', '성별': '남'},
    {'이름': '3길동', '주소': '부산', '성별': '여'},
    {'이름': '4길동', '주소': '서울', '성별': '남'},
    {'이름': '5길동', '주소': '부산', '성별': '여'},
    {'이름': '6길동', '주소': '부산', '성별': '여'},
    {'이름': '7길동', '주소': '부산', '성별': '남'},
    {'이름': '8길동', '주소': '서울', '성별': '여'},
    {'이름': '9길동', '주소': '부산', '성별': '남'}
]

print(a)
# 첫 데이터
print(a[0])
# 마지막 데이터
print(a[len(a)-1], end='\n\n')

# 2)
df = pd.DataFrame(a)
print(df, end='\n\n')

# 3)
result = df.groupby(['주소', '성별']).size().unstack()
print(result)

# 4) 시각화
from matplotlib import rc
rc('font', family='Malgun Gothic')
result.plot.bar(rot=0)
plt.show()
"""


"""
# ex76)
# 1) 로딩
# 2)
a = [
    {'이름': '1길동', '주소': ''},      # 값이 없는 경우
    {'이름': '2길동', '주소': '부산'},
    {'이름': '3길동'},                 # 아예 키가 없다
    {'이름': '4길동', '주소': '서울'},
    {'이름': '5길동', '주소': '부산'},
    {'이름': '6길동'},                 # 아예 키가 없다
    {'이름': '7길동', '주소': '부산'},
    {'이름': '8길동', '주소': '서울'},
    {'이름': '9길동', '주소': ''}       # 값이 없는 경우
]
print(a)
# 첫 데이터
print(a[0])
# 마지막 데이터
print(a[len(a)-1], end='\n\n')

# 3)
# 문법 확인
# print(a[1]['주소'])
# a[2]['주소'] = '불명'
# print(a[2]['주소'])
for index, v in enumerate(a):
    # print(k, v)
    if '주소' not in v:
        a[index]['주소'] = '불명'

for x in a:
    print(x)
print(end='\n\n')

# 4)
# 3번에서 처리 해도 되지만 편의성 여기서 처리한다.
# 주소키는 있지만 값이 없는 경우를 처리한다.
for index, v in enumerate(a):
    if a[index]['주소'] == '':
        a[index]['주소'] = '불명'

for x in a:
    print(x)
print(end='\n\n')

# 5)
df = pd.DataFrame(a)
print(df)

# 6) 카운팅
result = df['주소'].value_counts()
print(result)

# 7) 시각화
from matplotlib import rc
rc('font', family='Malgun Gothic')
result.plot.bar(rot=0)
plt.show()
"""


"""
# ex75) 키가 없는 경우
# 1) 파일 로딩
# 2)
a = [
    {'이름': '1길동', '주소': '서울'},
    {'이름': '2길동', '주소': '부산'},
    {'이름': '3길동'},
    {'이름': '4길동', '주소': '서울'},
    {'이름': '5길동', '주소': '부산'},
    {'이름': '6길동'},
    {'이름': '7길동', '주소': '부산'},
    {'이름': '8길동', '주소': '서울'},
    {'이름': '9길동', '주소': '부산'}
]
print(a)
# 첫 데이터
print(a[0])
# 마지막 데이터
print(a[len(a)-1], end='\n\n')

# 3)
# 이코드는 에러 발생
# address = [rec['주소'] for rec in a]

# 수정 코드
address = [rec['주소'] for rec in a if '주소' in rec]
print(address)

# 4)
df = pd.Series(address)
result = df.value_counts()
print(result)

# 5) 시각화
from matplotlib import rc
rc('font', family='Malgun Gothic')

result.plot.bar(rot=0)
plt.show()
"""


"""
# ex74) 73번을 다른 방식으로 프로그램
# 1) 파일 로딩
# 2)
a = [
    {'이름': '1길동', '주소': '서울'},
    {'이름': '2길동', '주소': '부산'},
    {'이름': '3길동', '주소': '부산'},
    {'이름': '4길동', '주소': '서울'},
    {'이름': '5길동', '주소': '부산'},
    {'이름': '6길동', '주소': '부산'},
    {'이름': '7길동', '주소': '부산'},
    {'이름': '8길동', '주소': '서울'},
    {'이름': '9길동', '주소': '부산'}
]

print(a)
# 첫 데이터
print(a[0])
# 마지막 데이터
print(a[len(a)-1], end='\n\n')

# 3) 리스트안에있는 딕셔너리를 >> 판다스로 만든다.
df = pd.DataFrame(a)
print(df, end='\n\n')

result = df['주소'].value_counts()
print(result, type(result), end='\n\n')

from matplotlib import rc
rc('font', family='Malgun Gothic')

result.plot.bar(rot=0)
plt.show()
"""


"""
# ex73)
# JSON 데이터 형식을 딕셔너리로 읽어 들인다.
# 직역별 카운팅을 한다.
# 시각화 플롯을 한다.

# 1) json 데이터 파일 로딩
# json 파일은 더블코테이션으로 묶어 있어야한다.
# 첫라인에 공백혹은 줄바꿈이 있으면 안된다.
import json

# a = [json.loads(line)for line in open('Jsondata.txt', encoding='utf-8')]
# print(a)
# # 첫 데이터
# print(a[0])
# # 마지막 데이터
# print(a[len(a)-1], end='\n\n')

# 2) 보면서 하기 편하게 복사를 해서
# 콤마를 붙이고 "을 '으로 리플레이스 한다.
a = [
    {'이름': '1길동', '주소': '서울'},
    {'이름': '2길동', '주소': '부산'},
    {'이름': '3길동', '주소': '부산'},
    {'이름': '4길동', '주소': '서울'},
    {'이름': '5길동', '주소': '부산'},
    {'이름': '6길동', '주소': '부산'},
    {'이름': '7길동', '주소': '부산'},
    {'이름': '8길동', '주소': '서울'},
    {'이름': '9길동', '주소': '부산'}
]

print(a)
# 첫 데이터
print(a[0])
# 마지막 데이터
print(a[len(a)-1], end='\n\n')

# 3) 주소만 리스트로 생성
# print([rec for rec in a])
# print([rec['주소'] for rec in a])
address = ([rec['주소'] for rec in a])
print(address)

# 4) 카운팅 한다.
# 복습 문법 확인1
if 2 in [1, 2, 3, 4]:
    print(1000)
else:
    print(2000)

# 윗 코드와 동일
print(1000 if 2 in [1, 2, 3, 4] else 2000)

# in 뒤에 리스트가 아니고 딕셔너리일때는 해당키가 있는지 확인
print(888 if 'key1' in {'key1': 10, 'key2': 20} else 999)
print(888 if 'key3' in {'key1': 10, 'key2': 20} else 999)
print(888 if 333 in {333: 10, 444: 20} else 999)
print(888 if 555 in {333: 10, 444: 20} else 999)

# 복습 문법 확인2
result = {'a': 10}
result['a'] = 20
print(result)

result['b'] = 30
print(result)

# 이제 카운팅을 한다.
# 이 방법 말고 다른 방법으로 카운팅 할수 있지만
# 아주 순수하게 작성했을때의  코드이다.
result = {}
for x in address:
    if x in result:   # 키가 있는지 확인하는것이다.
        result[x] += 1
    else:
        result[x] = 1

# 최종 결과는 딕셔너리 이다.
print(result, end='\n\n')

# series
# 5) 딕셔너리를 판다스의 시리즈로 바꾼다.
result1 = pd.Series(result)
print(result1, end='\n\n')

# 문법 확인
a = pd.Series([10, 20, 30, 40])
# 반시계 방향으로 각도값을 설정
a.plot.bar(rot=0)
plt.show()

# 시각화
from matplotlib import rc
rc('font', family='Malgun Gothic')

result1.plot.bar(rot=0)
plt.show()
"""


"""
# ex72)
# 학교명 학과수 학생수 교수수 컴럼을 가지는 파일 생성(csv)
# csv 파일을 읽어서 총합을 구한다.
# 구한 총합의 결과를 넘파이의 마지막 항에 추가
# 넘파이를 판다스 변환한다.

# 1) cvs파일 생성
# f = open('sample03.csv', 'w', encoding='utf-8', newline='')
# line = csv.writer(f)
#
# line.writerow(['학교명', '학과수', '학생수', '교수수'])
# line.writerow(['A대학', 59, 2140, 14])
# line.writerow(['B대학', 90, 4140, 53])
# line.writerow(['C대학', 49, 3140, 25])
# line.writerow(['D대학', 40, 5540, 13])
# line.writerow(['E대학', 42, 2340, 98])
#
# f.close()
# print('출력 파일을 확인하세요')

# 2) 파일 리딩
f = open('sample03.csv', 'r', encoding='utf-8')
lines = csv.reader(f)
header = next(lines)
print(header)

data = []
for line in lines:
    data.append(line)

f.close()

# 출력 코드
for x in data:
    print(x)
print()

# 3) 리스트 >> 넘파이로 변환
data1 = np.array(data)
print(data1, end='\n\n')

# 4) 넘파이의 열(수직)을 삭제
# axis = 0 : 수직, axis = 1 : 수평
# 인덱스를 수평방향으로 해석하세요.
data2 = np.delete(data1, 0, axis=1)
print(data2, end='\n\n')

# 5) 넘파이의 문자열을 >> 숫자로 변환
data3 = data2.astype(np.int32)
print('data3')
print(data3, end='\n\n')

# 6) 합산을 구한다.(수직방향으로 더할것이다.)
data4 = np.sum(data3, axis=0)
print(type(data4))
print('data4')
print(data4, end='\n\n')

# 7) 2차원 넘파이의 1차원 넘파이를 추가
# (dest, position, src)
data5 = np.insert(data3, len(data3), data4, axis=0)
print('data5')
print(data5, end='\n\n')

# 8) 넘파이를 판다스로 변환
# dataframe = pd.DataFrame(data5, columns=['호', '랑', '이'])
dataframe = pd.DataFrame(data5, columns=header[1:])
print(dataframe)
"""


"""
# ex71)
# 1. 기본 형태(title, xticks, yticks, xlabel, ylabel)
# plt.bar([1, 2, 3], [2, 3, 1])
# plt.show()

# 2. 수평 바(bar + horizontal)
# plt.barh([1, 2, 3], [2, 3, 1])
# plt.show()

# 3. align(정렬), alpha(투명도)
# x = ['python', 'C++', 'Java', 'perl', 'Scale', 'Lisp']
# y = [10, 8, 6, 4, 2, 1]
#
# [center, edge]
# plt.bar(x, y, align='center', alpha=0.8)
# plt.show()

# 4.
# plt.bar([0, 1, 2, 3], [90, 55, 40, 65], width=0.3)
# plt.show()

# 5.
# 이 코드는 성립하지 않는다.
# a = [0, 1, 2, 3]
# a = a + 0.35
# print(a)

# 이 코드는 성립하지 않는다.
# a = range(4)
# print(type(a))
# a = a + 0.35
# print(a)

# 이코드는 성립된다.
# a = np.arange(4)
# a = a + 0.35
# print(a)

# a bar: (+)를 기준점이다. 0.4 / 2 = 좌우 각각의 너비
# plt.bar(np.arange(4)+0.0, [90, 55, 40, 65], 0.4)   # width=0.4
# plt.bar(np.arange(4)+0.2, [65, 40, 55, 95], 0.4)
# plt.show()

# plt.bar(np.arange(4), [90, 55, 40, 65], 0.4, color='r', label='tgier')
# plt.bar(np.arange(4), [65, 40, 55, 95], 0.4, color='g', label='lion')
# plt.legend()
# plt.show()

# bar를 사용하는 예(*** 별)
# 나이대별      월급
# 학과별        경쟁률
# 월별          수익률
# 축구팀별       성적
# 동물원별       사자, 호랑이 개체수
# 나라별         남자, 여자   인구수
"""


"""
# ex70)
# 1) 제목 설정
# plt.title('plot')
# plt.show()

# 2) 격자 설정
# plt.grid(True)
# plt.show()

# 3) 리스트 1개 사용할때( y측으로 설정된다.)
# plt.plot([1, 4, 9, 16])
# plt.show()

# 4) 리스트 2개 사용할때(x, y 순서로 설정된다.)
# plt.plot([10, 20, 30, 40], [1, 4, 9, 16])
# plt.show()

# 5) 라벨 설정
# plt.plot([10, 20, 30, 40], [1, 4, 9, 16])
# plt.xlabel('dog')
# plt.ylabel('cat')
# plt.show()

# 6) 1개 이상의 선을 그린다.(홀드)
# plt.plot([10, 20, 30, 40], [1, 4, 9, 16])
# plt.plot([10, 20, 30, 40], [4, 9, 16, 25])
# plt.show()

# 7) 칼라 설정
# (r)ed, (g)reen, (b)lue
# plt.plot(range(1, 5), 'r')
# plt.plot(range(2, 6), 'g')
# plt.plot(range(3, 7), 'b')
# plt.plot(range(4, 8), 'c')
# plt.plot(range(5, 9), 'm')
# plt.plot(range(6, 10), 'y')
# plt.plot(range(7, 11), 'k')
# plt.plot(range(8, 12), 'w')
# plt.show()

# 8) 마커 설정
# a = '.,ov^<>w1234sp*hH+xDd'
# for k, v in enumerate(a):
#     plt.plot(range(1+k, 5+k), '-')
# plt.show()

# 9) 선 스타일
# plt.plot(range(1, 5), '-')
# plt.plot(range(2, 6), '--')
# plt.plot(range(3, 7), '-.')
# plt.plot(range(4, 8), ':')
# plt.show()

# 10) '색상, 마커, 선스타일'
# plt.plot(range(1, 5), 'rH--')
# plt.show()

# 11) 선, 마크, 색상, 세부 설정
# plt.plot(
#     [10, 20, 30, 40],    # x축 설정
#     [1, 4, 9, 19],       # y축 설정
#     c='b',               # 선 색상
#     lw=5,                # 선 굵기
#     ls='--',             # 선 스타일
#     marker='^',          # 마크 설정
#     ms=15,               # 마크 크기
#     mec='g',             # 마크 외관 선 색상
#     mew=2,               # 마크 외관 선 굵기
#     mfc='r'              # 마크 내부 색상
# )
# plt.show()

# 12) 그리기를 할 전체 범위 설정
# plt.plot([10, 20, 30, 40], [1, 4, 9, 16])
# plt.xlim(0, 50)
# plt.ylim(-10, 30)
# plt.show()

# 13) 눈금자 설정
# plt.plot([1, 3, 5, 8], [10, 50, 30, 90])
# plt.xticks(range(0, 10))
# plt.yticks(range(0, 100, 10))
# plt.show()

# 14) legend(범레)
# 2    9    1
# 6    10   7(5)
# 3    8    4             # 범레 위치
# plt.plot([10, 20, 30, 40], [1, 4, 9, 16], label='tiger')
# plt.plot([10, 20, 30, 40], [16, 9, 4, 1], label='lion')
# plt.legend(loc=1)
# plt.show()

# 15) 배경 색상 변경
# plt.gca().set_facecolor([0.9, 0.9, 0.9])
# plt.show()

# 16) 출력창 크기 변경
# 640 * 480
# 800 * 600
# 1024 * 760
# plt.figure(figsize=(10.24, 7.6))    # 디폴트 값이다
# plt.plot()
# plt.show()

# 17) 한글 사용
# from matplotlib import rc
# rc('font', family='Malgun Gothic')
# font1 = {'size': 17, 'color': 'green'}
# font2 = {'size': 36, 'color': 'red'}
# plt.plot(['호랑이', '코끼리', '독수리'], [90, 40, 70])
# plt.title('성적', fontdict=font2)
# plt.show()

# 18) n개의 플롯 설정
# a = [1, 2, 3, 4]
# b = [30, 40, 10, 20]
# plt.figure()
# 세로개수, 가로개수, 위치
# 번호의 위치 
# 1 2 3
# 4 5 6
# plt.subplot(2, 3, 3)
# plt.plot(a, b)
#
# plt.subplot(2, 3, 1)
# plt.plot(a, b)
#
# plt.subplot(2, 3, 5)
# plt.plot(a, b)
# plt.show()

# 19) 특정 위치에0 텍스트 출력
# plt.text(2.0, 3.0, 'tiger')
# plt.text(1.0, 3.0, 'lion')
# plt.plot([1, 2, 3, 4])
# plt.show()

# 20)
# age = [10, 20, 30, 40, 50, 60]
# weight = [20, 40, 55, 50, 70, 60]
# height = [100, 120, 140, 150, 170, 165]
# plt.plot(age, weight, 'r')
# plt.twinx()
# plt.plot(age, height, 'g')
# plt.show()

# 21) 그래프 저장
# plt.plot([10, 20, 30])
# fig = plt.gcf()
# plt.show()
# fig.savefig('test.png')
"""


"""
# ex69) 
# plot(그래프를 그린다)의 종류
# 1. line plot
# 2. bar chart
# 3. histogram
# 4. scatter plot   
# 5. contour plot
# 6. surface plot
# 7. box plot
# 8. pi plot
"""

"""
# ex68) import하는 3가지 방법
# 1)
# import matplotlib.pyplot
# matplotlib.pyplot.plot()
# matplotlib.pyplot.show()

# 2)
# from matplotlib.pyplot import *
# plot()
# show()

# 3) 많은 사람이 이용하는 방법
import matplotlib.pyplot as plt
plt.plot()
plt.show()
"""


"""
# ex67)
print('ex 1')
data = {
    '학교명': ['A대학', 'B대학', 'C대학', 'D대학', 'E대학'],
    '학급수': [25, 23, 15, 19, 10],
    '학생수': [620, 600, 550, 580, 400],
    '교사수': [20, 30, 10, 90, 55]
}
df = pd.DataFrame(data)
print(df, end='\n\n')

print('ex 2')
a = df.iloc[0, 0]
print(a)
a = df.iloc[0, 3]
print(a)
a = df.iloc[4, 0]
print(a)

# 세로 범위, 가로범위
a = df.iloc[:, 1:]
print(a)
"""

"""
# ex66)
print('ex 1')   # 빈 데이터프래임 생성
df = pd.DataFrame(columns=('이름', '나이', '고향'))
print(df, end='\n\n')
print(len(df))

print('ex 2')   # 추가되는 데이터 1개 1개를 레코드라고 한다.
df.loc[20] = ['이순신', 10, '대전']
df.loc[30] = ['홍길동', 20, '서울']
# df.loc['키'] = ['앵무새', '20', '서울']
# 데이터 갱신에 해당한다.
df.loc[10] = ['독수리', 30, '마산']
print(df, end='\n\n')

print('ex 3')
for x in range(6):
    df.loc[len(df)] = [
        '코끼리' + str(x),
        np.random.randint(10, 40),
        '서울' + str(x * x)
    ]
print(df, end='\n\n')

print('ex 4')   # 갱신
df.loc[4] = ['앵무새', 99, '제주도']
print(df, end='\n\n')

print('ex 5')   # 삭제
# 주의 : 리턴값을 받아서 갱신해야 한다.
df = df.drop([5])
print(df, end='\n\n')

df = df.drop([30, 4 ,7])
print(df, end='\n\n')

print('ex 6')   # 1개 검색
print(df.loc[3], end='\n\n')
print(type(df.loc[3]))

print('ex 7')   # 연속 검색
# loc를 사용하지 않는다.
print(df[1:3], end='\n\n')

print('ex 8')
for x in range(20):
    df.loc[len(df)] = [
        '코끼리' + str(x),
        np.random.randint(10, 40),
        '서울' + str(x * x)
    ]
print(df, end='\n\n')

# viewing
print(df.head(), end='\n\n')  # 맨앞에 5개
print(df.tail(), end='\n\n')  # 맨뒤에 5개
print(df.head(2))
print(df.tail(3))
"""


"""
# ex65)
# 2차원의 자료구조 : DataFrame
print('ex 1') # 딕셔너리를 이용한 데이터프래임 생성
a = {
    '이름': ['호랑이', '코끼리', '독수리'],
    '나이': [20, 30, 40],
    '급여': [4000, 5000, 6000]
}

df = pd.DataFrame(a)
print(df)
print(type(df), end='\n\n')
# 결과
#     이름  나이    급여
# 0  호랑이  20  4000
# 1  코끼리  30  5000
# 2  독수리  40  6000
# <class 'pandas.core.frame.DataFrame'>

print('ex 2-1')   # 리스트를 이용한 데이터프레임 생성
a = [['호랑이', '코끼리', '독수리'],
     [20, 30, 40],
     [4000, 5000, 6000]]

df = pd.DataFrame(a)
print(df, end='\n\n')

print('ex 2-2')   # 1번 예제와 동일하게 변경
a = [['호랑이', 20, 4000],
     ['코끼리', 30, 5000],
     ['독수리', 40, 6000]]

df = pd.DataFrame(a)
print(df, end='\n\n')

print('ex 2-3')
a = [['호랑이', '코끼리', '독수리'],
     [20, 30, 40],
     [4000, 5000, 6000]]

df = pd.DataFrame(a).T  # .T가 2-3번을 2-2번처럼 바꾸다.
print(df, end='\n\n')

print('ex 3')
a = [['호랑이', '코끼리', '독수리'],
     [20, 30, 40],
     [4000, 5000, 6000]]

df = pd.DataFrame(a).T
df.columns = ['이름', '나이', '급여']
print(df, end='\n\n')
"""


"""
import pandas as pd
# list[[][]] numpy : 2차원배열: 행렬  pandas(database)
# ex64)
import pandas as pd

# 1차원의 자료구조 : Series
# 2차원의 자료구조 : DataFrame

print('ex 1')
# 리스트로 데이터를 초기화
a = pd.Series([10, 20, 30, 40])
print(a)
print(type(a), end='\n\n')

# 결과
# 0    10
# 1    20
# 2    30
# 3    40
# dtype: int64
# <class 'pandas.core.series.Series'>

print('ex 2-1')
a = pd.Series([10, 20, 30, 40])
# 리턴값이 넘파이
print(a.values, end='\n\n')

# 결과 : [10 20 30 40] # 콤마가 빠졌다.

print('ex 2-2')
# 리턴값은 리스트
b = list(a)
print(b)
print(type(b))
print()
# 결과: [10, 20, 30, 40]

print('ex 3')
print(a.index, end='\n\n')
# 결과 : RangeIndex(start=0, stop=4, step=1)

print('ex 4')
print(a[0], a[1], a[2], a[3], end='\n\n')
# 결과 : 10 20 30 40

print('ex 5') # for문을 이용한 반복
for x in a:
    print(x, end=' ')
print('\n')
# 결과: 10 20 30 40

print('ex 6') # enumerate를 이용한 반복
for k, v in enumerate(a):
    print(k, v)
print()
# 결과:
# 0 10
# 1 20
# 2 30
# 3 40

print('ex 7')
for k, v in a.items():
    print(k, v)
print()
# 결과:
# 0 10
# 1 20
# 2 30
# 3 40

print('ex 8')
a = pd.Series([10, 20, 30, 40], index=['A', 'B', 'C', 'D'])
print(a)
# 결과 :
# A    10
# B    20
# C    30
# D    40
# dtype: int64
print(a['A'], a['B'], a['C'], a['D'], end='\n\n')
# 결과 : 10 20 30 40

print('ex 9')
a = {
    '이름': '홍길동',
    '나이': 20,
    '급여': 4000
}
# dict >> Series
b = pd.Series(a)
print(b)

# Series >> dict
c = dict(b)
print(c)
"""


"""
# ex63) 내장함수
# 1) id(), type()

# 2) abs
print(abs(10), abs(-10))

# 3) enumerate
for key, value in enumerate([10, 20, 30]):
    print(key, value)

# 4) eval(evaluation:실행 이라는 뜻으 가지고 있다.)
# 문자열안에 코드가 있을때 그 코드를 실행시킬때 사용한다.
# eval >> 뭔지는 몰라도 위험하다. 가급적 사용하지 말자.
a = 'print(10 + 20)'
print(a)         # print(10 + 20)
eval(a)          # 30

# 5) min, max
print(min(10, 20))
print(min(10, 20, 30, 40))
print(min([10, 20, 30, 40]))

# 6) 2진수:bin 16진수:hex 8진수: oct
print(bin(100))     # 0b1100100
print(hex(100))     # 0x64
print(oct(100))     # 0o144

print(0b1100100)    # 100
print(0x64)         # 100
print(0o144)        # 100

# 7)
int('123')  # 문자열 >> 정수
str(123)    # 정수 >> 문자열
a = list('호랑이')  # 문자열 >> 리스트
print(a)
a = list(range(4))
print(a)

# 8) ASCII
print(chr(65))   # 정수를 >> ASCII
print(ord('B'))  # ASCII >> 정수

# 9-1) 몫과 나머지를 구한다.
a, b = 10, 3
print(a//b, a % b)

# 9-2) 내장함수를 이용해서 구한다.
a = divmod(10, 3)
print(a, type(a))

# 10-1) all: 모두 참일때 True 리턴
print(all([False, False]))
print(all([False, True]))
print(all([True, False]))
print(all([True, True]))
print(all([True, True, True, True, True, True, True, True]))

# 10-2) any: 1개라도 참일때 True 리턴
print(any([False, False, False, False, False, False]))
print(any([False, False, True, False, False, False]))

# 11-1)
# 내장함수가 아니다.
# 정렬이후에 a자신의 리스트 데이타가 갱신되었다.
a = [4, 3, 2, 1, 2, 3, 4]
a.sort()
print(a)    # [1, 2, 2, 3, 3, 4, 4]

# 11-2)
# 내장함수로 정렬하면 리시트 값 자체는 변경되지 않는다.
a = [4, 3, 2, 1, 2, 3, 4]
sorted(a)
print(a)

b = sorted(a)
print(b)

# 12-1)
# 외장함수는 import를 사용해야 한다.
# ex) math, numpy
import time
for x in range(5):
    print(x)
    # 여기서 1은 1초이다
    # time.sleep(1)

# 12-2) time 이용
a = time.localtime(time.time())
print(a)
print(a.tm_year, '년')
print(a.tm_mon, '월')
print(a.tm_mday, '일')
print(a.tm_hour, '시')
print(a.tm_min, '분')
print(a.tm_sec, '초')

b = ['월', '화', '수', '목', '금', '토', '일']
print(b[a.tm_wday], '요일')

# 12-3
import datetime
print(datetime.datetime.now())
"""


"""
# ex62) switch의 대안으로 딕셔너리를 이용한다.
# 1)
a = {'n1': 50, 'n2': '호랑이', 'n3': True}
print(a.get('n1'))
# 키값을 찾지 못했을때 99를 출력
print(a.get('n4', 99))

# 2)
def func(num):
    a = {
        10: '호랑이1',
        20: '호랑이2',
        30: '호랑이3',
    }.get(num, '앵무새')
    print(a)


func(10)
func(40)



# 3)
def f1():
    print('구구단 프로그램')


def f2():
    print('합산 프로그램')


def f3():
    print('우박수 프로그램')

# 사용 방법 1
def func1(num):
    a = {
        10: f1,
        20: f2,
        30: f3
    }

    a[num]()

func1(20)
print('-' * 40)
# 사용방법 2
def func2(num):
    {
        10: f1,
        20: f2,
        30: f3
    }.get(num)()
func2(20)
"""


"""
# ex61) 딕셔너리(dictionary), JSON
# 1)
a = {'n1': 50, 'n2': '호랑이', 'n3': True}
print(a['n1'])
print(a.get('n2'))

# 2)
a = {
    '이름': '홍길동',                 # 문자열
    '나이': 25,                      # 정수
    '특기': ['농구', '도술'],         # 리스트
    '가족': {'아버지': '아빠', '어머니': '엄마'}  # 딕션너리
}

print(a['이름'], a['나이'])
print(a['특기'][0], a['특기'][1])
print(a['가족']['아버지'], a['가족']['어머니'])
print('-' * 40)
# 3)
a = {
    'response': {
        'body': {
            'items': [{
                    '나이': 10,
                    '이름': '홍길동'
                },
                '물약'
            ]

        },
        'page': 100
    },
    'header':{
        'result': 200,
        'meg': 'ok'

    }
}

print(a['response']['body']['items'][0]['나이'])
print('-' * 40)
print(a['response']['body']['items'][0]['이름'])
print('-' * 40)
print(a['response']['body']['items'][1])
print('-' * 40)
print(a['response']['page'])
print('-' * 40)
print(a['header']['result'])
print('-' * 40)
print(a['header']['meg'])
"""


"""
# ex60)
# 1)
# main.py에서 실행시킨 결과
print(__name__)
# 출력결과 : __main__

# 2)
# tiger01에서 실행시킨 결과
print(__name__)
# 출력결과 : __main__

# 3)
if __name__ == '__main__':
    print('여기서 부터 프로그램 작성')

# 4) main.py에서 tiger01.py를 import시킬것이다.
import tiger01 as tr

# tiger01.py에 있는 print(__name__)의 결과는 파일이름을 출력한다.

# 5) tiger01.py의 코드 수정
# if __name__ == '__main__':
#   print('독수리')
#   print([1, 2, 3])
#   print(__name__)
print('-' * 40)

tr.f1(1000)
"""


"""
# ex59)
# 1. Tiger.py 파일 생성
# 2. Tiger.py 에서 f1 함수를 만든다.
#            def f1(a):
#               print('호랑이', a)
# 3. import를 사용한다.
# 3-1 사용 방법1
# import tiger01
# tiger01.f1(1000)

# 3-2 사용 방법2
# from tiger01 import *
# f1(2000)

# 3-2 사용 방법3
# import numpy as np
# import tiger01 as tr
# tr.f1(3000)

# 4. 그런데 이 프로그램은 문제가 있다.
# import하는것 만으로도 tiger01에 있는 프로그램들이 실행되어 버린다.
"""


"""
# ex58) generator
# 1)
def f1(data):
    result = []

    for x in data:
        result.append(x * x)

    return result


print(f1([1, 2, 3, 4]), type(f1([1, 2, 3, 4])), end= '\n\n')


# 2)
it = iter(range(3))
print((next(it)))
print('호랑이')
print(next(it), end='\n\n')
# print(next(it)) # 에러가 발생한다.


# 3)
def f1(data):
    print('대기1')
    yield data[0] * data[0]
    print('대기2')
    yield data[1] * data[1]
    print('대기3')
    yield data[2] * data[2]

it = f1([1, 2, 3])
print(next(it))
print(next(it))
print(next(it))
# print(next(it)) 여기서 사용할수 없다.
print('-' * 40)

# ex4)
def f1(data):
    for x in data:
        print('대기' + str(x))
        yield x * x

it = f1([1, 2, 3])
print(next(it))
print(next(it))
print(next(it))

it = f1([1, 2, 3])
for x in it:
    print(x)
print()

# 5)
data = [x * x for x in[1, 2, 3]]
print(type(data))

# 이 코드때문에 위에서 유도 되었다. () << 를 사용하고 있다.
it = (x * x for x in[100, 200, 300])
print(next(it))
print(next(it))
print(next(it))

# list를 이용해서 제너레이터를 실행시킨다
it = (x * x for x in[100, 200, 300])
print(list(it))
"""


"""
# ex57) decorator
# 1)
# 관점지향프로그램이다.(AOP)
def f1():
    print(1)            # 1줄이 아니고 100줄이다(가정)
    print('호랑이')      # 진짜 1줄이다
    print(2)            # 1줄이 아니고 100줄이다.(가정)


def f2():
    print(1)            # 1줄이 아니고 100줄이다.
    print('코끼리')      # 진짜 1줄이다
    print(2)            # 1줄이 아니고 100줄이다


f1()
f2()
print('-' * 40)

# 2)
def f1():
    print('호랑이')


def f2():
    print('코끼리')


def f3(f4):                 # 데코레이터 함수라고 한다.
    def f5():
        print(1)  # 1줄이 아니고 100줄이다.
        f4()
        print(2)  # 1줄이 아니고 100줄이다.

    return f5

f3(f1)()
f3(f2)()
print('-' * 40)

# 3)
def f3(f4):                 # 데코레이터 함수라고 한다.
    def f5():
        print(1)  # 1줄이 아니고 100줄이다.
        f4()
        print(2)  # 1줄이 아니고 100줄이다.

    return f5


@f3           # f3에 전달되는 함수이름은 f1입니다.
def f1():
    print('호랑이')


@f3           # f3에 전달되는 함수이름은 f2입니다.
def f2():
    print('호랑이')


# f(3)(f1)()
f1()
f2()
print('-' * 40)

# 4)
def f3(f4):                 # 데코레이터 함수라고 한다.
    def f5(*args, **kwargs):
        print(1)  # 1줄이 아니고 100줄이다.
        f4(*args, **kwargs)
        print(2)  # 1줄이 아니고 100줄이다.

    return f5


@f3           # f3에 전달되는 함수이름은 f1입니다.
def f1():
    print('호랑이')


@f3           # f3에 전달되는 함수이름은 f2입니다.
def f2(a):
    print('호랑이', a)

@f3           # f3에 전달되는 함수이름은 f9입니다.
def f9(a, b):
    print('앵무새', a, b)


f1()
f2(1000)
f9('사과', 1000)
print('-' * 40)

# 5) 데이터베이스 프로그램이라고 가정했다.
def dataAccess(delegate):
    def decorate():
        print('데이터베이스에 접속하는 코드 10줄 정도')
        delegate()   # CRUD 작업을 처리한다.
        print('데이터베이스에 종료하는 코드 10줄정도')
        print()
    return delegate


@dataAccess
def dataInsert():
    print('insert data from table')


@dataAccess
def dataDelete():
    print('delete data from table')


dataInsert()
dataDelete()

# 데코레이터, 델리케이트, AOP, 프록시, 함수 포인트
"""


"""
# ex56)
# 1)
print('ex 1')
def f1(x):
    return x * 2

def f2(x):
    return x * x

def f3(x):
    return -x

# a는 함수가 된다.
def common(a, b):
    r = []
    for x in b:
        r.append(a(x))

    return r

print(common(f1, [1, 2, 3, 4]))
print(common(f2, [1, 2, 3, 4]))
print(common(f3, [1, 2, 3, 4]))

print()

# 2) 함수를 인수 전달할수 있다는것은 함수를 리턴 시킬수도 있다.
# 함수 내부에 함수를 작성할수 있다.
# 밖에 있는 함수를 outer함수 안에 있는 함수를 inner함수
print('ex 2')
def f1():
    print(1)
    def f2():
        print(2)

    return f2

# 사용방법 1
a = f1()
a()

# 사용방법 2
f1()()
print()

# 3)
print('ex 3')
def f1(a):
    print(a)
    def f2(b):
        print(b)
        return 30

    return f2

print(f1(10)(20))
print()

# 4)
print('ex 4')
# num의 생존 범위를 모든 언어를 통틀어서 함수 호출이 끝나면
# num 메모리는 사라진다.
def f1():
    num = 10
    print(num)

f1()
print()

# 5)
print('ex 5')
def f1():
    msg = '호랑이'
    def f2():
        print(msg)

    return f2

# msg변수는 생명 연장이 일어난다.
# 클로즈라고 한다.
f3 = f1()
f3()
print()

# 6)
print('ex 6')
def calc():
    a = 10
    b = 5

    def test(x):
        return a * x + b

    return test

print(calc()(100))
print(calc()(200))
print()

# 7) 6번 내부함수를 란다로 변경
print('ex 7')
def calc():
    a = 10
    b = 5


    return lambda x: a * x + b

print(calc()(100))
print(calc()(200))
print()
"""

"""
# 1. 1차원 배열을 수동설정
# 2. 순차적으로 데이터 저장(arange)
# 3. 랜덤하게 데이터 저장
# 4. empty, 0, 1
# 5. 2차원배열(수동설정,arange,이용한reshape, read, empty, 0, 1
# 6. 2차원에서 slide
# 7. 산술연산, 통계
# 8. 조건식


# ex55)
a = np.arange(0, 60, 10)
print(a)
print(a >= 30)
# 조건에 만족되는 개수
print((a >= 30).sum())       # 3

print(np.where(a <= 30, 88, 99))
print(np.where(a < 30, a, 99))
print(np.where(a % 2 == 0, '짝수', '홀수'))

print(np.where(a >= 30))    # (array([3, 4, 5], dtype=int64),)
b = np.where(a >= 30)       
print(a[b])
"""


"""
# ex54)
a = np.arange(1, 7, 1).reshape(2, 3)
print(a)

# 1)
print('합', a.sum())           # print(np.sum(a))
print('평균', a.mean())
print('최소값', a.min())
print('최대값', a.max())
print('분산', a.var())
print('표준편차', a.std())


a = np.array([1, 2, 3, 4, 5])
# 10 20 30 40 50 60
print('평균', a.mean())
# 편차
# 2, 1, 0, 1, 2

# 편차 제곱
# 4, 1, 0, 1, 4

# 편차 제곱의 합
# 10

# 분산 >> 편차 제곱의 합 / 개수
print(10 / 5)
print(a.var())

# 표준편차
print(math.sqrt(10 / 5))
print(a.std())

# 2)
# a = np.arange(1, 7, 1).reshape(2, 3)
a = np.random.randint(1, 10, size=(2, 3))
print(a)
# axis=0 : 수직방향으로...axis=1: 수평방향으로...
print(a.sum(axis=0))
print(a.mean(axis=0))
print(a.max(axis=0))
print(a.min(axis=0))
print()

# index를 얻는다
print(a.argmax(axis=0))
print(a.argmax(axis=1))
"""

"""
# ex53)
a = np.arange(1, 7, 1).reshape(2, 3)
print(a)

b = np.arange(1, 7, 1).reshape(2, 3)
print(b)

print(a + b, '--------------1')
# 리스트의 확장이다.
c = [1, 2, 3]
d = [1, 2, 3]
print(c + d, '-------------1')

print(a - b, '--------------2')
print(a * b, '--------------3')
print(a // b, '--------------4')
print(a % b, '--------------5')
print(a * 10, '--------------6')
print(a * a, '--------------7')
print(a >= b, '--------------8')
"""


"""
# ex52)
# 2차원 배열이다. [3][4]
data = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 8, 7, 6],
])

print(data)
print(data[0][0])
print(data[2][3])
print(data[1:3, 2:4])
"""


"""
import numpy as np
# ex51)
# 1)
# [0, 1] 개수는 6개만 배열을 생성한다.
a = np.random.randint(2, size=6)
print(a)

# 2)
# [3, 9]
a = np.random.randint(3, 10, size=6)
print(a)

# 3) 2차원을 사용하고 싶으면 tuple 사용한다.
a = np.random.randint(10, size=(3, 4))
print(a)

# 4)
# [0.0 ~ 1.0]까지의 실수값
a = np.random.rand(4)
print(a)

b = np.random.randint(10, size=4)
print(b)

print(a.dtype, b.dtype)

# 5) empty, zeros, ones, randint
print('ex5------------------')
a = np.empty(6)    # 배열을 만드는 생성 속도가 빠르다.
print(a)

a = np.zeros(6)
print(a)

# 디폴트는 실수 값으로 나온다.
a = np.ones(6)
print(a)

# 실제 코드에서 사용된다.
a = np.ones(6, dtype=np.int64)
print(a, a.dtype)

#
a = np.random.randint(2, size=6, dtype=np.int64)
print(a, a.dtype)

print('-' * 40)
# 6) 2차원으로 만든다.
a = np.empty((2, 3))
print(a)

a = np.zeros((2, 3))
print(a)

a = np.ones((2, 3))
print(a)

a = np.random.randint(100, size=(2, 3))
print(a)

a = np.arange(6).reshape(2, 3)
print(a)

# 7)
a = np.arange(6)            # [0 1 2 3 4 5]
print(a)

a = np.arange(5, 10)        # [5 6 7 8 9]
print(a)

a = np.arange(5, 10, 2)     # [5 7 9]

print(a)
"""


"""
# ex50)
import numpy as np

# 1)
# 순차적으로 데이턱 저장된 6개 짜리 1차원 배열을만든다.
a = np.arange(6)
print(a)
print('배열내용:', a)
print('shape:', a.shape)
print('size:', a.size)
print('type:', a.dtype)  # a가 가지는 있는 데이터의 타입

print('ndim:', a.ndim, '차원 배열')
print('itemsize:', a.itemsize, '1개당 메모리 확보수')
print('len: 이렇게는 사용하지 않는다', len(a))
print('type:', type(a))  # a 자체의 타입을 묻는다
print('-' * 40)
# 2)
# 6 = 2 * 3 일때 reshape가 성립된다.
# 가로가 2칸, 세로가 3칸인 배열을 만든다.
a = np.arange(6).reshape(2, 3)
print(a)
print('배열내용:')
print(a)
print('shape:', a.shape)
print('size:', a.size)
print('type:', a.dtype)  # a가 가지는 있는 데이터의 타입

print('ndim:', a.ndim, '차원 배열')
print('itemsize:', a.itemsize, '1개당 메모리 확보수')
print('len: 이렇게는 사용하지 않는다', len(a))
print('type:', type(a))  # a 자체의 타입을 묻는다.
"""

"""
# ex49)
# csv라이브러리는 처음부터 파이썬 갈때 있었다.
import csv

# numpy 라이브러리는 필요할때 다운받아서 사용한다.
import numpy as np

# 1. string : 문자들의 집합
# 2. list : 서로다른 타입의 데이터를 저장해서 CRUD했던 구조
# 3. numpy : 동일한 수자형태타입을 저장해서 산술적인 연산을 지원하는 구조
#       구조는 배열이다.(동일한 숫자(정수,실수) 타입이다.)

# 출력 함수에 대한 창고 코드
# for x in dir(list):
#   print(x)

# for x in dir(np):
#    print(x)


a = [1, 2, 3, 4, 5]               # [1, 2, 3, 4, 5]
b = np.array([1, 2, 3, 4, 5])     # [1 2 3 4 5] >> 콤마 없음
print(a, type(a))
print(b, type(b))

# ndarray : numeric dimension array : n차원의 숫자를 다루는 배열이다.
"""

"""
# ex48) 실제파일을 읽어본다.
import csv

f = open('school_2019.csv', 'r', encoding='utf-8')
data = csv.reader(f)

# 첫라인의 한줄만 뽑아 낸다.
header = next(data)
print(header)

info = []
for x in data:
    info.append(x)


f.close()

# 읽어 들인 데이터를 출력해본다.
print('데이터 라인수', len(info))

# 전체 보는 코드는 주석
# for x in info:
#     print(x)

for index, value in enumerate(info):
    print(index, value)
    if index == 5:
        break
"""

"""
# ex47) 파일 입출력
# 데이터 파일이 .txt는 잘 사용하지 않는다.
# .csv 파일을 사용한다.(메모장에서 읽을수 있다.)
# .csv 파일은 데이터를 저장하기 위한 규칙이 적용되어 있다.
# .csv 파일을 사용하기 위해서 import csv가 필요하다
# 1) 출력
import csv
f = open('sample02.csv', 'w', encoding='utf-8', newline='')
# f가 가지는 출력형식을 csv형식의 출력을 line객체가 하게 된다.
line = csv.writer(f)

# csv파일의 하드(header)를 출력함
line.writerow(['대학교명', '학과수', '학생수', '교수수'])
line.writerow(['A대학', 59, 2146, 14])
line.writerow(['B대학', 60, 3334, 18])
line.writerow(['C대학', 93, 7414, 29])
line.writerow(['D대학', 51, 3474, 25])
line.writerow(['E대학', 70, 6756, 26])
f.close()

# 대학교명,학과수,학생수,교수수 >>
# 이 데이터에서 (항목이 콤마로 연결되었다.)
# 콤마뒤에 스페이스 처리가 되어 있지 않다.


# 2) 리딩
f = open('sample02.csv', 'r', encoding='utf-8')
data = csv.reader(f)

# 첫라인의 한줄만 뽑아낸다.
header = next(data)
print(header)

# 2번째 라인부터 읽어 들이게 된다.
# 일단 출력을 해보기 위한 코드이다.
# 데이터를 이용할려면 저장해야한다.
# for x in data:
#    print(x)

info = []
for x in data:
    info.append(x)

# 리스트를 전체 출력하면 한줄에 쭉 출력되어 버린다.
print(info)


for x in info:
    print(x)


# 적당하게 데이터를 출력한다.
for index, value in enumerate(info):
    print(index, value)
    if index == 3:
        break

f.close()

print('Exit')
"""

"""
# ex46) 파일 입출력
# 프로젝트 이름 우클릭 >> open in >> directory path >> 프로그램 이름선택
# >> 경로확인

# 1) 파일을 생성해본다.
# 파일 입출력은 싸인펜을 사용하는것과 같다(open, close)
# read, write
f = open('sample01.txt', 'w', encoding='utf-8')
f.write('호랑이호랑이')
f.close()

# 2) 반복 출력
# 정수를 바로 출력할수 없다.
f = open('sample01.txt', 'w', encoding='utf-8')
for x in range(1, 5):
    f.write(str(x))
f.close()

# 3) 문자열 연결과 줄바꿈(케리지리턴) $n
f = open('sample01.txt', 'w', encoding='utf-8')
for x in range(1, 5):
    f.write('호랑이 : ' + str(x) + '\n')
f.close()

# 4) with 여기서오픈 as >>>> close 생략 가능
with open('sample01.txt', 'w', encoding='utf-8') as f:
    for x in range(1, 5):
        f.write('코끼리 : ' + str(x) + '\n')

# 5) 파일에서 읽어 들인다.( 2번째 인수를 'r'로 수정)
f = open('sample01.txt', 'r', encoding='utf-8')
data = f.readline()   # 1줄을 읽어 들인다.
print(data)

data = f.readline()
print(data)

data = f.readline()
print(data)

data = f.readline()
print(data)

f.close()
print('-' * 40)
# 6) 전체 라인수를 모를때 전체를 읽어들인다.
f = open('sample01.txt', 'r', encoding='utf-8')
while True:
    data = f.readline()
    print(data)
    if not data:
        print('데이터를 읽지 못함')
        break

f.close()
print('-' * 40)

# 7) readline(s)
# 리스트로 저장이 된다.
# 결과 : ['코끼리 : 1\n', '코끼리 : 2\n', '코끼리 : 3\n', '코끼리 : 4\n']
f = open('sample01.txt', 'r', encoding='utf-8')
data = f.readlines()
print(data)
f.close()

# 줄바꿈이 2번 일어나게 되는데
# 1개는 리스트 안에 줄바꿈이 있고
# 1개는 print 함수 자체가 줄바꿈을 해버린다.
for x in data:
    print(x)
print('파일 입출력 작업이 종료됨')
# 8) 줄바꿈을 제거
# 방법1)
data = ['코끼리 : 1\n', '코끼리 : 2\n', '코끼리 : 3\n', '코끼리 : 4\n']
print(data)

test = '코끼리 호랑이 독수리'
test = test.replace('호랑이', '앵무세')
print(test)


for x in range(len(data)):
    data[x] = data[0].replace('\n', '')

print(data)
print('-' * 40)
# 방법 2)
data = ['코끼리 : 1\n', '코끼리 : 2\n', '코끼리 : 3\n', '코끼리 : 4\n']
print(data)

# enumerate 테스트 코드
for index, value in enumerate(data):
    print(index, value)


for index, value in enumerate(data):
    data[index] = value.replace('\n', '')

print(data)
"""

"""
# ex45-2)
class Zoo:
    def __init__(self, animal):
        self.animal = animal

    def cry(self):
        self.animal.cry()


class Dog:
    def cry(self):
        print('멍멍')


class Cat:
    def cry(self):
        print('야옹')

# 1)
z1 = Zoo(Dog())
z2 = Zoo(Cat())
z1.cry()
z2.cry()

# 2)
z3 = [Zoo(Dog()), Zoo(Cat())]
z3[0].cry()
z3[1].cry()

# 3)
for x in z3:
    x.cry()
"""

"""
# ex45-1)
class Dog:
    def cry(self):
        print('멍')


class Cat:
    def cry(self):
        print('야옹')


class Snake:
    def cry(self):
        print('획')


animal = [Dog(), Cat(), Snake()]
print(len(animal))
animal[0].cry()

for x in animal:
    x.cry()
"""

"""
# ex44)
class Tiger:
    def __init__(self, num):
        print('Tiger 생성자', num)


class Lion(Tiger):
    def __init__(self, num):
        Tiger.__init__(self, num // 2)
        print('Lion 생성자', num)


a = Lion(1000)
# 참조
# 클래스 상속 계층도를 보고 싶을때
# print(Lion.mro())
print(Lion.mro())
for x in Lion.mro():
    print(x)
"""

"""
# ex43) 상속
class Tiger:
    def f2(self):
        not self
        print(2)

    def f3(self):
        not self
        print(31)

class Lion(Tiger):
    def f1(self):
        not self
        print(1)

    def f3(self):
        not self
        print(32)

    def f4(self):
        super().f3()
        print(4)

# 이코드는 상속과는 무관한 코드이다.
a = Tiger()

b = Lion()
b.f1()
b.f2()
b.f3()
# 부모의 함수 호출
b.f4()
"""

"""
# ex42) class
# 클래스를 구성하는 3대요소: (1.변수(인스턴스), 2.생선자, 3.함수)
# 사과: 속성(색상,무게, 당도, 원산지....), 동작(동사, 먹는다, 깍는다, 요리한다)

# 1번) 클래스만 만들었다.
class Tiger01:
    pass

# 2번) 아무 일도 하지않는 함수를 만든다.
class Tiger02:
    def f1(self):
        pass

    def f2(self):
        pass

# 3번) 무조건 self를 받는다. (self 변수를 왜 사용안하는거에 대한 경고)
class Tiger03:
    def f1(self):
        not self
        print('호랑이')


# a라는 이름의 객체를 만들었다(객체를 생성시킨다)
a = Tiger03()
# f1함수는 인수를 1개 전달하는 모양인데
# 왜 인수를 전달하지 않았는가 ?
a.f1()

# 4번) 생성자의 정확한 표현은 생성자함수라고 한다.
# 생성자 함수는 객체가 생성될때 자동으로 콜(호출)이 된다.
# 생성자 함수는 사용자가 직접 호출할수 없고
#      객체 1개가 생성될때 자동으로 딱 1번 호출된다.
# 생성자함수는 1번 이상 만들수가 없다.
class Tiger05:
    # num = 10 변수를 만드것이 아니다.
    # 생성자함수가 하는 역할은 맴버변수를 만들고
    # 그 값을 초기화 하는 목적이다.
    def __init__(self):    # 생성자 함수이다.
        print('생성자 함수가 호출이되었다')
        self.a = 10
        self.seat = 64
        self.weight = 100     # 변수 3개가 만들어졌다.

    def showMember(self):
        print(self.a, self.seat, self.weight)


t1 = Tiger05()     # 생선자가 콜이 된다.
t1.showMember()

t2 = Tiger05()
t2.showMember()

# t1의 seat이랑 t2의 seat은 완전히 다른 변수이다.
t1.seat = 1000
t2.seat = 2000
print(t1.seat, t2.seat)

# 맴버 변수가 어떤것이 선언되었는지 확인 할때
print(t1.__dict__)    # {'a': 10, 'seat': 1000, 'weight': 100}
print(t2.__dict__)    # {'a': 10, 'seat': 2000, 'weight': 100}

# 5번)
# 함수, 생성자, 변수

# 5번)
class Tiger06:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)

t1 = Tiger06('호랑이1', 20)
t2 = Tiger06('호랑이2', 30)
t1.show()
t2.show()
print('-' * 40)
# 7번)
# 생성자 함수는 1개밖에 못만든다.
class Tiger07:
    def __init__(self, name='무명', age=0):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)

t1 = Tiger07()
t2 = Tiger07('호랑이2')
t3 = Tiger07('호랑이3', 20)

t1.show()
t2.show()
t3.show()
print('-' * 40)
# 8번)
class Tiger08: # 자동차 클래스라고 생각한다.
    def __init__(self, fuel=100):
        self.fuel = fuel  # self.fuel : 인스턴스 변수

    def move(self):
        print('자동차가 달린다')
        self.fuel -= 15

    def stop(self):
        print('자동차가 멈춘다')
        self.fuel -= 3

    def inject(self, fuel):
        self.fuel += fuel

    def showFuel(self):
        print('남은 연료 : ', self.fuel)


car1 = Tiger08()
car1.move()
car1.showFuel()

car2 = Tiger08(300)
car2.showFuel()
car2.move()
car2.move()
car2.showFuel()

car2.stop()
car2.showFuel()

car2.inject(50)
car2.showFuel()
print('-' * 40)
# 9번)
# 클래스 변수(관제탑)을 사용할때는 반드시 클래스 이름으로만 사용한다.
# 만약에 다른 이름으로 사용하면 이골 저골 본다.
class Tiger09:
    # 관제탑이다. 프로그램이 실행될때 1번 만들어 진다.
    count = 777                  # 이변수를 클래스 변수라고 한다(static 변수이다)

    def __init__(self):
        self.num = 10


    def inc(self):
        not self
        Tiger09.count += 10

    def dec(self):
        not self
        Tiger09.count -= 10

print(Tiger09.count)   # 클래스 이름으로 사용하고 있다.
air = Tiger09()
print(air.count)       # 다른 이름으로 사용하고 있다.(사용하지 말자)

# 주의 해야 할 예제
# print(air.__dict__)
# air.count = 888   # 내부 인스턴스 변수를 만들어 버린다.
# print(air.__dict__)

air1 = Tiger09()
air1.inc()
print(Tiger09.count)

air2 = Tiger09()
air2.dec()
print(Tiger09.count)

print('-' * 40)
# 10번)
# 생성된 객체가 self 이다.
class Tiger10:
    def __init__(self):
        print(id(self))

a = Tiger10()
print(id(a))

b = Tiger10()
print(id(b))

# 11번)
class Tiger11:
    def f1(self):
        not self
        print('f1 call')

    def f2(self):
        not self
        print('f2 call')
        self.f3()

    def f3(self):
        not self
        print('f3 call')
        self.f1()

# 함수를 서로 호출하는것은 프로그램에 폭주가 일어난다.
#    def f4(self):
#       not self
#        print('f4 call')
#        self.f5()
#
#    def f5(self):
#        not self
#        print('f5 call')
#        self.f4()

# a = Tiger11()
# t.f1()
# t.f2()
# t.f4() # 사용할수 없다.
print('-' * 40)
# 12번)
# 객체를 인수 전달하는 프로그램
class Lion:
    def f1(self):
        not self
        print('Lion f1 call')


class Tiger12:
    def f1(self, Lion):
        not self
        Lion.f1()
        print('Tiger f1 call')

t12 = Tiger12()
t12.f1(Lion())

print('-' * 40)
# 13번)
# 체이닝 프로그램
class Tiger13:
    def f1(self):
        print('Tiger13 ,1')
        return self

    def f2(self, a):
        print('Tiger13 ,a')
        return self

    def f3(self, a, b):
        not self
        print('Tiger13', a, b)

t = Tiger13()
t.f1().f1().f2(10).f3(888, 999)
"""

"""
# 앞으로 남은 일정
# 클래스, 넘파이, 판다스, map plot, 파일압출력, 데이터분석
"""

"""
# ex41) 프로그램을 중단시키지 말고 프로그램적으로 처리해서
# 계속 진행하는것을 예외 처리라고 한다
# 1번)
try:
    print(4 / 0)
except:
    print(2)

print('호랑이')
print('-' * 40)
# 2번)
try:
    print(4 / 0)
except Exception as e:
    print(e)

print('호랑이')

# 3)
a = [10, 20, 30]
print(a.index(30))

try:
    print(a.index(100))
except Exception as e:
    print('예외 발생', e)

print('프로그램은 중단되지 않았음')
"""

"""
# ex40)
# 1번)
def func(n):
    if n % 2 == 0:
        return '짝수'
    else:
        return '홀수'


print(func(10))

# 2번)

def func(n):
    return '짝수' if n % 2 == 0 else '홀수'
print(func(10))

# 3번 1개의 데이터가 아니고 여러개의 데이터 대하여 ...
print(list(map(func, [1, 2, 3, 4])))

# 4번 란다로 처리
print(list(map(lambda x: '짝수' if x % 2 == 0 else '홀수', [1, 2, 3, 4])))

# 5번 컴프리핸션
print(['짝수' if x % 2 == 0 else '홀수' for x in range(1,5)])
"""


"""
# ex39) map( 함수 + 데이터 ) >> 데이터 가공
# 반복문을 사용하지 않고 데이터 1개의 함수에 넣어서
# 그 결과를 map 으로 받아온다. 사용은 list 로 감싼다.
# 1번) 함수 정의
def func(n):
    return n + 1


# 2번) 데이터 정의
data = [1, 2, 3, 4]

# 3번)
result = map(func, data)
print(type(result))
print(list(result))

# 4번) 3번에 대한 취합코드
print(list(map(func, data)))

# 5번) 4번에 대하여 코드 수정
print(list(map(func, [1, 2, 3, 4])))

# 6번) 5번에 대하여 란다를 사용
print(list(map(lambda n: n + 1, [1, 2, 3, 4])))

# 7번) 6번을 조금만 변형( 파이썬 스럽다 )
print(list(map(lambda n: n + 1, range(1, 5))))

# 8번) 컴프레이션으로 수정
# 그래서 최근에는 map사용을 지양하고 컴프르핸션사용 추세
print([x + 1 for x in range(1, 5)])
"""

"""
# ex38) 람다 함수 : 코드가 간략화 된다.
# 리턴함수를 대상으로 한다.
# 1번)
def func():
    a = 10
    b = 20
    return a + b
print(func())

# 2-1번)
def func(x):
    return x + 1000
print(func(10))

# 2-2번)
# func = lambda x: x + 10 : return x + 10
func = lambda x: x + 1000
print(func(10))

# 2-3번) 10이라는 인수 전달은 어떻게 하나
print((lambda x: x + 1000)(10))

# 3-1번) 인수 전달이 없다.
func = lambda : 9999

a = func()
print(a)

print(func())

# 3-2번)
print((lambda : 9999)())

# 4번) 인수 전달이 2(n)가 있을때
print((lambda x, y: x + y)(10, 20))
print((lambda x, y: x + y)('호랑이', '코끼리'))

# 5번)
def func01(fff):
    print(fff(8))

func02 = lambda x: x * x
print(func02(7))

func01(func02)
func01(lambda x: x * x)

print('-' * 40)
# 6번)
def func01(fff):
    print(fff(17, 3))

func01(lambda x, y: x + y)
func01(lambda x, y: x - y)
func01(lambda x, y: x * y)
func01(lambda x, y: x / y)
func01(lambda x, y: x // y)
func01(lambda x, y: x ** y)

# 7번)
def func01(num):
    return lambda x: x * num

# 풀어놓은 코드
func = func01(10)
a = func(20)
print(a)

# 압축된 코드
print(func01(10)(20))

# 8번)
f = lambda n, m: n if n % 2 == 0 else m

print(f(1, 888))
print(f(2, 999))
"""


"""
# ex37) comprehension(독해)
# 데이터를 분석하고 해석하고 조건을 설정해서
# 새로운 데이터를 재 생산해 내는것을..

# 1번)
a = []
for x in range(6):
    a.append(x)
print(a)

# 2번)
a = []
for x in range(6):
    a.append(x * 2)       # 데이터 재생산
print(a)

# 3번) comprehension()
a = [x * 2 for x in range(6)]
# 밑에 코드는 설명이고 실행은 안된다.
# a = [
#           for x in range(6) :
#           x * 2
#     ]

print(a)

# 4-1번)
a = ['앵무새' for x in ['호랑이', '코끼리', '독수리']]
print(a)

# 4-2번)
a = ['호랑이', '코끼리', '독수리']
b = ['앵무새' for _ in a]
print(b)

# 5-1번)
a = ['호랑이', '코끼리', '독수리', '호랑이', '코끼리', '독수리']
b = []
for x in a:
    if x != '호랑이':
        b.append(x)
    else:
        b.append('산토끼')
print(b)

# 5-2번)
a = ['호랑이', '코끼리', '독수리', '호랑이', '코끼리', '독수리']
b = []
for x in a:
    b.append(x) if x != '호랑이' else b.append('산토끼')
print(b)

# 5-3번)
a = ['호랑이', '코끼리', '독수리', '호랑이', '코끼리', '독수리']
b = [x if x != '호랑이' else '산토끼' for x in a]
# ['산토끼', '코끼리', '독수리', '산토끼', '코끼리', '독수리']
print(b)

# 6번) 정규화 예제
a = list(range(6))  # 동일 코드 a = [0, 1, 2, 3, 4, 5]
print(sum(a))
b = [x / sum(a) for x in a]
print(b)
print(sum(b))      # 100분율을 해서 합이 1이 되는 계산과정을 정규화라고한다.

# 7-1번) 설명코드
# a = [for x in range(10)]
#        if x % 2 ==0
#            (?????)

# 7-2번)
a = [x * 100 for x in range(10) if x % 2 == 0]
print(a)  # [0, 200, 400, 600, 800] 짝수만 나온다

# 8번) remove 대안 코드(모두 삭제)
a = [1, 2, 3, 4]
a = a * 2
print(a)         # [1, 2, 3, 4, 1, 2, 3, 4]
print([x for x in a if x != 2])

# 9번) 't' 문자가 들어가 있는 동물 모두 선택
a = ['tiger', 'lion', 'cat', 'dog', 'eagle']
# 참고 코드
if 't' in a:
    print(1)
else:
    print(2)

b = [x + 'T' for x in a if 't' in x]
print(b)

# 10번) 't' 문자가 들어가 있는 동물이름을 대문자로 선택하세요
a = ['tiger', 'lion', 'cat', 'dog', 'eagle']
b = [x.upper() for x in a if 't' in x]
print(b)

# 11-1번)    
a = [x + y                  # a = [(x, y)]
     for x in range(3)
     for y in range(4)
     if (x + y) % 2 == 0
]
print(a)

# 11-2번)
a = [x + y for x in range(3) for y in range(4) if (x + y) % 2 == 0]
print(a)

# 12-1번)
for x in range(1, 6):
    for y in range(x, 6):
        for z in range(y, 6):
            print('[', x, y, z, ']', end=' ')
        print()
    print()

# 12-2번)
a = [(x, y, z)
     for x in range(1, 30)
     for y in range(x, 30)
     for z in range(y, 30)
     if x**2 + y**2 == z**2]

for x in a:
    print(x)

"""


"""
# ex36) 전달되는 인수를 초기화 시킬수있다.
# 단 끝에서 부터 초기화를 시켜와야 된다.
def func01(a, b, c=100, d=200):
    print(a, b, c, d)


func01(10, 20)
func01(10, 20, 30)
func01(10, 20, 30, 40)


def func02(a, b, c='tiger', d=100):
    print(a, b, c, d)


func02(10, 'lion')
func02(10, 'lion', 20)
func02(10, 'lion', 20, 'cat')

# 표준함수를 사용할때 인수가 총 13개를 던지겠끔 만들어져 있다고 할때
# 사용할때 인수 1개를 설정해도 사용이 가능하다는 이야기는
# 초기화가 12개 되어있다. 라고 해석하면 된다.

# 가변인수 전달 <--> 고정인수 전달
def func03(a, b, *args):
    print(a, b)
    print(type(args))
    for x in args:
        print(x, end=' ')
    print()

func03(10, 20)
func03(10, 20, 30, 40, 50, 60, 70)
func03('tiger', 20, True, [10, 20, 30])


# bare * : 문법
def func04(a, b, *, c, d):
    print(a, b, c, d)

# 명시를 하지 않으면 에러 발생
# func04(10, 20, 30, 40)
func04(10, 20, c=30, d=40)


def func05(a, b, *, width, height, color):
    print(a, b, width, height, color)

# 개발 팀원이 작성한것이다.
# 팀장이 와서 코드를 검증한다.
# 코드의 가독성이 떨어진다.
func05(1, 2, width=100, height=200, color='red')


def func06(**kwargs):
    print(list(kwargs.keys()))
    print(list(kwargs.values()))
    for x in kwargs.values():
        print(x, end=' ')


    print(list(kwargs.items()))
    for k, v in kwargs.items():
        print(k, v)


func06() # 인수 전달 없이 호출
# func06(10)  # 에러 발생
# 딕셔너리 전달 방식
func06(a=10, b='tiger', c=True)
"""



"""
# ex35)
# 1번)
def func01():
    print(1)
    return 100     # return을 만나면 함수 종료
    print(2)
    return 200
func01()

def func02_1(a, b):
    if a > b:
        return a + b
    else:
        return a - b
    # print('호랑이') # 있어봐야 필요 없다.


print(func02_1(10, 20))
print(func02_1(20, 10))

def func02_2(a, b):
    return a + b if a > b else a - b

print(func02_2(10, 20))
print(func02_2(20, 10))

# 리턴된 값은 코드에서 응용할수 있다.
def func03_1():
    return 1000 # return 코드는 다시 응요해서 사용가능

print(func03_1())

def func03_2():
    print(1000)

func03_2()

print(func03_1() * func03_1())

def func04(a):
    return a * 2

print(func04(func04(6)))

"""

"""
# ex34)
# 인수 전달을 1개이상 할수 있다.
# 단, 리턴은 1개만 할수있다.
# a, b = 3, 4
def func01(a, b):
    print(a, b)
    print(a + b)
func01(2, 3)

def func02(num):
    for x in range(10):
        print(num, '*', x, '=', x * num)
func02(13)

def func03(num):
    sum = 0
    for x in range(1, num + 1):
        sum += x
    print(sum)
func02(1000)


def func04_1():
    for x in range(3):
        for y in range(4):
            print('x:', x, 'y:', y)
func04_1()
print('-' * 40)

def func04_2():
    for x in range(3):
        for y in range(4):
            if (x + y) % 2 == 0:
                print('0', end=' ')
            else:
                print('x', end=' ')
        print()
func04_2()

print('-' * 40)

def func04_3(width, height, ch1, ch2):
    for x in range(height):
        for y in range(width):
            if (x + y) % 2 == 0:
                print(ch1, end=' ')
            else:
                print(ch2, end=' ')
        print()
func04_3(13, 8, '0', 'x')

print('-' * 40)
def func04_4(width, height, ch1, ch2):
    for x in range(height):
        for y in range(width):
            print(ch1 if(x + y) % 2 == 0 else ch2, end=' ')
        print()
func04_4(13, 8, '0', 'x')
"""

"""
# ex33) 함수(function) >> method(class 와 연관)
# 자주 사용되는 코드를 저 사용하기 위하여 코드를 지정되는 형태

# 1번) 전달인수 없고 리턴값이 없다.
def func01():
    print('멍')


func01()
func01()
for x in range(4):
    func01()

# 2번) 전달인수 있고 리턴값이 없다
def func02(num):           # num = 7
    print(num)
    for _ in range(num):
        print('멍', end=' ')
    print()


func02(7)
# 3번) 전달인수 없고 리턴은 없다.
def func03():
    print('3번째 함수 호출')
    return 100


a = func03()
print(a)
print(func03())     # 반은것을 출력한다.
# 안받으면 문법에러없이 값이 소멸된다.
func03()

# 4번) 전달인수 있고 리턴값이 있다.
def func04(num):
    print('4번째 함수 호출')
    return num * 2


a = func04(10)
print(a)
print(func04(100))
"""


"""
# ex32) dictionary (키:값,키;값,key:value,k:v)
# 1번)
a = {10: 100, 20: 200, 30: 300}
# 10번키로 정수를 가지고 있다
# 20번키로 정수를 가지고 있다
# 30번키로 정수를 가지고 있다
print(type(a))
print(a)
# 키는 유일키이다.
a = {10: [], 20: [], 30: []}
# 10번, 20번, 30번 키로 list를 가지고 있다.

# 2번)
a = {10: '호랑이', 20: '코끼리', 30: '독수리'}
print(a)
# 키: 모든 타입을 사용할수있다.
# 때문에 중접해서 정의될수 있다.
a = {10: 999, 20: '코끼리', 30: [1, 2, 3], 40: (4, 5), 50: True}
print(a)

# 중첩 예제
a = {10: {20: {30: {40: '호랑이'}}}, 20: '독수리'}

# 중첩 예제
# 중복된 키가 있을경우 둘중에 하나는 사라진다(어떤 키가 사라는지는 알수없다.)
a = {10: 100, 10: 200, 20: 300}

# 키를 문자열로 설정할수 있다.
# (가급적이면 정수면 정수, 문자열이면 문자열로만 구성하는게 좋다.
a = {'name': '홍길동', 'age': 26, 'salary': 300}
print(a)
# 키를 실행시 추가 할수 있다.
a = {'name': '홍길동', 'age': 26} # 파일에서 읽어 왓다

a['salary'] = 300 # 여기에서 추가를 했다.
a['height'] = 183
print(a)

# 삭제
a = {'name': '홍길동', 'age': 26, 'salary': 300}
del a['age']
print(a)

# 선택
a = {'name': '홍길동', 'age': 26, 'salary': 300}
print(a['name'], a['age'])
print(a.get('name'))

print(a.keys())   # dict_keys(['name', 'age', 'salary'])

# 키를 리스트로 관리하고 있기 때문에 리스트를 이용해서 추출할수 있다.
print(list(a.keys()))   # ['name', 'age', 'salary']
b = list(a.keys())      # ['name', 'age', 'salary']
print(b)

# 잠시 튜플
c = (1000, 2000, 3000)
print(c[0], c[1], c[2])


print('-' * 40)

# 키는 [0]으로 값은 [1]으로 추출한다.
for data in a.items():
    print(data, data[0], data[1])

# 데이터 추출 정리
a = {'name': '홍길동', 'age': 26, 'salary': 300}
print('-' * 40)
print(a.keys())
print(a.values())
print(a.items())

for data in a.values():
    print(data)

b = list(a.values())

#
# range(0,6) <<  #range([0, 1, 2, 3, 4, 5])
c = range(6)      #range([0, 1, 2, 3, 4, 5])
print(list(c))
"""


"""
# ex31) tuple(데이터 집합+ 적당하게는 CRUD 가 있다)
# 1. () 사용한다. >> []는 리스트이다. >>{}는 딕션어리이다.
# 2. 데이터 갱신 불가(수정할수없다), 삭제할수 없다.
# 3. 자료가 1개일때는 끝에 콤마를 추가한다.

a = (10, 20, 30)
print(a)

a = ('tiger', 'lion', 'cat')
print(a)

a = (10, 'lion', True)
print(a)
print(len(a))

a = (10,)           # 콤마를 추가한다
print(type(a))

a = ('tiger',)
print(type(a))
"""

"""
# ex30)
# 1번
a = [10, 20, 30, 40]

# 검색을 해서 찾은 위치의 인덱스 번호를 얻는다.
b = a.index(30)
print(b)

print(a) # list의 데이터 변동은 없다.

# 못찾았을때 (예외 발생)
try:
    b = a.index(50)
except:
    print('검색 실패')
pass

# 2번
a = [20, 10, 40, 30]
# a.sort()           # 순차 정렬      ex([10, 20, 30, 40])
a.sort(reverse=False)
print(a)

a.sort(reverse=True) # 역순정렬       ex([40, 30, 20, 10])
print(a)

# 주의 : reverse명령은 데이터를 뒤집는다  ex([30, 40, 10, 20])
a = [20, 10, 40, 30]
a.reverse()
print(a)

# 3번
a = [10, 20, 30, 40, 50, 60, 20]
print(a.count(20))

a = ['tiger', 'tiger', 'lion', 'tiger', 'cat', 'dog']
print(a.count('tiger'))

# 4번
a = [10, 20, 30, 40]
a.append(50)
print(a)

# 이 프로그램은 잘못 사용했을 가능성이 높다.
a.append([60, 70, 80])
print(a)

# 윗 프로그램의 의도되로 프로그램을 작성한다면
# extend를 사용한다
a = [10, 20, 30, 40]
a.extend([60, 70, 80])
print(a)

# extend와 동일한 역활을 한다.
a = [10, 20, 30, 40]
# a = a + [60, 70, 80]
a = a + [60, 70, 80]
print(a)

print('-' * 40)

# 5번 문자열 비교하는것과 동일하다
# 1. 앞에서 부터 같은 데이터가 있으면 상쇄를 시킨다.
# 2. 서로 다른 데이터 2개랑 대소 비교를 한다.
# 3. 이후에 남은 데이터는 무시된다.
# 4. 비교할 데이터가 없으면 0으로 처리합니다.
a = [10, 20, 30]
b = [30, 20, 10]
print(a > b)        # False

a = [30, 20, 30, 10]
b = [30, 20, 10, 40]
print(a > b)        # True

a = [30, 20, 10]
b = [30, 20, 10, 40]
print(a > b)        # False

a = [30, 20, 30]
b = [30, 20, 30]
print(a >= b)       # True

# 사전순으로 정렬할때 사용된다.
print('tiger' > 'aiger')    # True
"""

"""
# ex29)
# 1번
a = [10, '호랑이', [20, 30, 40]]
print(a[0])
print(a[1])
print(a[2])
print(a[2][0])
print(a[2][1])
print(a[2][2])

# 2번 문자열상수와 리스트의 큰 차이점
a = 'abcd'
b = ['a', 'b', 'c', 'd']
# a[0] = 'e'  # 성립되지 않는다
b[0] = 'e'
print(b)

# 3번 데이터 갱신을 일괄적으로 할수있다. (일괄 정신, 연속 수정)
a = [10, 20, 30, 40, 50, 60, 70]
# 2 3 4
a[2:5] = [77, 88, 99]
# [10, 20, 77, 88, 99, 60, 70]
print(a)

b = ['tiger', 'lion', 'dog', 'cat']
# 1 2
b[1:3] = ['elephant', '9999']
print(b)

# 4번
a = [10, 20, 30, 40, 50, 60, 70]
# 2 3 4
a[2:5] = []
print(a)


a = [10, 20, 30, 40, 50, 60, 70]
# 2 3 4 자리를 삭제하고 삭제된 위치에 새로운 테이터 추가한다.
# 좌측과 우측의 개수가 동일할 필요가 없다.
a[2:5] = [1, 2, 3, 4, 5, 6, 7]
print(a)
print(len(a))

# 5번 삭제하는 코드가 동일한 코드이다.
a = [10, 20, 30, 40]
del a[2]
print(a)

a = [10, 20, 30, 40]
del a[2:3]
print(a)

# 6번 append를 이용하여 데이터를 끝에 추가한다.
a = [10, 20, 30, 40]
a.append('tiger')
print(a)

# 7번 insert를 이용해서 특정위치에 데이터를 추가한다.
# 0 1   2   3   4
# [ 10, 20, 30, 40]
a = [10, 20, 30, 40]
a.insert(1, True)
# a.insert(len(a), True) # append와 동일하다.
print(a)

# 8번 마지막 데이터 요소를 삭제
a = [10, 20, 30, 40]
a.pop()
print(a)

# 9번 특정위치의 데이터 요소 삭제
a = [10, 20, 30, 40]
a.pop(2)
print(a)

# 10번 데이터를 검색해서 삭제 (remove)
a = [10, 20, 30, 40, 20, 50, 60]
# 찾은 데이터 1개만 삭제한다.
# 찾은 데이터를 모두 삭제하고 싶을때 (예약)
a.remove(20)
print(a)


print('호랑이')
# 검색에 실패하면 에러가 발생한다. (exception)이 발생한다.

# 예외 처리 : 프로그램에 문제가 발생하더라도 프로그램을 중단하지말고
# 정상으로 프로그램을 진행시키는것
try:
    a.remove(100)
except:
    print('에러 발생')
pass

print('독수리')

try:
    print(10 / 0)
except:
    print('나누기 예외 발생')
pass
"""


"""
# 28) list 배열(데이터 집합) + (CRUD)
# 앗.. 출력결과에 데이터를 콤마로 구분해 놓았다.
# 1번
a = [10, 20, 30, 40]
print(a)

# 2번
print('호랑이', '코끼리', '독수리')

# 3번 데이터의 타입이 달라도 된다.
a = [10, '호랑이', 3.14, True]
print(a)
a = [10, '호랑이', 3.14, True, {}, ()]
print(a)
a = [10, '호랑이', 3.14, True, [20, 30, '독수리'], {}, ()]
# 모든 타입이 전부 들어갈수있다
print(a)

print('-' * 40)
# 4번 CRUD(create, read, update, delete)
# CR(Read)UD
a = [10, 20, 30, 40]
print(a)
print(a[0], a[1], a[2], a[3])

# for i in range(4)
for i in a:
    print(i, end=' ')
print()

# CRU(update)D
a = [10, 20, 30, 40]
# 삭제를 하고 추가된것이다.
print(id(a[0]))
print(id(a[2]))
a[2] = 99
print(id(a[0])) # 고유아이디가 같다.
print(id(a[2])) # 고유아이디가 변경된다.
print(a)

# CRUD(delete)
a = [10, 20, 30, 40]
del a[2]
print(a)
# 데이터 크기를 얻는다.
print(len(a))
"""


"""
# ex27)
# 1번
for i in range(3):
    for j in range(4):
        print('호랑이')
print()
# 2번
for i in range(3):
    for j in range(4):
        print(i,j)
print()

# 3번
for i in range(3):      # 세로의 의미를 가진다.
    for j in range(4):  # 가로의 의미를 가진다.
        print('[', i, j, ']', end=' ')
    print() # 안의 for문장이 다 돌고 나서 줄바꿈
print()

# 4번
a , b = 6, 7
for i in range(a):
    for j in range(b):
        print('*', end=' ')
    print()
print()

# 5번
print('%d' % 12)  # 12
print('%04d' % 12)# 0012
print('%4d' % 12) #   12

k = 0
for i in range(3):
    for j in range(4):
        print('%02d' % k, end=' ')
        k += 1
    print()
print()
"""


"""
# ex26) 승수 구하는 프로그램, a의 b승을 구한다.
print(2 ** 8)
_sum = 1

a = 3
b = 4
for i in range(b):
   #  _sum = _sum * a
    _sum *= a
print(_sum)
"""


"""
# ex25) 5단 출력 프로그램 및 합산 프로그램
# 1번
dan = 7
for i in range(10):
    print(dan, '*', i, '=',  dan * i)
print()

# 2번) 1부터 10까지 합산하는 프로그램
_sum = 0 # 간단한 경고를 피하기 위하여 (_) 를 사용함

num = int(input('합산할 숫자를 입력하세요'))

for i in range(1, num+1):
   #  _sum = _sum + i
    _sum += i
print(_sum) # tab을 치면 모든결과 /안치면 55만 나온다.

#    _sum = _sum + i
#    _sum += i

"""

"""

# ex25) 새로운 파일 만들기
# 프로젝트 이름선택 >> 우클릭>> new python file >>
# 파일명 입력(ex test01) 새로운 파일에서 코드 작성하고
# alt + shift + f10 으로 파일 교체하고 이후에 shift + f10
"""

"""
# ex24)
# i, data, value
# 1번
for i in [10, 20, 30, 40]:
    print(i)

# 2번
for i in [10, 20, 30, 40]:
    print(i, end=' ')
print() # 줄바꿈만 한다.

# 3번
for data in ['월', '화', '수', '목']:
    print(data, end=' ')
print()

# 4번
# for i in list(range(10)): 동일 문장
for i in range(10):
    print(i, end=' ')
print()
"""


"""
# ex23) for 선행예제
# range(n)   # 0 <= n <= x
print(range(10)) # range(0, 10)
print(type(range(10))) # class 'range'
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(list(range(10)))) # class 'list'

# 1번
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(10)))

# 2번
# [5, 6, 7, 8, 9]
print(list(range(5,10)))

# 3번
# [5, 7, 9]
# 2의 배수라고 해석하면 안된다. step의 개념이다
print(list(range(5,10,2)))
"""

"""
# ex22) 삼항연산( 1. if else 2. 대입받는 변수가 같은가
# 1번
num = 0
if 3 > 2:
    num = 10
else:
    num = 20

print(num)
# 2번 삼항연산
num = 10 if 3 > 2 else 20
print(num)

# 3번 1. if else를 사용하고 있는가? 2. 대입받는 변수가 같은가?
if num % 2 == 0:
    num = num // 2
else:
        num = num *3 + 1

# 4번
num = 23
num = num // 2 if num % 2 == 0 else num * 3 + 1
print(num)

# 5번
if 3 > 2:
    print('호랑이')
else:
    print('코끼리')

# 6번 5번문제를 삼항연수로 바꾸었을때
print('호랑이' if 3 > 2 else '코끼리')
"""
# 결과적으로 if 조건이 만족하면 앞에 있는것을 대입또는 출력하고
# 그렇지 않은경우에는 뒤에 있는 것을 대입 또는 출력한다.


"""
# ex21) while:반복횟수를 모를때,for: 반복횟수를 알때

# 1. 얘가 그렇다는 거다, 사용안하는 방식
a = 0
while a < 5:
    print(a)
    # a++ 단함 연산자가 없다
    # a = a + 1
    a += 1

print('while 종료')

# 2번
a = 0
while a < 10:
    print(a)
    a += 1

    if a == 3:
        print('컨디뉴 사용됨')
        continue

    if a == 6:
        print('브레이크')
        break

# 3번
a = 0
while True:
    print(a, end=' ')
    if a == 4:
        print()
        break

    a += 1
print('-' * 40)
# 4 : 우박수 출력 프로그램
num = 9

while True:
    print(num)

    if num == 1 :
        print('탈출하기 일보직전')
        break

    if num % 2 == 0:
        num = num //2
    else:
        num = num *3 + 1
print('while 문 탈출 되었음')

# 5번
while True:
    data = int(input('비밀번호를 입력하세요'))
    if data == 9999:
        print('홈페이지로 이동합니다')
        break
    print('패스워드가 맞지 않습니다')
"""


"""
# ex20) if가 false라고 판단하는경우
if None: #     False,[],(),{},None,0,' '
    print('True')
else:
    print('False')
"""

"""
# ex19)
a = 4
b = 3
# 1번
if a > b:
    print(1)
else:
    print(2)
# 2번
if a > b:
    if a+2 > b+2:
        print(1)
    else:
        print(2)
else:
    if a-10 > b-4:
        print(3)
    else:
        print(4)

print('='*30)
# 3번
jumsu = 87
if jumsu >= 90:
    print('A학점입니다')
elif jumsu >=80:
    print('B학점입니다')
elif jumsu >=70:
    print('C학점입니다')
elif jumsu >=60:
    print('D학점입니다')
else:
    print('F학점입니다')

# 4번
# list : 데이터들의 집합 + CRUD
print(type([]))
print(type([10, 20, 30, 40]))

if 10 in [10, 20, 30, 40]:
    print('호랑이1')

if 'lion' in ['tiger, lion, cat, dog']:
    print('호랑이2')
else:
    print('호랑이3')

# 5번 (find 비슷한 프로그램이다)
s1 = '무궁화 꽃이 피었 습니다'
s2 = s1.split(' ')
print(s2)
if '꽃이' in s2:
    print('find')
else:
    print('not found')
"""

"""
# ex18) if, while, for (swtich 없다)
# if
# 1번
if True:
    print('호랑이1')
# 2번
if False:
    print('호랑이2')
    # 줄바꿈을 해서 헷갈리지 않게 하기
print('호랑이3')
# 3번
if False:
    print('호랑이2')
    print('호랑이3')

# 4번
a = 30
b = 20
if a > b:
    print('호랑이6')

    if a - 20 > 0:
        print('호랑이7')   
    print('호랑이8')

print('호랑이9')

"""


"""
# ex17) 키 입력 프로그램
# print('숫자를 입력하시오')
# data = input()
# print('호랑이',type(data)) # str

# data = input('숫자를 입력하시오')
# print('호랑이',type(data))

data = int(input('숫자를 입력하시오'))
print(type(data+100))    # int
"""

"""
# ex15)
# and or
# 논리연산 : and, or,not
print(False or False)  # False
print(False or True)   # True
print(True or False)   # True
print(True or True)    # True

print(not True)
print(not(3 > 2))      # True

print(False or False or False)     # Fasle
print(3 < 2 or 10!=10 or True)     # True
"""

"""
# ex14)
print(30 > 20)
print(30 >=20)
print(30 < 20)
print(30 <= 20)
print(30 == 20)
print(30 != 20)

apple = 30 > 20
print(type(apple), apple)
"""


"""
# ex13)
# all replace
s = '무궁화 꽃이 피었습니다 무궁화'
print(s.replace('무궁화','소나무'))
a = s.replace('무궁화','소나무')
print(a)
print(s.split())
a = s.split()
#     ['무궁화', '꽃이', '피었습니다', '무궁화']
print(type([]))   # list
print(type(a))    # list
#     ['무궁화', '꽃이', '피었습니다', '무궁화']
print(a)
print(a[0],a[3])

print('-'*20)
s = '무궁,화 꽃,이 피었,습니다 무,궁화'
# print(s.split())
print(s.split(','))
"""


"""
# ex12)
s = '꽃무궁화꽃이피었습니다꽃'
print(len(s))
print(s.count('꽃'))
# 무궁화 라는 단어가 있는지 없는지 확인
# 찾았을때의 인덱스가 알려준다.
print(s.find('피었습니다'))
# 못찾으면 -1로 알려준다.
print(s.find('호랑이'))

s = 'Apple'     # 문자열 생성
print(id(s))
s = s + "banana"   # 문자열 추가
print(id(s))
print(s)
print(s.upper())  # 대문자
print(s.lower())  # 소문자
# 위의 결과를 확인했는데 s의 내용이 변경된것인지 아닌지 확인
print(s)
# 여기서는 실제로 변경되었다.
s = s.upper()
print(s)
"""


"""
# ex11)
print('호%d랑%s이' %(10,'무궁화'))
print('%d' % 10) # 1개를 치환할때는 갈호 생략 가능
a = '호{0}랑{1}이'.format(10,'무궁화')
print(a)
print('호{0}랑{1}이'.format(10,'무궁화'))

s = '호{0}랑{1}이'
a = s.format(10,'무궁화')
print(a)
"""


"""
# ex10) 문자열에 대한 내용이다

apple = '무궁화꽃이피었습니다'
#         0123456789 (양수)
banana = "abcdefghij"
#          987654321(음수라고 가정)
# 여기서 사용하는 0을 인덱스라고 한다
# [0]를 이용한 그 안의 내용물 : 요소
print(apple[0],apple[9])
print(apple[-1], apple[-10])
print(apple[2:5]) # 2번부터 5번 앞까지
print(apple[5:]) # 5번부터 끝까지
print(apple[:5]) # 시작부터 5번 앞까지
print(apple[:]) # 시작부터 끝까지

a = apple[5:]
print(a)

# 주의 사항
print(apple[0])
a = apple[0]
print(0)
# 문자열은 문자열 상수로 정의된것이다
# apple[0] = '호' (error)

print('소'+ apple[1:])
# len = length
print(len(apple))  # 10

print(apple[:len(apple)]) # 시작부터 10번앞까지
"""

"""# ex9)
# 1)
print(3 + 8)

# 2)
a = 3 + 8
print(a)

# 3)
b = 2** 8
print(b)

# 4)
print(round(3.145, 2)) # 3.15
print(round(3.144, 2)) # 3.14
print("호랑이"*3)
"""




"""# ex8) 식별변호를 알고 싶을때 (id)
a = 10
b = 20
c = 30
print(id(a));
print(id(b));
print(id(c));

a = '호랑이'
b = '호랑이'
c = '코끼리'
print(id(a));
print(id(b)); # 아이디가 중복되서 나온다
print(id(c));

print(17/4)
print(17//4)
print(17%4)
"""


"""# ex7) 데이터 교환
a , b = 10, 20
print(a,b)
temp = a
a = b
b = temp
print(a, b)

c, d = 30, 40
print(c, d)
d, c = c, d;
print(c, d)
"""

"""# ex6)
# int a = 10;
a = 10
print(type(a))
a = '호랑이'
print(type(a))
a = 3.14
print(type(a))
a = []
print(type(a))
a = ()
print(type(a))
a = {}
print(type(a))

a, b, c = 10, 20 ,30
print(a,b,c);
# error
# a =10 , b = 20
a = 10; b = 20; c = 30
"""


"""# ex5) 
# 숫자 + 숫자
print(30+40)
# 숫자 + 문자(문법에러)
#print(30+'호랑이')
# 문자(문법에러)+ 숫자
#print('호랑이'+30)
# 문자열 + 문자열 = 문자열 연결
print('호랑이'+'코끼리')
# 문자열이다.
print(type('123'))

#print('123'+456)  >> 에러
# 문자열로 만들어 놓고 산술연살을 해야할때가
# 비일비재하게 일어난다.
# 문자열을 숫자로 만들어 주세요.(int)
print(int('123'))
print(type(int('123')))
print(int('123')+123)
print(type(str(40)))
print('호랑이'+str(40))
"""




"""# ex4) 산술연산
print(17+3)
print(17-3)
print(17*3)
# 모든 결과가 나타난다.(5.6666667)
print(17/3)
# % 나머지 값
print(17%3)
# 결과가 35가 아니다.
# 기본적으로 연산은 촤측에서 우측으로 일어난다
# *,/,% 는 =-보다 연산 우선순위가 높다.
print(3+4*5)
print((3+4)*5) # 결과 35
print((3+4)*(5+6)) # 7 * 11
"""









"""# ex3) type(형)
# 너 누구냐 ? int인데요 integer; 정수
print(type(20))
# str ; string(문자열)
print(type('호랑이'))
# float ; 실수
print(type(3.14))
# boolean
print(type(True))
# list : n개의 데이터 + CRUD 기능
print(type([]))
# dictionary : 사전
print(type({}))
# tuple 
print(type(()))"""




"""
# ex2) print
print(10)

print(10,20,30)
# 문자가 1개 이상인것을 문자열이라고 한다.
# 싱글 코테이션을 이용해서 문자열을 표시한다.
print('호랑이')

print(10,'호랑이',3.14,True,False)
# 정수,문자열,실수,참/거짓

# ; 을 이용하여 한줄 코드 처리
print(100);print(200);

# print(300) >> 코드는 생략된 형태이다
# \n (캐리지 리턴; 줄바꿈표시
print(300,end='\n');
print(400,end='코끼리'); # 적당하게 응용
print(500);
print('=======================')
print('호랑이' * 4)

#문자열 포맷(치환을 시킬수가 있다.)
print('%d %s' %(123,'독수리'))
print('코%d끼%s리' %(456,'앵무새'))
# 디폴트
print(10,20,30, sep=',',end='\n')
# 응용
print(10,20,30, sep=',',end='\n\n')
print('test')
"""

"""
# ex1)
# print(100);

print(200);
print(200);
print(200);
 """
