import requests

webhook_url = 'https://webhook.site/e3680cd5-04d6-4077-870a-10ddc8c7b67e'

def enviar_notificacao(novo_pet):
    print(f"Notificação: Novo pet disponível para adoção: {novo_pet['nome']}!")
    
    headers = {'Content-Type': 'application/json'}
    response = requests.post(webhook_url, json=novo_pet, headers=headers)
    return response.status_code == 200

if __name__ == "__main__":
    novo_pet = {'nome': 'Bobby', 'tipo': 'Cachorro'}
    enviar_notificacao(novo_pet)