---
layout: post
title: "git으로 협업하기 위한 git flow 이해하기"
date: 2025-05-15 12:11:01 +0900
categories: KB_ITs_Your_Life_6th
---

{% include figure.liquid loading="eager" path="assets/img/posts/2025-05-15-git으로-협업하기-위한-git-flow-이해하기/img.png" class="img-fluid rounded z-depth-1" %}

나는 지금까지 개인 프로젝트를 깃에 올리지 않았다. 수정할 때마다 새로 커밋하는 것도, 잘못된 명령어 하나로 로컬이 원격과 연동되어버리면 다시 복구하느라 시간 쏟는 과정이 아까웠다. 하지만 이제는 협업을 위해 배워야 한다.

### 개인 브랜치 사용: 로컬 코드를 원격 저장소에 올리는 코드

1. git status

2. git add .

3. git commit -m "설명 추가: 현재 변경 내용 요약"

4. git checkout -b <브랜치명>

5. git push origin <현재 브랜치명>

- git branch
- git push --set-upstream origin <브랜치명> // git push 만으로 자동으로 원격과 연결

 

---