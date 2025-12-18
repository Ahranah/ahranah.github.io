---
layout: post
title: "[SQL] SELECT, INSERT, DELETE, UPDATE"
date: 2024-10-23 01:10:02 +0900
categories: [Computer Science, DataBase]
tags: [join, sql, insert, update, delete, select, subquery, database]
---

# SQL과 관계대수가 뭐가 다른가?

SQL은 IBM 연구소에서 관계 DBMS(System R) 연구할 때 관계대수를 기반으로 집단 함수, 그룹화, 갱신 연산을 추가해서 개발한 언어

사용자가 관계 DBMS에 원하는 데이터(what) 명령 -> 관계 DBMS에서 효율적으로 처리(how)하여 반환

# SQL은 비절차적, 관계대수는 절차적

SQL은 원하는 것만 질의에 명시하고, 관계대수식은 소괄호 ()를 이용해 관계 연산자의 수행 순서를 명시한다.

SQL은 3개 종류의 연산으로 명시할 수 있다.

- DDL: SCHEMA(구조나 제약조건 등)을 생성하거나 변경, 제거한다.CREATE(DOMAIN, TABLE... ),ALTERTABLE,DROPDOMAIN, TABLE, VIEW ...
- DML: 튜플의 검색(SELECT),INSERT_ INTO _ VALUES ( ),DELETEFROM, 수정(UPDATE_ SET)
- DCL: 트랜잭션 명시, 권한 허가 또는 취소

{% include figure.liquid loading="eager" path="assets/img/posts/2024-10-23-sql-select-insert-delete-updat/Screenshot 2024-10-22 at 11.18.45 PM.png" class="img-fluid rounded z-depth-1" %}

*스키마란 SQL2에서 사용되는 테이블, 도메인, 제약조건, 뷰, 권한을 그룹화한 것을 의미한다. 
- CREATE SCHEMA kim schema AUTHORIZATION kim;

{% include figure.liquid loading="eager" path="assets/img/posts/2024-10-23-sql-select-insert-delete-updat/img.png" class="img-fluid rounded z-depth-1" %}

{% include figure.liquid loading="eager" path="assets/img/posts/2024-10-23-sql-select-insert-delete-updat/img_1.png" class="img-fluid rounded z-depth-1" %}

## 데이터 정의어와 무결성 제약조건

**1. ENROLLED(STUDENT_ID, COURSE_ID, GRADE)**

CREATE TABLE 를 작성해라
- STUDENT_ID 는 STUDENT 테이블의 기본 키를 참조하는 외래키다. 
- COURSE_ID 는 COURSE 테이블의 기본 키를 참조하는 외래키라고 가정한다.  
- GRADE CHAR(1) CHECK ('A', 'B', 'C', 'D', 'F')

**2. ON UPDATE CASCADE**

UPDATE DEPARTMENT SET DEPTNO = 6 WHERE DEPTNO = 3;
ON UPDATE CASCADE 되어 있다면 어떤 파급이 있는가? 

**3. STUDENT TABLE 에 STUDENT_PK라는 이름의 제약 조건을 추가해라. 제약 조건은 STNO 컬럼을 기본 키로 지정하는 것이다.  **

**4. STUDENT TABLE 에 STUDENT_PK라는 이름의 제약 조건을 제거해라. **

 

## SELECT문

관계 대수의 selection, projection, join, cartesian product 를 결합한 정보 검색 명령어다.

**1. HAVING, WHERE, GROUP BY, ORDER BY 순서를 써보시오.**

**2. 모든 컬럼 검색:**
전체 부서의 모든 컬럼을 검색하라. DEPARTMENT
사원의 상이한 직급(TITLE)을 EMPLOYEE에서 검색하라.

**3. 특정 튜플 검색 - WHERE**

colums LIKE '%Hello%';

colums LIKE '_Hello';

**4. 다수의 검색 조건 WHERE AND OR**
- NOT, AND, OR, 비교 연산자의 우선 순위를 비교하라.
- AGE가 18살이 아닌 회원의 이름을 검색하라

