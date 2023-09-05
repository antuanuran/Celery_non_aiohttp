# 1. Создаём виртуальное окружение:
   - python3 -m venv venv
   - source venv/bin/activate

# 2. Устанавливаем библиотеки:
   - pip install -r requirements.txt

# 3. Устанавливаем Redis:
   - docker-compose up -d
   
# 4. Запускаем worker:
   - celery -A tasks worker --loglevel=INFO
   
# 5. Запускаем приложение (5 - это аргумент):
   - python3 main.py 5
   
   
