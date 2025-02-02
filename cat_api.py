import requests

cat_api_url = 'https://api.thecatapi.com/v1/images/search'

def get_random_cat():
    response = requests.get(cat_api_url)
    if response.status_code == 200:
        return response.json()[0]['url']
    return None

if __name__ == "__main__":
    print("Imagem randômica:", get_random_cat())