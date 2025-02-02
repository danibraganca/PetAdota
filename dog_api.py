import requests

dog_api_url = 'https://dog.ceo/api/breeds/image/random'

def get_random_dog():
    response = requests.get(dog_api_url)
    if response.status_code == 200:
        return response.json()['message']
    return None

if __name__ == '__main__':
    print("Imagem randômica ", get_random_dog())