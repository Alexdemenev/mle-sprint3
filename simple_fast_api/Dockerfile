FROM python:3.11-slim

LABEL author=${AUTHOR}
# ${AUTHOR} - это переменная среды
COPY . ./simple_fast_api
WORKDIR simple_fast_api 
RUN pip3 install -r requirements.txt
# директория simple_fast_api скопирована в Docker
# укажем инструкцию по запуску микросервиса

VOLUME /speeches
# указываем, что директория speeches внутри контейнера будет являться томом
# на этапе сборки docker создаст необходимые файлы на самой виртуальной машине
# в директории /var/lib/docker/volumes/

EXPOSE ${APP_PORT}
# указываем переменную среды
# эта инструкция указывает образу, 
# что порт 1702 должен быть открыт 'снаружи'

CMD uvicorn app.main:app --host  0.0.0.0 --port ${APP_PORT}
# изменили команду на простую строк
