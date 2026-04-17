import requests
import datetime
from api_methods import get_everything
from dotenv import load_dotenv
import os



def create_daily_annotation(topic):

    load_dotenv()
    
    news_api_key = os.getenv("NEWS_API_KEY")
    mistral_api_key = os.getenv("MISTRAL_API_KEY")

    today = datetime.date.today().strftime("%Y-%m-%d")
    print(f"Системная дата: {today}")

    response = get_everything(news_api_key, q=topic, sort_by="publishedAt", page_size=20)
    articles = response.get("articles", [])

    print(f"Найдено статей: {len(articles)}")
    if articles:
        print(f"Дата первой статьи: {articles[0].get('publishedAt')}")

    articles_text = "\n\n".join([f"Заголовок: {a['title']}\nОписание: {a['description']}" for a in articles])

    prompt = f"Ты аналитик. На основе этих новостей за последний день по теме '{topic}' напиши аннотацию на русском языке (250-300 слов) с оценкой основных событий:\n\n{articles_text}"

    headers = {"Authorization": f"Bearer {mistral_api_key}", "Content-Type": "application/json"}
    payload = {"model": "mistral-small-latest", "messages": [{"role": "user", "content": prompt}]}

    print("Отправка запроса в Mistral...")
    mistral_response = requests.post("https://api.mistral.ai/v1/chat/completions", json=payload, headers=headers)

    if mistral_response.status_code != 200:
        print(f"Ошибка Mistral API: {mistral_response.status_code}")
        print(mistral_response.text)
        return None

    summary = mistral_response.json()["choices"][0]["message"]["content"]

    with open("text", "w", encoding="utf-8") as f:
        f.write(summary)
    print("Файл 'text' создан в текущей папке.")

    return summary

if __name__ == "__main__":
    ann = create_daily_annotation("NBA")
    if ann:
        print("Аннотация (первые 200 символов):", ann[:200] + "...")
