---
layout: post
title: "[Vue] Component 심화"
date: 2025-03-27 16:36:51 +0900
categories: KB_ITs_Your_Life_6th
tags: [slot, vue, prop, emit, web]
---

## Style : CSS

## <style scoped>

일반적으로 기본 밑바탕이 되는 CSS 클래스는 import './main.css' css 파일로 src/main.js 에서 import 한다. 가장 먼저 import하기 때문에 앱 전체의 공통 스타일 적용에 편리하다. 그리고 각 컴포넌트(vue)에 적용할 css는 .vue에서 <style scoped> 범위 css로 설정해 충돌을 피해 적용하는 것이 바람직하다.

 

## <style module>

```javascript
  <div :class="$style.child">
  
  <style  module>
    .child {
      background-color: orange;
      border: solid 1px black;
      margin: 1.5em;
      padding: 1em;
    }
</style>
```

child: "_child_1n8qe_3" 절대 충돌하지 않을 클래스명을 가지게 된다. 

이 클래스는 내부 $style 옵션에 객체로 등록되어, 객체의 속성은 style module에 작성된 css가 되어 this.$style.child(클래스)에 문자열 css를 바인딩해야 하므로 v-bind를 이용한다 .

```cs
// css 클래스가 여러 개인 경우
<div :class="[$style.child, $style.italic]"> ... </div>
```

 

## Slot

컴포넌트 간 정보 전달의 큰 그림은 App.vue를 루트로 가지는 트리 구조다.

```javascript
import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')
```

main.js 파일에 등록된 최초 컴포넌트가 App.vue 이므로 루트 컴포넌트가 된다. 

```javascript
main.js
  └── App.vue (루트 컴포넌트)
        ├── Header.vue
        ├── Content.vue
        │     ├── PostList.vue
        │     │     ├── PostItem.vue
        │     └── Sidebar.vue
        └── Footer.vue
```

이런 식의 트리를 가진다고 할 때,

#### 각 컴포넌트(vue)끼리는 어떻게 값을 주고 받을까???

 

기본적인 컴포넌트 간 정보 전달 방법은 props와 emits이다. 

- 속성(부모 -> 자식(하위)) - props
- 이벤트(자식 -> 부모) - emit

props로 받은 값은 읽기 전용이라 값을 (굳이) 변경할 수 없다.  값을 변경도 못할 뿐더러 ul/li 같은 **구조 있는 HTML을 넘길 수 없다**는 단점도 있다. 부모 파일에서 정의한 구조를 원본으로 하위 컴포넌트에서 사용할 수 있어서 slot을 쓴다. 

 

**Slot** : 부모 컴포넌트 -> 자식 컴포넌트로 <[속성명]>...</[속성명]>  전달

사실 부모가 자식한테** content를 넘기는 게 아니라 **자식이 부모한테 **“여기 빈 칸 있어요~” **라고 말하고, **부모가 그 칸에 뭘 넣을지 정하는 구조**예요. 즉, 구조나 값을 포함한 **내용(content)은 부모 쪽에서 결정한다.**

부모 쪽에서 구조를 결정하는게 그렇게 큰 장점이 될까?? 이해가 잘 안됐다. **컴포넌트 재사용성**이 높아진다는 것인데 그걸 예제로 봐보자.

 

[Vue.js Slot: 슬롯은 왜 필요한가? :: 마이구미이 글은 Vue.js 에서 제공하는 요소에 대해 다룬다.크게 Slots, Named Slots, Scoped Slot 기능을 위한 예제를 통해 진행한다.관련 문서 - https://kr.vuejs.org/v2/guide/components.html#슬롯을-사용한-컨텐츠-배포참고mygumi.tistory.com](https://mygumi.tistory.com/262)
 

#### 

요약하면 : 

예를 들어, 볼륨바를 volume.vue에 추가해야 된다고 해보자. <slot>으로 넣게 되면 컴포넌트를 사용하는 곳(부모)에서만 추가적인 코드를 작성하면 나중에 volume.vue를 재사용할 수 있다. 

볼륨바를 volume.vue 자체에 추가하면 바가 항상 추가되어 재사용성이 떨어지게 된다. 

slot 을 사용할 때의 문제는 데이터 처리다. slot은 부모 컴포넌트에 정의되어 있기 때문에 부모 데이터 범위에는 접근을 할 수 있는데, 문제는 하위 컴포넌트 데이터에 액세스 권한이 없다.

여기서 **Scoped slot**을 쓰면 하위 컴포넌트의 값을 상위 컴포넌트에서 접근할 수 있게 해준다. 

 

#### 예제 :

```javascript
// props : CardProps.vue (자식)

<template>
  <div class="card">
    <h3>{{ title }}</h3>
    <p>{{ content }}</p> <!-- 구조가 고정돼 있음 -->
  </div>
</template>

<script>
export default {
  props: ['title', 'content']
}
</script>
```

 

```javascript
// 부모
<CardProps title="공지사항" content="- 항목1\n- 항목2\n- 항목3" />
```

**props는 문자열밖에 못 넘기니까 ul, li 같은 구조를 못 넘긴다! **→ HTML 태그 넘기려고 하면 escape 돼버리거나 그대로 출력됨

 

#### 예제 : Slot

```javascript
// CardSlot.vue (자식)

<template>
  <div class="card">
    <slot name="title"></slot>
    <slot></slot> <!-- 기본 슬롯 -->
  </div>
</template>
```

```javascript
// 부모
<CardSlot>
  <template v-slot:title>
    <h3>? 공지사항</h3>
  </template>

  <ul>
    <li>항목1</li>
    <li>항목2</li>
    <li>항목3</li>
  </ul>
</CardSlot>
```

<CardSlot> </CardSlot> 템플릿 내용을 자식의 <slot></slot> 부분에 렌더링한다.  v-slot:#title 처럼 이름을 지정해준 슬롯은 **Named slot** 이라고 하며 레이아웃 관리 목적으로 많이 사용된다. 

 

#### Props vs. Slot 요약

props
텍스트나 값만 넘길 수 있어서 ul/li 같은 **구조 있는 HTML을 넘길 수 없음**

slot
템플릿(=구조 있는 코드)을 직접 넘기니까 뭐든지 가능

 

 

추가로,

**Named Slot** 은 넘겨주는 정보를 명시하여 레이아웃 관리가 더 용이하다는 장점이 있다. 

```javascript
<BaseLayout>
  <template #header>
    <h1>다음은 페이지 제목일 수 있습니다.</h1>
  </template>

  <template #default>
    <p>주요 내용에 대한 단락입니다.</p>
    <p>그리고 또 하나.</p>
  </template>

  <template v-slot:footer>
    <p>다음은 연락처 정보입니다.</p>
  </template>
</BaseLayout>
```