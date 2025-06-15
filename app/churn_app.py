"""Приложение Fast API для модели оттока."""


from fastapi import FastAPI, Body
from .fast_api_handler import FastApiHandler


# Создаем приложение Fast API
app = FastAPI()

# Создаем обработчик запросов для API
app.handler = FastApiHandler()


@app.post("/api/churn/") 
def get_prediction_for_item(
    user_id: str,
    model_params: dict = Body(
        {
            'gender': 1.0,
            'SeniorCitizen': 0.0,
            'Partner': 0.0,
            'Dependents': 0.0,
            'Type': 0.5501916796819537,
            'PaperlessBilling': 1.0,
            'PaymentMethod': 0.2192247621752094,
            'MonthlyCharges': 50.8,
            'TotalCharges': 288.05,
            'MultipleLines': 0.0,
            'InternetService': 0.3437455629703251,
            'OnlineSecurity': 0.0,
            'OnlineBackup': 0.0,
            'DeviceProtection': 0.0,
            'TechSupport': 1.0,
            'StreamingTV': 0.0,
            'StreamingMovies': 0.0,
            'days': 245.0,
            'services': 2.0
        }
    )
):
    """Функция для получения вероятности оттока пользователя.

    Args:
        user_id (str): Идентификатор пользователя.
        model_params (dict): Параметры пользователя, которые мы должны подать в модель.

    Returns:
        dict: Предсказание, является ли пользователь оттоком.
    """
    all_params = {
        "user_id": user_id,
        "model_params": model_params
    }
    return app.handler.handle(all_params)
