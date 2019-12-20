# 2019_AI_Final 2015108189 김한주

# 에어비엔비 데이터를 이용하여 방갯수와 침대갯수로 숙박비용 예측하기
에어비엔비 데이터 출처 : https://velog.io/@leejh3224/Machine-Learning-%EC%97%90%EC%96%B4%EB%B9%84%EC%95%A4%EB%B9%84-%EA%B0%80%EA%B2%A9-%EC%98%88%EC%B8%A1

수업시간 때 이용하였던 predictionutil 라이브러리를 이용했습니다!

# 데이터 불러오기

![모든데이터.PNG](./모든데이터.PNG)


```
from prediction_util import PredictionUtil as xxx

gildong = xxx()
gildong.read('airbnb.csv')
gildong.show_unique_column()
```

![유니크.PNG](./유니크.PNG)

# 불필요한 데이터 속성 제거

현재 데이터에는 불필요한 id, minimum_nights, maximumnights, number_of_reviews가 있어서 제거합니다

`
gildong.drop(['id', 'minimum_nights', 'maximum_nights', 'number_of_reviews'])
`

# 데이터 분석하기

`
gildong.heatmap(['accommodates', 'bathrooms', 'bedrooms', 'beds', 'price'])
`

![히트맵.PNG](./히트맵.PNG)

히트맵 결과 accommodates, bedrooms, beds가 관련이 높다는것을 볼 수 있습니다

`
gildong.plot_3d('bedrooms', 'beds', 'price')
`

![3d.PNG](./3d.PNG)

beds와 bedrooms가 높을수록 가격이 높은 것을 알수있습니다

# 데이터 학습 및 예측

## 1. LinearRegression

`
gildong.run_linear_regress(['accommodates', 'bedrooms', 'beds'], 'price')
`

## 2. KNeighborsRegressor

`
gildong.run_kneighbor_regress(['accommodates', 'bedrooms', 'beds'], 'price')
`

## 3. DecisionTreeRegressor

`
gildong.run_decision_tree(['accommodates', 'bedrooms', 'beds'], 'price')
`
 
## 4.RandomForestRegressor

`
gildong.run_random_forest(['accommodates', 'bedrooms', 'beds'], 'price')
`

## 5. 4가지 방법 동시실행

`
gildong.run_all(['accommodates', 'bedrooms', 'beds'], 'price')
`

# 오류...???

수업시간에 배운 내용처러 나름 열심히 해봤는데 마지막에서 오류가 났습니다..
열심히 찾아봤는데 아무리 해봐도 어디서 잘못된건지 잘모르겠습니다.. ㅠㅠ

이번 수업을 통해서 머신러닝이 어떻게 이루어지는지 조금이라도 알게 되어서 유익한 시간이었던것 같습니다!!
