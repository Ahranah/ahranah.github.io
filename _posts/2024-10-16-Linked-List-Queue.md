---
layout: post
title: "[Linked List] Queue"
date: 2024-10-16 23:37:41 +0900
categories: [Computer Science, Data Structure]
tags: [큐, 포인터, 동적할당]
---

# Queue

Fisrt In First Out

**<---- the other end (the front) ㅁ ㅁ ㅁ ㅁ ㅁ  one end(the rear)** **<----**

<-- dequeue from the front --------<---  enqueue from the rear 

## 방향 진짜 중요하다 무조건 왼쪽으로 ~~ !!

enqueue, dequeue 모두 rear와 front를 가리키는 인덱스를 +1 해 item을 넣고 빼게 된다.
이때, rear idx가 [max]인 경우 front idx 부터 할당된 어레이까지 공간이 남아도 더 이상 enqueue가 되지 않는다는 한계가 있다.

# Circular Queue

어레이를 동그랗게 이어서 여분 공간을 사용할 수 있도록 한다.

dequeue : 값을 내보내고 front = front  + 1 한다. 

enqueue: rear = rear + 1 에 넣는다.

{% include figure.liquid loading="eager" path="assets/img/posts/2024-10-16-linked-list-queue/Screenshot 2024-10-16 at 10.37.11 PM.png" class="img-fluid rounded z-depth-1" %}

보다시피 Empty, Full 모두 front == rear + 1 로 표현되는 문제가 있다.

## Reserved space

Front가 가리키는 공간을 Reserved space로 두고, dequeue 시에는 front + 1 를 내보낸다.

```ini
front = (front + 1) % max_queue; 
result = queue[front]
```

- Full Queue(rear + 1) % maxQueue == front
- Empty Queuefront == rear

## Linked List

포인터는 변수다. 포인터가 가리키는 대상에 따라 포인터가 특정 **타입** 을 가지게 된다.

우리는 NodeType의 주소를 가져야 하기 때문에 포인터는 모두 NodeType* ptr; 를 가진다. (int* 아닌 이유가 궁금했다.)

```cpp
template<class ItemType>
struct NodeType {
	ItemType value;
    NodeType * next;
}

template<class ItemType>
class QueueType 
{
private:
	NodeType<ItemType> * pFront;
    NdoeType<ItemType> * pRear;
    
public:
	QueueType();
    ~QueueType();
    void enqueue(ItemType value);
    void dequeue(ItemType & value);
    void clear();
    int size() const;
    bool isFull() const;
    bool isEmpty() const;
}
```

**-> 해석하는 방법**

이런식으로 접근하면 헷갈린다. 잊지 말아야 할 건 **new_node가 포인터**라는 거다. 포인터는 가리키는 객체 멤버에 접근할 때 무조건 -> 을 이용한다. new_node.value = new_value; 를 할 수 없는 이유 또한 new_node가 포인터이기 때문이다. 객체 중에서 멤버를 고를 때 .(점 연산자)를 이용하는데 포인터는 객체 상자를 가리키고 있기에 . 을 쓰면 컴파일 오류가 난다.  

```cpp
void QueueType::enqueue(ItemType new_value){
	NodeType* new_node;
    new_node = new NodeType;
    
    new_node -> value = new_value; 
    new_node -> next = nullptr;
    /*
    pRear -> next = new_node; //지금 가리키는 (직전 마지막)의 next를 최신으로 이어놓고
    pRear = new_node; // 자신은 최신을 가리킨다.
    */
    
    // edge condition : Empty()
    // when the queue is empty, pFront should be updated to point to new_node !
 	if (! isEmpty()){ // 비어있었다면 직전 노드가 없어서 next가 없다. 
    	pRear->next = new_node;
    } else { pFront = new_node;};
    pRear = new_node;
}
```

{% include figure.liquid loading="eager" path="assets/img/posts/2024-10-16-linked-list-queue/Screenshot 2024-10-16 at 10.46.34 PM.png" class="img-fluid rounded z-depth-1" %}

뇌 빼고 있다보니 왜 새 객체 new_node 를 포인터로 가지는 지 백지 코딩할 때 이유를 못 찾았다.

** Dynamic Allocation: **

힙은 프로그램 실행(런타임) 중에 메모리를 할당받기 때문에 할당된 메모리의 주소를 저장할 필요가 있다. 그때 주소를 저장할 수 있는 변수가 포인터고 !! 그래서 new 는 항상 포인터로 생성하고 delete 하는 것을 잊지 말자!! 

{% include figure.liquid loading="eager" path="assets/img/posts/2024-10-16-linked-list-queue/Screenshot 2024-10-16 at 10.49.06 PM.png" class="img-fluid rounded z-depth-1" %}

```cpp
void QueueType::dequeue(ItemType & ret_value){
	NodeType* tempPtr;
    tempPtr = pFront;
    
    ret_value = pFront -> value;
    pFront = pFront -> next;
    delete tempPtr;
    
    //edege : Empty 
    if (isEmpty()){ pRear = nullptr; }
}
```

**dequeue하면 front는 -1 일까 +1 일까?**

이게 왜 자꾸 헷갈리는 지 모르겠는데.. 뭔가 내보내니까 -1 (어레이적 관점) 해야 할 것 같아서 pFront = pFront -> next 가 아니라 이전 노드의 next를 nullptr로 업데이트해줘야 할 것만 같다. (심지어 가능한 구현인지도 모르겟슴)

아무튼 큐는 앞으로 앞 뒤가 없는 친구니까 !! ㅁㅁㅁㅁㅁ <- 요 놈을 내보낸다고 생각하지 말고  

이 놈을 잡아 뺀다고 생각해야 한다. -> ㅁㅁㅁㅁㅁ / 넣을 때는 ㅁㅁㅁㅁㅁ<- 얘를 넣은 거다

큐는 들어가고 나오는 공간이 다르니까 구분하려다보니 더 헷갈려졌다. 방향만 잘 잡으면 안 헷갈리겠다. **<- 왼쪽으로 넣고 빼세요 **