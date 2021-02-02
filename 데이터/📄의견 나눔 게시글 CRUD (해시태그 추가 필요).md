## 📄의견 나눔 게시글 CRUD



* DB

| 이름         | 타입     |
| ------------ | -------- |
| user         |          |
| title        | char     |
| content      | text     |
| created_at   | DateTime |
| updated_at   | DateTime |
| comment_type | boolean  |
| category     | char     |
| read_count   | int      |

```text
✅ comment_type 
- 1 : 토의
- 0 : 토론
```



* 전체 리스트 조회 (R)

  * GET http://127.0.0.1:8000/articles/article_list/

  * 데이터 : 글 제목, 글쓴이, 작성일, 조회수 

  * ex)

    ``` text
    [
        {
            "id": 2,
            "title": "a",
            "user": 2,
            "created_at": "2021-01- 27T15:06:40.436368+09:00",
            "read_count": 1
        }
    ]
    ```



* 글 작성 (C)
  * POST  http://127.0.0.1:8000/articles/article_create/
  * 보내줄 데이터 : title / content / comment_type / category / user 



✅ 로그인이 안되어있을 때 글작성 버튼 누르면 alert창 뜨게 해주세용!



------------------------

* 디테일 페이지 조회 (R)

  * GET  http://127.0.0.1:8000/articles/< int:article_pk >/ 

  * 받아오는 데이터 :  title / content / created_at / updated_at / comment_type / category / user

  * ex

    ```text
    {
        "id": 2,
        "title": "a",
        "content": "a",
        "created_at": "2021-01-27T15:06:40.436368+09:00",
        "updated_at": "2021-01-27T15:23:11.559545+09:00",
        "comment_type": true,
        "category": "a",
        "read_count": 2,
        "user": 2
    }
    ```

    



* 디테일 페이지 수정 (U)
  * PUT http://127.0.0.1:8000/articles/< int:article_pk >/ 
  * 보내줄 데이터 : title / content / comment_type / category / user



* 디테일 페이지 삭제(D)

  * DELETE http://127.0.0.1:8000/articles/< int:article_pk >/ 

  * 삭제되면 삭제된 게시글 id 값 response

    ```text
    {
        "id": 2
    }
    ```



✅ 디테일 페이지 수정과 삭제 버튼은 해당 글 작성자에게만 보여지게 해주세욥!! (back에서 안 막아뒀음!)