---
layout: post
title: "[Contiguous data structures] List"
date: 2024-10-20 02:38:19 +0900
categories: [Computer Science, Data Structure]
---

# basics

C++ 을 사용하기에 앞서 C++을 사용한 Object Oriented Programming이 어떤 것이고 쓰면 뭐가 좋은지 살펴본다.
OOP는 data 와 operation(method)를 하나로 묶어서 구조체 형태로 사용하는데 이를 ADT라고 한다. 학생 데이터 베이스에 학생 정보만 있는게 아니라 학생 정보를 관리할 동작(추가, 삭제 등)을 하나로 보는 것이다.

## ADT(Abstract Data Type)

어떻게 해야 사용할 수 있을 지가 아니라 어떤 기능을 사용할 수 있을 지 알려주기 위한 구조

Tell what the program must do, but not how

public interfaces/methods만을 통해 데이터에 접근할 수 있으므로 접근 제어 가능

- 
- encapsulationData + Operation

구현과 독립되어 명시된 자료 구조로 요소의 조직, 관리, 저장 방식을 정의한다. 사용자의 관점에서 접근과 수정이 훨씬 쉬워진다.
-> 시스템 사용자 관점에 필수적인 구조!

### ADT basic operations

append
insert
remove
update
clear

size
isFull
find
getItem

- 

## Abstraction

구현으로부터 논리적 특성을 분리했다. = values와 operation만 생각한다.
예를 들면, 학생 이름(value)를 한 번에 관리하려면 추가 기능(add)이 필요하겠군 이렇게만 생각하고 어떤 data type, 내부 논리(this -> name), 메모리 관리 등은 고려하지 않아도 된다는 것이다.

---