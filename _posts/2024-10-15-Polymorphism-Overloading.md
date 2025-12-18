---
layout: post
title: "[Polymorphism] Overloading"
date: 2024-10-15 13:53:15 +0900
categories: [Computer Science, Object Oriented Programming]
tags: [매크로, 템플릿, 다형성, 오버로딩, 네임스페이스]
---

cpp 에서는 함수 원형이 달라지면 이름이 같아도 다른 함수가 된다. c와 중요한 차이점이다. 

 

# Overloading

함수 원형(반환 형식(type), 호출 규칙, 함수 이름, Argument 구성) 중 함수 이름을 제외하고 다르게 변경할 수 있다. 그러나 반환 형식이나 호출 규칙만 다른 경우는 문법에 맞지 않다. 즉, 함수를 이름은 같고 내용은 다르게 재정의할 수 있다. 

- int Add(int a, int b) {} 

- double Add(double a, double b) {}

- int Add(int a, int b, int c) {}

 

호출자 관점에서 호출되는 함수는 컴파일러에 의해 자동으로 결정된다. 

-> 모호성

```cpp
void TestFunc(int a)
{ std::cout << "TestFunc(int)" << std::endl;}

void TestFunc(int a, int b = 10)
{ std::cout << "TestFunc(int, int)" << std::endl;}

int main(int argc, char* argv[])
{ 
	TestFunc(5);
	return 0;
}
```

위 코드는 컴파일할 수 있는가?

2번째 TestFunc는 디폴트 매개변수를 가지기 때문에 호출자가 실인수를 기술하지 않아도 두 번째 매개변수에 10이 적용된다. 

호출자의 관점에서 overload func 호출이 **모호**하여 컴파일 오류가 발생한다. overloading 자체에는 문법적 오류가 없다. 

 

# Template

overloading은 다른 반환, 매개변수를 가지려면 모든 해당 함수가 일일이 존재해야 한다. 메모리, 인력 효율을 위해 템플릿을 이용한다. 

함수 위에 template<typename T> 만 붙여주면 된다. 

```cpp
template <typename T>
T tesfunc(T a) { return ; }

int main(int argc, char* argv[])
{ 
	std::cout << testfunc(3) << std::endl;
    std::cout << testfunc(3.3) << std::endl;
    std::cout << testfunc('A') << std::endl;
    std::cout << testfunc("String") << std::endl;
    
    //<typename T> - <int> 지정
	std::cout << testfunc<int>(3) << std::endl;
    
	return 0;
}
```

typename은 자료형을 의미하며 판화 틀처럼 구멍 난 부분의 역할을 한다. 호출자가 어떤 실인수로 함수를 호출하는가에 따라 자동으로 overloading 된다. 즉, 사용자 코드에 의해 컴파일러가 overloading 한다. 

 

# 매크로

함수를 호출하면 스택 메모리 사용으로 매개변수 복사(메모리 복사), 스택 조정, 제어 이동 등 내부에서 여러 연산이 일어난다. 호출로 인한 오버헤드를 극복하고자 매크로를 이용한다. 매크로는 함수 호출을 하지 않는다. 함수가 아니기 때문이다. 따라서 엄청난 성능 향상이 있을 수 있지만 자료형을 지정할 수 없어 논리적 오류를 발생시키기도 한다. 

```cpp
// 매크로
#define ADD(a, b) ((a) + (b))

// 일반 함수
int Add(int a, int b) { return a+b; }

int main(int argc, char* argv[]){
	int a, b;
    scanf_s("%d%d", &a, &b);
    
    printf("ADD(): %d", ADD(a,b));
    printf("Add(): %d", Add(a,b));
    
    return 0;
}
```

 

 

# 네임스페이스

Namespace는 소속 집단명이다. cpp가 지원하는 각종 요소(변수, 함수, 클래스)를 한 범주로 묶어주기 위한 문법이다. 

코드의 소속을 나누면 규모가 큰 프로그램 관리에 좋다. 식별자에 붙이는 이름은 다 거기서 거기이기 때문에 네임스페이스를 잘 활용한다면 이름이 겹쳐서 발생하는 문제를 한 번에 해결할 수 있다. 

C++ 에서 네임스페이스에 속하지 않은 식별자는 없다. 전역 함수도 ::testfunc 라고 네임스페이스를 가진다. 

 

Queue를 직접 구현한 코드로 template 가 어떻게 사용되는지 보자

```cpp
#define MAX_ITEMS 50

template<class ItemType>
class QueueType
{
private:
    ItemType *     data; // dynamic array implementation
    int         front; // the index of the front element
    int         rear; // the index of the rear element
    int         maxQueue; // the MAX size of the queue
    
public:
    QueueType(int maxQue);
    void        enqueue(ItemType value);
    ItemType    dequeue( );
    void        clear( );
    bool        isFull( ) const;
    bool        isEmpty( ) const;
    void        printQueue( ) const;
};

template<class ItemType>
QueueType<ItemType>::QueueType(int maxQue){
    // Constructor -- No return type
    maxQueue = maxQue + 1;
    front = maxQueue - 1;
    rear= maxQueue - 1;
    data = new ItemType[maxQueue];
}

template<class ItemType>
ItemType QueueType<ItemType>::dequeue( ) {
    ItemType ret;
    if(isEmpty()){
        cout << "[ERROR] Queue is Empty. Dequeue Failed." << endl;
        location temp(-1,-1);
        return temp;
    }
    front = (front + 1) % maxQueue ;
    ret = data[front];
```

template<class > ? typename이 아니네요. class는 클래스만 지정하기 위한건가요?

역사적으로 class가 먼저 사용되던 용어이고 이후에 타입을 표현하기 위해 더 명확한 표현인 typename이 추가되었다. 결론적으로 동일한 동작을 한다. 

 

## 클래스를 소속으로 가진다. 

template<class ItemType>

반환 타입 클래스<ItemType> :: 클래스 메서드 

클래스는 객체 지향의 핵심이다. 이제 다음 글에서 클래스를 다루겠다.