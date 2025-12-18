---
layout: post
title: "Linear/Polynomial Regression"
date: 2024-10-13 20:51:44 +0900
categories: [Data Science, Machine Learning]
---

기계학습 선형, 다항 회귀 모델 실습하기

 

# Linear Regression Model 

2차원 평면 상 데이터에 대해 해당 데이터를 잘 표현할 수 있는 선형 회귀 모델

1. Loading the dataset

```python
# Generate 2-dimensional
X = [rand() * i * 0.5 - 20 for i in range(0, 100)]
y = [x ** 3 * 0.002 - x ** 2 * 0.005 + x * 0.003 + rand() * 5 for x in X]
```

 

2. 데이터셋을 trainset & testset로 나누고 분포 시각화

```python
# Data random shuffle
idx = list(range(length(x)))
random.shuffle(idx)

# Split data for train/test 2: 8
X_train, X_test = [X[i] for i in idx[:80]], [X[i] for i in idx[80:]]
y_train, y_test = [y[i] for i in idx[:80]], [y[i] for i in idx[80:]]
```

```python
# Visualization of trainset

import matplotlib.pyplot as plt

plt.scatter([i for idx, i in enumerate(X_train)], [i for idx, i in enumerate(y_train)],
			label = 'Train', marker = 'o')

plt.scatter([i for idx, i in enumerate(X_test)], [i for idx, i in enumerate(y_test)],
			label = 'Test', marker = 'x', color = 'r')

plt.title('Data points')
plt.xlabel('X')
plt.ylabel('y')
plt.ylim([-20, 20])
plt.legend()
plt.show()
```

Python 문법 : i for idx, i in enumerate(X_test) 

enumerate는 괄호 안에 값을 (인덱스, 값) 쌍으로 반환한다. idx에 인덱스, i 에 값을 나타내는 것이다. 

i for ... 은 i만 리스트로 모으겠다는 뜻으로 즉, X_test의 값만을 리스트로 추출해 반환한다.

 

3. Linear Regression Model

```python
import math
import numpy as np

class Lienar():
	# initialize weights and bias
	def __init__(self):
    	self.weight = rand()
        self.bias = 0
        self.lr = 5e-4 #learning rate =0.0005   
    
    # Predict the output based on the weighted sum of Linear regression model
    def forward(self, x):
    	prediction = self.weight * X + self.bias
        return prediction
        
    # Compute the prediction error to gain the model weight
    def backward(self, x, y):
    	pred = self.forward(x)
        errors = pred - y
        return errors
        
    # Iterate forward and backward to update model weights
    def train(self, x, y, epochs):
    	for e in range(epochs):
        	for i in range(len(y)): # Stochastic GD : 각 학습 데이터 포인트마다 한 번씩 가중치 업데이트
            	x_, y_ = x[i], y[i]
                
             # To calculate gradient of the model by the sample
             errors = self.backward(x_, y_)
             gradient_weight = errors * x_
             gradient_bias = errors * 1
             
             # To update the weight and bias with backward()
             self.weight -= gradient_weight * self.lr
             self.bias -= gradient_bias * self.lr
    
    def evaluate(self, x):
    	predictions = [self.forward(x_) for x_ in x]
        return predictions # list type
```

 

gradient는 왜 에러에 x를 곱하는가?

기울기의 직관적인 의미는 가중치가 변화할 때 입력 x가 모델 output에 미치는 영향을 나타낸다. 입력 x가 클수록 가중치 w의 변화가 모델 예측에 더 큰 영향을 미치기 때문에, 에러와 입력을 곱해서 가중치의 업데이트 방향과 크기를 결정하게 됩니다.

bias는 ?

편향 b에 대한 기울기는 x와 무관하게 항상 1이므로, 에러(error)에 단순히 1을 곱합니다. 편향은 모든 입력에 대해 일정하게 적용되므로, b는 입력과 상관없이 **에러만 반영**하여 업데이트됩니다.

 

4. 학습 및 결과 시각화

```python
# Define a model
linear = Linear()

# Training
linear.train(X_train, y_train, 100) 

# Print weight and bias 6자리까지
print(f"weight: {linear.weight: 0.6f}")
print(f"bias: {linear.bias: 0.6f}")
```

```python
# Range of X
x = np.linspace(-20, 20, 50)

# Plotting linear
plt.plot(x, linear.forward(x), label = 'Prediction')

# Plotting test data points
plt.scatter([i for idx, i in enumerate(X_test)],
			[i for idx, i in enumerate(y_test)],
            label = 'Test', marker ='x', color ='r')
            
# Calculate MSE
mse = sum([(y-linear.forward(x))** 2 for x, y in zip(X_test, y_test)])

plt.title(f'Data points (MSE : {mse:0.3f})')
'''
```

 

# Polynomial Regression Model

1. 다항 회귀 모델 구현

 

2. 다항 회귀 모델 학습 및 시각화

```python
# Model define and training

# Define a model
polynomial = Polynomial(dim = 2, lr = 1e-6)

# Training
polynomial.train(X_train, y_train, 100)

# Print weights and bias
for i, weight in enumerate(polynomial.weights):
	print(f"weight_{i+1}: {weight:0.6f}")
print(f"bias: {polynomial.bias:0.6f}")
```

```python
# Plotting polynomial and data points

# Range of X
x = np.linspace(-20, 20, 50)

# Plotting test data points
plt.scatter([i for idx, i in enumerate(X_test)],
			[i for idx, i in enumerate(y_test)],
            label = 'Test', marker = 'x', color = 'r')
            
# Calculate MSE of test data
mse = sum([y - polynomial.forward(x))**2 for x, y in zip(X_test, y_test)]) / len(X_test)

plt.title(f'Data points (MSE: {mse:0.3f})')
plt.xlabel('x')
~
```

mse = sum([(y - polynomial.forward(x))** 2 for x, y in zip(X_test, y_test)]) / len(X_test)

- **2 는 제곱을 의미합니다.

- zip( , ) 은 iterable들을 짝지어 주는 함수로 X_test, y_test 의 각 요소를 순서대로 짝지어서 (x, y)로 반환합니다.

 

> 여기서부턴 다음 글로! 

3. 다항 회귀 모델 분석: 최적화

손실함수를 최소화하기 위한 dim, lr을 구해라!

[https://hazel01.tistory.com/36](https://hazel01.tistory.com/36)

[[ Deep Learning 02 ] 경사하강 학습법 ( Gradient Descent ) , 옵티 마이저 ( Optimizer )Deep Learning 02. 경사하강 학습법 1. 모델을 학습하기 위한 기본적인 용어 1.1. 학습 매개변수 ( Trainable Parameters ) : 학습 과정에서 값이 변화하는 매개변수 : 매개변수가 변화하면서, 알고리즘 출력이hazel01.tistory.com](https://hazel01.tistory.com/36)
 

## Feature Normalization의 역할

Feature Scaling