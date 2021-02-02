#### 장고 fake data 생성 방법



* cd back 

  : back 폴더 내로 이동

* 설치

  ```
  pip install -r requirements.txt
  ```

* 데이터 생성 명령어

  python manage.py seed 앱이름 --number=15(생성할 데이터 수)

  * 앱이름 종류
    * accounts -> user 데이터 생성됨
    * articles -> 의견 나눔 게시판 데이터 생성됨

* 사용 예시

  * 의견나눔 게시판 데이터 15 개 생성
    * python manage.py seed articles --number=15



* 생성된 데이터 확인하기
  * db.sqlite3 파일에서 오른쪽 버튼 -> open database -> 아래쪽에 sqlite explorer 탭 생성됨 -> db 확인 가능



⛔ 주의 사항!!!

djago seed 사용하여 fake 데이터를 생성했다면,

깃 푸쉬 하기전에 db.sqlite3 파일을 삭제해야함!!!!!!

(항상 데이터를 추가해서 실험 해본 후에는 무조건 db.sqlite3 파일 삭제해주어야 충돌안남!!!!)