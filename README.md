## Запуск проекта

1. **Установите зависимости**
     ```bash
   poetry install
    poetry shell
    ```
2. **Запустите миграции**
    ```bash
   alembic upgrade head
    ```
   

3. **Перейдите в директорию проекта и запустите проект**
    ```bash
    cd fastapi-application
    uvicorn main:main_app --reload


