import pandas as pd
import numpy as np

result = pd.read_csv('2020년 1월_2월.csv')
print(result)
print(result.describe())
print('-'*50)
#카테고리별 거래금액 : price
price = result.filter(items=('카테고리', '거래금액'))
print(price)

price2 = price.groupby('카테고리').sum()
print(price2)

print('-'*50)
#카테고리별 남녀 사용 비율 : sex
sex = result['고객 성별'].value_counts()
print(sex)

sex1 = result.filter(items=('카테고리', '고객 성별'))
print(sex1)

sex2 = sex1.value_counts()
print(sex2)

#aaa

#pd.pivot_table에서 열이름을 못찾겠음

