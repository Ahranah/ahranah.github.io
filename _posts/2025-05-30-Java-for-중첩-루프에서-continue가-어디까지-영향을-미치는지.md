---
layout: post
title: "[Java] for 중첩 루프에서 continue가 어디까지 영향을 미치는지"
date: 2025-05-30 17:32:07 +0900
categories: [Computer Science, Object Oriented Programming]
---

while, for, switch 문 내에서 continue의 동작 범위가 어디까지 인지, 그리고 자주 혼동되는 케이스인 switch 문과의 관계에 대해서도 살펴본다.

## 기본 개념:continue는 루프 제어문

continue는 **루프의 다음 반복으로 건너뛰는 제어문**이다. 즉, 아래 구조에서 continue는 for 또는 while 루프의 **현재 반복을 종료하고 다음 반복으로 진행**한다.

```angelscript
for (int i = 0; i < 5; i++) {
    if (i == 2) continue;
    System.out.println(i);
}
```

출력 결과:

```angelscript
0
1
3
4
```

 

---