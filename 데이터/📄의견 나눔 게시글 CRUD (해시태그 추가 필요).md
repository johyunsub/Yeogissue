## πμκ²¬ λλ κ²μκΈ CRUD



* DB

| μ΄λ¦         | νμ     |
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
β comment_type 
- 1 : ν μ
- 0 : ν λ‘ 
```



* μ μ²΄ λ¦¬μ€νΈ μ‘°ν (R)

  * GET http://127.0.0.1:8000/articles/article_list/

  * λ°μ΄ν° : κΈ μ λͺ©, κΈμ΄μ΄, μμ±μΌ, μ‘°νμ 

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



* κΈ μμ± (C)
  * POST  http://127.0.0.1:8000/articles/article_create/
  * λ³΄λ΄μ€ λ°μ΄ν° : title / content / comment_type / category / user 



β λ‘κ·ΈμΈμ΄ μλμ΄μμ λ κΈμμ± λ²νΌ λλ₯΄λ©΄ alertμ°½ λ¨κ² ν΄μ£ΌμΈμ©!



------------------------

* λνμΌ νμ΄μ§ μ‘°ν (R)

  * GET  http://127.0.0.1:8000/articles/< int:article_pk >/ 

  * λ°μμ€λ λ°μ΄ν° :  title / content / created_at / updated_at / comment_type / category / user

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

    



* λνμΌ νμ΄μ§ μμ  (U)
  * PUT http://127.0.0.1:8000/articles/< int:article_pk >/ 
  * λ³΄λ΄μ€ λ°μ΄ν° : title / content / comment_type / category / user



* λνμΌ νμ΄μ§ μ­μ (D)

  * DELETE http://127.0.0.1:8000/articles/< int:article_pk >/ 

  * μ­μ λλ©΄ μ­μ λ κ²μκΈ id κ° response

    ```text
    {
        "id": 2
    }
    ```



β λνμΌ νμ΄μ§ μμ κ³Ό μ­μ  λ²νΌμ ν΄λΉ κΈ μμ±μμκ²λ§ λ³΄μ¬μ§κ² ν΄μ£ΌμΈμ₯!! (backμμ μ λ§μλμ!)