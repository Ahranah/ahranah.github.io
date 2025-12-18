---
layout: post
title: "[Node.js] 비밀번호 암호화하기 - bcypt 모듈"
date: 2025-05-30 10:35:39 +0900
categories: KB_ITs_Your_Life_6th
---

비밀번호가 req.body에 담겨서 이동할 때 암호화없이 그대로 이동하면 js 코드로 값을 홀랑 알아내버릴 수 있다.

해시함수를 이용해 암호화해보자. 

- 한 번 해시된 값은 원래 입력값으로 되돌릴 수 없다.

```javascript
const bcrypt = require("bcrypt");

const password = "qwer";

bycrypt.hash(password, 10, (err,hash) => {
	try {
    	// 해시화된 비밀번호를 디비에서 저장하거나 다른 처리
    } catch(err) {
    
    }
    
 });
```

비밀번호를 10번 해시한 후에 hash 함수를 실행할 것이다. 

 

비밀번호가 디비에 저장되면 로그인할 때마다의 비밀번호가 해시된 비번값과 동일한지 확인해야 로그인 처리를 해줄 수 있다. 

```javascript
const loginPassword = "로그인 비밀번호";
const hashedPassword = "DB에서 가져온 해시값";

bcrypt.compare(loginPassword, hashedPassword, (error, result) => {
	try {
    	if (result === true){
        
        }
    }
    
    ...
```

compare의 콜백함수는 값 2개를 비교한 후에 실행할 함수이므로 result 가 이미 값을 비교한 것이다.