**5. 범위 연산자 (p.44)**
- BETWEEN AND 를 AND로만 표현해라
- 18살 이거나 19살인 회원의 모든 정보를 검색하라.

**6. SELECT절에서 산술 연산자 사용**
- 직급(TITLE)이 과장이 사원들에 대해 이름(EMPNAME), 현재 급여(SALARY), 10% 인상 급여 값을 검색해라 (TABLE EMPLOYEE)

**7. unknown에 대한 비교 연산의 값은?**

 
TRUE
FALSE
UNKNOWN
NOT

TRUE
 
 
 
 

FALSE
 
 
 
 

UNKNOWN
 
 
 
 

 

**8. 집단 함수**

집단 함수는 여러 튜플에 적용하는 명령어로 SELECT, HAVING에만 적용 가능

{% include figure.liquid loading="eager" path="assets/img/posts/2024-10-23-sql-select-insert-delete-updat/Screenshot 2024-10-23 at 12.09.07 AM.png" class="img-fluid rounded z-depth-1" %}

 

**9. 그룹화**

GROUP BY로 사용된 컬럼에 대해 동일한 값을 갖는 튜플이 하나로 묶임, 사용된 컬럼은 그룹화 컬럼(grouping column)이라 한다. 

SELECT 절에는 하나의 값을 갖는 컬럼, 집단 함수, 그룹화 컬럼만 나타날 수 있다.

**이 질의의 문제점은?**

SELECT EMPNO, AVG(SALARY) FROM EMPLOYEE; 

**해결 방법은?**

 

**10. HAVING과 GROUP BY의 종속성**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-10-23-sql-select-insert-delete-updat/img_2.png" class="img-fluid rounded z-depth-1" %}

{% include figure.liquid loading="eager" path="assets/img/posts/2024-10-23-sql-select-insert-delete-updat/img_3.png" class="img-fluid rounded z-depth-1" %}

{% include figure.liquid loading="eager" path="assets/img/posts/2024-10-23-sql-select-insert-delete-updat/img_4.png" class="img-fluid rounded z-depth-1" %}

 

**11. ORDER BY**

**12. 집합 연산**

집합 연산하려면 두 테이블이 **합집합 호환성**을 가져야 함
- UNION, EXCEPT, INTERSECTION, UNION ALL, EXCEPT ALL, INTERSECT ALL, MINUS ...

**중복 튜플을 제거하는 결과를 반환하는 합집합 명령어는?**

 

**13. 조인**

두 개 이상의 테이블로부터 연관된 튜플을 결합하는데 조인 조건은 **WHERE에서 비교 연산자**로 연결 (주로 = )

{% include figure.liquid loading="eager" path="assets/img/posts/2024-10-23-sql-select-insert-delete-updat/Screenshot 2024-10-23 at 12.33.36 AM.png" class="img-fluid rounded z-depth-1" %}

일반적으로 FROM절에 **n개의 테이블**을 명시했을 때는 **n-1개의 조인 조건**이 필요하다. 잘못쓰면** 카티션 곱**이 생성.

{% include figure.liquid loading="eager" path="assets/img/posts/2024-10-23-sql-select-insert-delete-updat/Screenshot 2024-10-23 at 12.26.55 AM.png" class="img-fluid rounded z-depth-1" %}

**관계 대수에서 실행 순서**
( R x S ); 양쪽 테이블에서 (selection) 조인 조건에 만족하는 튜플을 찾고, (project) 이 튜플들로부터 SELECT절에 명시된 컬럼만 추출

컬럼 이름이 동일하다면 r.column, s.column - **테이블 이름**을 명시하거나 select column as cb from ~ 하고 cb**(튜플 변수)**를 사용해야 한다.

**14. 자체 조인(self join)**

한 테이블에 접근하는 건데 FROM 에서 두 테이블에 참조되는 것처럼 표현하기 위해 별칭을 두 개 지정

FROM EMPLOYEE E, EMPLOYEE M

{% include figure.liquid loading="eager" path="assets/img/posts/2024-10-23-sql-select-insert-delete-updat/img_5.png" class="img-fluid rounded z-depth-1" %}

