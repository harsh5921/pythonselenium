import requests

def check_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "✅ Working"
        elif response.status_code == 404:
            return "❌ Not Found (404)"
        else:
            return f"❗ Unexpected Status Code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"❌ Error: {e}"
