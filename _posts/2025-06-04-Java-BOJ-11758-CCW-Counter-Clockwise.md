---
layout: post
title: "[Java][BOJ 11758] CCW: Counter-Clockwise"
date: 2025-06-04 11:45:45 +0900
categories: [Algorithm, 백준]
---

## 문제

## 문제 파악

첫째 줄에 P1의 (x1, y1), 둘째 줄에 P2의 (x2, y2), 셋째 줄에 P3의 (x3, y3)가 주어진다. (-10,000 ≤ x1, y1, x2, y2, x3, y3 ≤ 10,000) 모든 좌표는 정수이다. P1, P2, P3의 좌표는 서로 다르다.

P1, P2, P3를 순서대로 이은 선분이 반시계 방향을 나타내면 1, 시계 방향이면 -1, 일직선이면 0을 출력한다.

## 접근 방법

기하의 핵심이론 CCW

CCW(Counter-Clockwise): 평면상의 3개의 점과 관련된 점의 위치 관계를 판단하는 알고리즘

이를 이해하기 위해선 벡터의 외적 개념 이해가 필요하다. 

{% include figure.liquid loading="eager" path="assets/img/posts/2025-06-04-java-boj-11758-ccw-counter-clo/img.png" class="img-fluid rounded z-depth-1" %}

CCW = (X1Y2 + X2Y3 + X3Y1) - (X2Y1 + X3Y2 + X1Y3)

벡터의 외적이 |CCW| / 2는 세 점으로 이뤄진 삼각형의 넓이로 이해하면 된다. 

{% include figure.liquid loading="eager" path="assets/img/posts/2025-06-04-java-boj-11758-ccw-counter-clo/img_1.png" class="img-fluid rounded z-depth-1" %}

1. 1번째 점을 뒤에 한 번 더 씁니다.

2. 오른쪽 아래 방향 화살표 곱은 더하고, 왼쪽 아래 방향 화살표의 곱은 뺍니다. 

사진 출처와 더 자세한 정보는 

[기하 - CCW 활용1. CCW 기하 관련 문제를 풀이할 때, 필수적으로 알아두어야 하는 알고리즘으로 CCW(Counter-Clockwise)가 있다. 여기서 CCW란, 벡터의 외적을 이용하여 3개의 점에 대한 위치 관계를 판단하는 알고리즘이velog.io](https://velog.io/@gmlstjq123/%EA%B8%B0%ED%95%98-CCW)

## 

[[알고리즘] CCW(백준11758번)_골드5_기하학, 기하, 벡터, 외적, 신발끈문제링크 ? 문제 2차원 좌표 평면 위에 있는 점 3개 P1, P2, P3가 주어진다. P1, P2, P3를 순서대로 이은 선분이 어떤 방향을 이루고 있는지 구하는 프로그램을 작성하시오. 입력 첫째 줄에 P1의 (x1, y1g4daclom.tistory.com](https://g4daclom.tistory.com/162)
 

## 코드 구현

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int x1 = input.nextInt();
        int y1 = input.nextInt();
        int x2 = input.nextInt();
        int y2 = input.nextInt();
        int x3 = input.nextInt();
        int y3 = input.nextInt();
        
        int ccw = (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3);
        if (ccw == 0) {
            System.out.println(0);
        } else if (ccw > 0) {
            System.out.println(1);
        } else System.out.println(-1);
    }
}
```

 

## 배우게 된 점

 

## 질문