{% include figure.liquid loading="eager" path="assets/img/posts/2024-10-23-sql-select-insert-delete-updat/img_6.png" class="img-fluid rounded z-depth-1" %}

 

 

**15. 중첩된 질의(nested query) = subquery**

외부 질의의 WHERE 에 다시 SELECT FROM WHERE 를 포함하는 것
- [DML] INSERT, DELETE, UPDATE에 사용될 수 있음

결과는 1. 단일값 2. 한 개의 컬럼에서 나온 여러 개의 값 3. 여러 컬럼으로 이루어진 테이블이 반환될 수 있음

**15.1. 단일값이 나오는 경우 **

WHERE TITLE = (SELECT ~ )

**15.2. 한 개의 컬럼으로 이루어진 여러 개의 값이 반환되는 경우**

여기서 여러 개의 값은 스칼라 값들의 다중집합? , 다수의 튜플일 수 있다. 이를 위해서 외부 WHERE에서 **IN, ANY(SOME), ALL, EXIST** 등의 연산자를 사용해야 한다.

- 3426IN{2107, 3921}

{% include figure.liquid loading="eager" path="assets/img/posts/2024-10-23-sql-select-insert-delete-updat/Screenshot 2024-10-23 at 12.52.19 AM.png" class="img-fluid rounded z-depth-1" %}

- EXIST다중집합이 비어있지 않은지
- ANY, SOME한 컬럼이 다중집합에 속하는 하나 이상의 값들과 어떤 관계를 가지는지 테스트499 <ANY{ 300, 200, 500 } -> TRUE300 <ANY{ 299, 199, 99} -> FALSE
- ALL컬럼과 집합의 관계를 테스트499 <ANY{ 300, 200, 500 } -> FALSE300 <ANY{ 499, 399, 599} -> TRUE

 

가능하면 subquery는 사용하지 않는 것이 좋다. 
어떤 질의는 subquery로만 표현할 수 있긴 하지만. . .

```sql
# JOIN
SELECT EMPNAME FROM EMPLOYEE E, DEPARTMENT D
WHERE E.DNO = D.DEPTNO
	AND (D.DEPTNAME = 'HR' OR D.DEPTNAME = 'BUSINESS');
    
# SUBQUERY
SELECT EMPNAME FROM EMPLOYEE 
WHERE DNO IN 
	(SELECT DEPTNO FROM DEPARTMENT WHERE DEPNAME = 'HR' OR D.DEPTNAME = 'BUSINESS');
```

 

**15.3. 여러 컬럼으로 이루어진 테이블이 반환되는 경우**

**= 16. 상관 중첩된 질의(Correlated nested query)**

subquery where 절에 있는 조건이 외부 쿼리에서 선언된 테이블을 참조하는 경우이다. 테이블이 반환되면 EXIST로 빈 테이블인지 아닌지를 확인한다.

{% include figure.liquid loading="eager" path="assets/img/posts/2024-10-23-sql-select-insert-delete-updat/Screenshot 2024-10-23 at 1.00.13 AM.png" class="img-fluid rounded z-depth-1" %}

뭐가 다른거냐면! 결과 반환 횟수(수행 횟수)가 다른거다. 

외부 질의를 만족하는 튜플이 구해진 뒤에 중첩된 질의가 수행되므로 correlated nested query는 외부 질의를 만족하는 튜플 수만큼 여러 번 수행될 수 있다. 위 코드에서는 외부 쿼리에서 사원 이름 컬럼을 선택하고,  영업이나 개발에 속하는 사원 컬럼을 외부 쿼리에서 만족할 때까지 반환한다. 

 

INSERT, DELETE, UPDATE 위에서 한 번 언급됐따. subquery 할 때.. 

수정하는 친구들이라서 기본키일 때 참조 무결성 제약 조건 위배하지 않도록 조심해야 한다. 

## INSERT INTO [TABLE] VALUES ( , , );

## DELETE FROM [TABLE] [WHERE ~];

## UPDATE [TABLE] SET [COLUMN = ~] [WHERE ];