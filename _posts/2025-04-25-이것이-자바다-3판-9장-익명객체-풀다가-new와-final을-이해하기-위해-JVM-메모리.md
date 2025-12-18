---
layout: post
title: "이것이 자바다(3판) 9장 익명객체 풀다가 new와 final을 이해하기 위해 JVM 메모리 동작 공부"
date: 2025-04-25 01:21:52 +0900
categories: [Computer Science, Object Oriented Programming]
tags: [new, final, Heap, stack, Stringpool, LocalVariable, anonymousobject, 지역변수final, stringnew]
---

## 7.다음 Chatting 클래스는 컴파일 에러가 발생합니다. 원인을 설명해보세요.

```arduino
public class Chatting {
	class Chat {
    	void start() {}
        void sendMessage(String message) {}
    }
    
    void startChat(String chatId) {
    	String nickName = null;
        nickName = chatId;
        
        Chat chat = new Chat() {
        	@Override
            public void start() {
            	while(true) {
                	String inputData = "안녕하세요.";
                    String message = "[" + nickName + "]" + inputData;
                    sendMessage(message);
                }
            }
        };
        
        chat.start();
    }
}

```

### 닉네임은 메소드의 지역변수이므로 final의 특징을 가진다. 따라서 값을 변경할 수 없어 String nickName = chatId;로 선언해야 한다.

 

?  나는 왜 계속 String null로 초기화하면 값 넣을 때 new로 해야하는 줄 알았을까 ㅠ

⇒ 요약: **String은 기본형처럼 자주 쓰여서, 특별하게 최적화된 참조형, **JVM에서 String Pool이라는 영역을 따로 만들어 관리.

참조형을 null로 초기화하고 new없이 값 대입하려고 하면 컴파일 에러나는 것이 맞다. String만 특이한 경우다. 

---