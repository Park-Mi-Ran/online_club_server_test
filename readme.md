동아리 박람회를 대체하기 위해 동아리 연합회를 진행할 예정입니다.

인원:

세팅 방법
git clone을 합니다. git clone https://github.com/SYULION9TH/2021-syu-club.git

github branch 설계 규칙
▶ 1. Branch 확인 하기

1. 현재 내가 위치한 Branch 확인
   $ git branch
2. 원격 저장소의 브랜치 확인
   $ git branch -r
3. 브랜치의 마지막 커밋 메세지 확인
   $ git branch -v

▶ 2. Branch 생성 및 이동
2.1 첫번째 방법

1. Branch 생성하기

- git branch 브랜치명
  ex)
  $git branch test

2. 생성한 Branch로 이동하기

- git checkout 브랜치명
  ex)
  $git checkout test

▶ 3. Branch 삭제

1. git branch -d 브랜치명
   ex)
   $git branch -d test

▶ 4. branch 병합 Git Merge
$git merge 브랜치명

\*\*master branch로 이동
$git checkout master
출처: https://goddaehee.tistory.com/274 [갓대희의 작은공간]

출처: https://goddaehee.tistory.com/274 [갓대희의 작은공간]

출처: https://goddaehee.tistory.com/274 [갓대희의 작은공간]
2021-syu-club/onlineclub폴더가 있는 위치에서 가상환경(source myvenv/bin/activate )을 실행해 줍니다.

가상환경 실행 후 requirements.txt가 있는 위치에서 pip install -r requirements.txt명령어를 입력합니다.

python manage.py runserver 이후 127.0.0.1:8000/admin으로 들어가서 제대로 되는지 확인합니다.

id : dev
password : 1234
※python manage.py migrate는 하지마세요※

개발 시작합시다.

동아리 앱 폴더:

동아리 - 황한슬, 박미란
models = ClubTypes, Clubs

게시물 - 최정은
models = Posts

account -함승우
models - AuthUser

URL 설계
자원의 컬렉션 이름으로는 복수형을 쓴다. ex) /Post/1 -> /posts/1

http의 Method가 들어가서는 안된다.

동사표현을 쓰면 안된다. ex) /posts/show/1 -> GET /posts/1

경로 중 변하는 값은 유일한 값으로 바꾼다. ex) id가 12인 게시물을 지우는 행위 DELETE /posts/12

'/'는 계층관계를 나타내는데 사용한다.

URI 마지막 문자로 슬래시(/ )를 포함하지 않는다.

대문자는 쓰지 않고 소문자만 쓴다.

하이픈(- )은 URI 가독성을 높이는데 사용 불가피하게 긴 URI경로를 사용하게 된다면 하이픈을 사용해 가독성을 높인다.

밑줄(\_ )은 URI에 사용하지 않는다. 밑줄은 보기 어렵거나 밑줄 때문에 문자가 가려지기도 하므로 가독성을 위해 밑줄은 사용하지 않는다.

리소스 간에 연관 관계가 있는 경우 ex) 리소스명/{리소스ID}/관계가 있는 다른 리소스 명 --> posts/1/comments

QnA 예시)

설명 Method 경로
한 동아리의 QnA목록을 나타낸다. GET /clubs/:id/qna
한 동아리의 QnA상세를 나타낸다. GET /clubs/:id/qna/:id
한 동아리의 QnA를 수정한다. PUT /clubs/:id/qna/:id
한 동아리의 QnA를 삭제한다. DELETE /clubs/:id/qna/:id