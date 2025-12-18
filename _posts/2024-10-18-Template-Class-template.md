---
layout: post
title: "[Template] Class template"
date: 2024-10-18 02:06:02 +0900
categories: [Computer Science, Object Oriented Programming]
tags: [클래스, 템플릿, 매개변수]
---

# 함수 템플릿과 클래스 템플릿

템플릿을 함수에서 사용할 수 있고 클래스에서 사용할 수 있다. 둘 다 **틀** 로 사용하는 것인데 함수 수준에서 클래스 수준으로 확대된 것만 다르다.

# 템플릿

템플릿은 overloading에서 함수를 특정 사용 매개변수, 반환 형식에 따라 여러 번 작성해줘야 한다는 불편함을 위해 효율적인 메모리와 시간 관리를 위해 나온 개념이다.

```cpp
// function template 
template <typename tem>
tem function(tem arg){ std::cout << "argument: " << arg << std::endl; return arg; }

int main(int arg, char* argv[]){
    std::cout << function(3) << function('A') << function("String") << function(3.3) << std:endl; }

// class template     
template <class ItemType>
class SortedType 
{
private: 
    ItemType data[MAX_ITEMS];
    int length;
public:
    SortedType();
    void insertItem(ItemType value);
    bool findItem(ItemType & item);
    ItemType getItem(int pos);
};

template <class ItemType>
ItemType SortedType<ItemType>::getItem(int pos){
    if (pos < length){
    return data[pos]; 
    } else { return -1; } ;

int main(int arg, char* argv[]){
    SortedType<int> sList;
    SortedType<char> charList;
}
```

## 클래스 템플릿 주의 사항

1. 멤버 선언과 정의를 분리할 때에는 기술할 때마다 template</typename/>을 매번 선언해야 한다.
2. 클래스 밖에서 멤버를 정의할 때에 클래스 이름 옆에 </typename/>을 기술해야 한다.
3. 인스턴스 선언할 때 반드시 </typename/> 을 지정해줘야 한다.

클래스 밖에서 정의하는 경우 </typename/> 를 기술하거나 지정해줘야 한다!
각각 자료형에 맞게끔 만들어진 인스턴스는 **템플릿 클래스** 라고 부른다. 모두 동일한 멤버를 가진다.

이게 다입니다. 굳이 써야 할까?

어떤 형식이든 배열로 관리할 수 있는 구현이 가능하다. 그럼 템플릿에서 구조적으로 메모리 자동 동적 할당 및 해제하며 복사 생성자와 이동 시맨틱을 지원하므로 성능도 좋다.

```abnf
Class<int> arr(5);
Class<int> arr2(3);
arr2 = arr; 
```

이런 코드도 오류 없이 메모리를 r-value에 맞춰 새로 생성해 문제없이 넘어갈 수 있도록 구현이 가능하다는 것이다. 추가로 템플릿도 다중 정의, 상속이 가능하다.

그것은 나중에 ~

# 템플릿 매개변수

템플릿 매개변수는 클래스 템플릿 내부에서 모두 접근 가능하다. 멤버 변수처럼요. 디폴트 값도 지정 가능하다.
생성자의 매개변수로 개수를 입력받는 방식 대신 사용할 수 있다.

```angelscript
template<typename Type = int, int nSize = 3>
class Arraytype
{ 
private:
    int* m_pData;
public:
    Arraytype(){ m_pData = new Type[nSize] };
    // Arraytype(int nParam) { m_pData = new int[nParam];}

    ~Arraytype() {delete [] m_pDate; } ;

int main(){
    Arraytype<int, 3> arr;
    arr[0] = 10;
    Arraytype< > arr2;

    // Arraytype a(3);
```

템플릿을 사용한 방식과 생성자 매개변수로 입력 받는 방식을 확인할 수 있다.

end