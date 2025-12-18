---
layout: post
title: "[Servlet] 웹 애플리케이션 기본 구조와 Servlet 라이프사이클"
date: 2025-07-07 22:37:16 +0900
categories: KB_ITs_Your_Life_6th
---

## 웹 애플리케이션 개발을 위한 웹 기본 동작 원리를 익혀본다.

 

## 1. 네트워크: HTTP

웹은 HTTP라는 프로토콜을 기반으로 브라우저와 서버가 메시지를 주고 받으면서 동작한다. 

{% include figure.liquid loading="eager" path="assets/img/posts/2025-07-07-servlet-웹-애플리케이션-기본-구조와-servle/img.png" class="img-fluid rounded z-depth-1" %}

브라우저가 HTML을 통해 서버에 요청(request)을 전달하면 서버는 request와 함께 전달된 사용자 정보를 추출해서 요청된 기능을 처리한다. 이때 서버에서 사용자 request를 처리하는 대표적인 자바 기술이 Servlet이다.

- 서블릿은 Spring MVC에서도 이어지는 개념이니 용어가 익숙해져야 한다.

웹 앱 개발은 TCP 기반의 HTTP를 이해하는 것으로 시작한다. 네트워크 사용할 때 사용하는 통신 규약이므로 웹 프로그래밍 개발을 위해 동작 원리를 익혀야 한다. 

{% include figure.liquid loading="eager" path="assets/img/posts/2025-07-07-servlet-웹-애플리케이션-기본-구조와-servle/img_1.png" class="img-fluid rounded z-depth-1" %}

히히 끼워팔기

[TCP/IP 와 UDP*이것이 자바다(3판)을 보고 작성한 글입니다.IP: Internet ProtocolIP 주소는 네트워크 어댑터(LAN 카드)마다 할당된다.DNS(Domain Name System)Web browser 웹 명령어 ipconfig / ifconfig웹브라우저가 DNS를 거쳐 웹서ahranah.tistory.com](https://ahranah.tistory.com/88)
 

[HTTP Protocol 기초*Node.js 프로그래밍 입문(고경희)를 읽고 작성한 글입니다.  클라이언트는 서버로 자료를 요청하고, 서버는 클라이언트로 자료를 전송하는 방식으로 웹이 동작한다. HTTP requestHTTP response 근데ahranah.tistory.com](https://ahranah.tistory.com/58)
 

## 2. 서버의 구성: 톰캣과 서블릿

앞서, 서버가 클라이언트의 request를 처리하는 대표적인 기술이 서블릿이라 했다.

서블릿은 JSP와 함께 동적 콘텐츠를 작성할 수 있는 자바 기술이다. 서버를 구성하는 부품은 자바로 구현 가능한 것으로 이뤄지는데, 자바로 구현한 웹 애플리케이션은 기본적으로 서버 사이의 이식성이 보장되기 때문이다. 

톰캣 서버를 기반으로 개발된 웹 앱은 제우스나 웹로직 같은 다른 서버에서 실행해도 동일하게 실행된다. 이렇게 서버 사이의 이식성을 보장하기 위해서 기본적으로 웹앱이 모든 서버가 인식하는 정형화된 디렉터리 구조를 유지해야만 한다. 

- 서버 사이 이식성을 보장하기 위해 자바로 구현한 Servlet, Tomcat 서버를 이용한다.
- 서버 사이 이식성을 보장하기 위해 정형화된 디렉토리 구조를 유지한다.

 

### 2-1. 서버 동작의 개요

{% include figure.liquid loading="eager" path="assets/img/posts/2025-07-07-servlet-웹-애플리케이션-기본-구조와-servle/img_2.png" class="img-fluid rounded z-depth-1" %}

웹 애플리케이션 컨테이너(예: Tomcat, Jetty)는 서블릿이 안정적으로 실행되기 위한 공통 환경을 제공한다. 구체적으로는 HTTP 요청·응답을 관리하고, 서블릿의 생성·초기화·소멸(lifecycle)을 제어하며, 보안·트랜잭션 같은 엔터프라이즈 기능을 대신 처리한다. 개발자는 이 복잡한 기반 구조를 직접 구현할 필요 없이 비즈니스 로직에만 집중할 수 있다.

- 쇼핑몰 장바구니 할인에서 아래와 같은 내용이 비즈니스 로직이다.사용자가 장바구니에 담은 상품들의 가격과 수량을 합산해총 주문금액을 계산할인 적용 기준 검사 - 계산된 금액이 “10만원 이상”이면10% 할인을 적용

서블릿을 여러 개로 나누는 이유는 관심사의 분리(Separation of Concerns)와 재사용성 때문이다. 예를 들어 “로그인 처리”, “게시판 목록 조회”, “파일 업로드” 같은 기능을 각각의 서블릿 클래스로 구현하면 유지보수가 쉽고, URL 맵핑을 통해 기능별로 요청을 간편히 분배할 수 있다. 각 서블릿은 자신에게 맡겨진 책임만 수행하기 때문에 테스트·디버깅도 명확해진다.

컨테이너는 실행 환경을 표준화하고, 서블릿 분리는 모듈화를, 멀티스레드는 성능 최적화

1. 클라이언트 요청웹 브라우저가 특정 URL로 HTTP 요청을 보냄요청은 먼저 웹 서버(예: Apache httpd, Nginx)로 들어감
2. 서블릿 컨테이너 전달웹 서버는 요청을 서블릿 컨테이너(예: Tomcat)의 접속 포트로 포워딩컨테이너는 요청 URL에 매핑된Servlet클래스를 찾음
3. 서블릿(Servlet) 실행doGet()/doPost()메소드에서 비즈니스 로직 수행필요 시 DB와 연동하여 데이터 조회·가공조회한 결과를request.setAttribute("data", 값)등에 담아 JSP로 전달
4. JSP 호출 및 화면 결합서블릿이RequestDispatcher.forward("/view.jsp")로 JSP 실행 지시JSP는 HTML 템플릿 코드에 서블릿에서 설정한request데이터를 삽입하여 동적 페이지(HTML) 생성
5. 응답 반환생성된 HTML은 다시 서블릿 컨테이너 → 웹 서버 → 클라이언트 순으로 전송브라우저가 수신한 HTML을 렌더링

{% include figure.liquid loading="eager" path="assets/img/posts/2025-07-07-servlet-웹-애플리케이션-기본-구조와-servle/img_3.png" class="img-fluid rounded z-depth-1" %}

멀티스레드 지원하여 한 대의 서버 프로세스에서 수십, 수백 개의 요청을 동시에 처리할 수 있다. 쓰레드 풀에서 각각의 요청을 병렬 처리하여 다수 요청에서 응답 지연을 줄인다. 단, 스레드 간 공유 자우너에 대한 동기화 처리가 필요해 코드가 복잡해지고, 교착 상태나 race condition을 주의해야 한다. 

- 단일 스레드: 순차적 처리 → 구현이 단순하고 디버깅이 쉬우나, 동시 접속이 늘어나면 대기 시간 증가
- 멀티스레드: 병렬 처리 → 처리량이 높고 확장성이 좋으나, 동시성 제어와 컨텍스트 스위칭 비용을 고려해야 함

 

 

*채쌤의 Servlet&JSP 프로그래밍 핵심(채큐태)를 읽고 작성한 글입니다.