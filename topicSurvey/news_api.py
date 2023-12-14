import requests;


def fetch_news(topic_name):
    try:
        # Replace 'YOUR_API_KEY' with your actual News API key
        api_key = '09e68d835d864ff49edeae893a749fd1'
        base_url = 'https://newsapi.org/v2/everything'
        params = {
            'q': topic_name,
            'apiKey': api_key,
            'pageSize': 10,
        }
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

        data = response.json()

        news_list = []
        for article in data.get('articles', []):
            source_name = article['source'].get('name', '')
            news_list.append({
                'title': article.get('title', ''),
                'description': article.get('description', ''),
                'published_at': article.get('publishedAt', ''),
                'author': article.get('author', ''),
                'url': article.get('url', ''),
                'source_name': source_name,
            })

        return news_list

    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Error fetching news: {e}")
        return []

    except Exception as e:
        # Handle other exceptions
        print(f"Unexpected error: {e}")
        return []