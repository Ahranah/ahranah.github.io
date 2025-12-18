---
layout: post
title: "Computer Architecture_MIPS Code Examples(1)"
date: 2024-07-01 01:48:12 +0900
categories: [Computer Science, Computer Structure]
tags: [recursive, 재귀함수, mips, Assembly, 어셈블리어, nested procedure, 피드백환영, 아는척은금지]
---

DP 프로그래밍에서 재귀함수를 이용했어요. 재귀함수 호출이 메모리에 어떻게 할당되는지 단계들을 살펴보면 복습에도 좋을 것 같아서! 다뤄보고자 합니다. 

#### 큰 그림은 다음 4 단계로 이루어집니다.

(1) High level language to assmebly 
(2) Pipeline에서 어셈블리어의 실행 
(3) CPU에서 Cache Memory 이용 
(4) TLB와 Page Table의 실행 과정  

기회가 된다면 File system 실행도 다뤄보고 싶어요! (먼 산)

---