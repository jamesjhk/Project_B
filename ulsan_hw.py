import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1.파일을 데이터프레임으로 변환 df에 저장
df=pd.read_csv('2020년+1월_2월.csv')
print(df)
print('-1'*100)
print('\n')

#2.인덱스 타입
print(type(df))
print('-2'*100)
print('\n')

#3.인덱스 갯수
print(df.index)
print('-3'*100)
print('\n')

#4.컬럼별 type
print(df.info())
print('-4'*100)
print('\n')

#5.거래금액별 정렬 및 총합계금액
acount=df.sort_values(by='거래금액',ascending=False)
total_acount=df['거래금액'].sum()
print(acount)
print(total_acount)
print('-5'*100)
print('\n')


#6.고객생년월일별 남녀별 거래금액
df1=df.pivot_table(values='거래금액', index='고객 생년월일', columns='고객 성별', aggfunc=sum)
print(df1)
print('-6'*100)
print('\n')

#생년을 나이로 바꾸어 열추가하기
df['나이']=2020-(df['고객 생년월일'])+1
print(df)
print('-7'*100)
print('\n')


# 나이로 연령대 열 추가하기
df['연령대']=np.trunc((df['나이'])/10)*10

#def generation(x):
#    return(int(age)+"대")
#여기가 문제인데 아직 age값을 받지도 않은 이 generation함수가 이렇게될까요?
#age=int(input())

print(df)
print('-8'*100)
print('\n')

#연령대별 거래금액, 각 연령대별 남녀 분리
df_age=df.pivot_table(values='거래금액', index='연령대', columns='고객 성별', aggfunc=sum)
print(df_age)
print('-9'*100)
print('\n')

#남녀 옆에 총합을 구하고 싶은데...어떻게 할까요?열추가로....


#각 연령대별 1인당 평균 거래금액

#그래프그릴때 한글폰트지원
import matplotlib.font_manager as fm
font_name = fm.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family=font_name)

#그래프 figure생성(항상 먼저 종이를 만들어야한다)
fig = plt.figure(figsize=(20,5))

#그래프 스타일 서식지정
plt.style.use('ggplot')

#x축 눈금 라벨 회전하기
plt.xticks(size=10, rotation=75) #년도별로 묶은 자료가 있어야 년도별로 표시됨. 아직 못만듦

#그래프 출력
plt.plot(df1.index,df1.values,marker='.')
plt.show()
print('-10'*100)
print('\n')

