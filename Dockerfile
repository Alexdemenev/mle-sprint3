FROM python:3.11-slim
# возьмем образ, который мы скачали ранее и в котором уже установлен python

LABEL author=${LABEL}
# добавим label, используя переменную среды

COPY . ./churn_app
# копируем файлы в Docker
# название директории внутри контейнера: churn_app

WORKDIR churn_app 
# изменяем рабочую директорию Docker 

RUN pip3 install -r ./requirements.txt
# инструкция для установки библиотек

EXPOSE 8081
# инструкции для открытия порта, указанного в переменной среды


VOLUME /models
# примонтируйте том с моделями


CMD uvicorn app.churn_app:app --reload --port 8081 --host 0.0.0.0
# измените команду запуска, учитывая порт из .env
