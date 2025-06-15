from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Histogram, Counter
import numpy as np

# создание экземпляра FastAPI приложения
app = FastAPI()

# инициализируем и запускаем экпортёр метрик
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

# main_app_predictions — объект метрики
main_app_predictions = Histogram(
    # имя метрики
    "main_app_predictions",
    # описание метрики
    "Histogram of predictions",
    # указываем корзины для гистограммы
    buckets=(1, 2, 4, 5, 10)
)

# main_app_predictions_counter — объект метрики
main_app_predictions_counter = Counter(
    "main_app_positive_predictions_counter",
    "Counter of predictions higher than 0",
)

# предсказания
@app.get("/predict")
def predict(x: int, y: int):
    #print(x)
    np.random.seed(int(abs(x)))
    prediction = x+y + np.random.normal(0,1)
    main_app_predictions.observe(prediction) # записываем значение в метрику
    if prediction > 0:
        main_app_predictions_counter.inc(1)
    return {'prediction': prediction}
