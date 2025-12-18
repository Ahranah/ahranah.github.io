---
layout: post
title: "[Class] Method"
date: 2024-10-16 17:40:15 +0900
categories: [Computer Science, Object Oriented Programming]
tags: [인터페이스, static, const, this-pointer, 메서드, 멤버함수, 정적 멤버]
---

Method a.k.a. Interface Function a.k.a. Member Function

Method default form

*static* return_type class name :: function (arguments) *const*;

# this pointer

현재 설계 중인 제품의 전화 번호는 미래에 결정된다. 그런데 제작자는 아직 결정되지 않은 전화 번호를 이용해야 하는 코드를 작성해야 할 수 있다.
**현재 시점에서 미래의 전화 번호에 접근하는 방법이 this pointer 입니다.**

```gradle
int main()
{
    USERDATA user = { , , print};
    user.Print(&user);

    // cpp
    user.Print();

    return 0;
}
```

클래스 객체(인스턴스) user가 선언되는 시점은 클래스를 정의하고 난 나중 일이다. Print()에서 user 구조체 주소를 넘겨 받아 데이터를 반환하려면 user의 주소가 필요한데 아직 주소를 모른다. cpp의 매개변수 칸에도 눈에 보이지 않을 뿐 &user를 전달하고 있다. 이렇게 **첫 번째 argument로 전달된 instance address는 this 포인터(지역 변수)에 저장된다.**

```angelscript
class abc
{ 
public:
    abc(int param) : idx(param) {};
    void print() { cout << this->abc::idx << endl;}
private:
    int idx;
};

int main(){
    abc a(1), b(2);
    a.print();
```

1 이 나온다.

명확히 말하면

1. a.print() 에 사실은 &a 매개변수를 넘겨준다.
2. public: void print(abc * pdata) { abc * this = pdata; )를 위에 가지고 있어
3. this = & a

this -> 를 이렇게 이용하는 것이다.
| 메서드 함수 내부에서 실제 클래스 인스턴스의 주소를 가리키는 포인터이다.

# const

const는 안전 장치이자 배려이자 작성자 수준을 가늠하는 사용자 친화 코드 이자 미래이다. int Getdata() const {} 상수형 메서드로 정의하면 멤버 변수의 값을 write (변경) 수 없고, const 메서드 내에서 const가 아닌 함수를 호출할 수 없다.

추가 내용: 상수화 하는 방법은 Class *\this 를 const Class *\this 로 변경하는 것이다.

# static

cpp에서 전역 변수를 사용하는 것은 좋은 선택이 아니다. 이를 해결하기 위해 전역 변수와 동일한 동작을 하지만 클래스 멤버로 소속을 가지는 static을 이용한다.

- 사용자 코드에서 클래스 메서드를 사용하려면 무조건 인스턴스 선언하거나 new 연산으로 동적 인스턴스를 생성하고 멤버 접근 연산자로 호출해야 한다.

정적 멤버 함수는 인스턴스 선언 없이 직접 호출할 수 있다. 그러나 *\this 사용이 불가능하며 선언과 정의를 반드시. 반듯이. 분리해야 한다.

```java
class Class
{
 public:
     Class(int nparam) : mdata(nparam) { mCount++;}
    int Getdata() { return mdata;};
    void resetCount() {mCount = 0;};

    // static method definition & declaration
    static int GetCount() { return mCount; };

private:
    int mdata;

    // static method definition
    static int mCount;
};

// static method declaration
int Class::mCount = 0;

int main(int argc, char* argc[])
{
    Class a(10), b(0);
    cout << a.Getdata() << endl; // static 
    cout << Class::GetCount() << endl; // access without an instance
    b.resetCount();
    cout << b.GetCount() << endl;

    return 0;
}
```

결과값은
10
2
0

정적 멤버 함수는 인스턴스 및 멤버 접근 연산자(resetCount)를 이용해도 되고 클래스 이름::범위 지정 연산자(public)을 이용해 인스턴스 없이 직접 호출도 가능하다.