import requests

webhook_url = 'https://webhook.site/e3680cd5-04d6-4077-870a-10ddc8c7b67e'

def enviar_notificacao(novo_pet):
    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.post(webhook_url, json=novo_pet, headers=headers)
        if response.status_code == 200:
            print(f"Notificação enviada com sucesso: Novo pet disponível para adoção {novo_pet['nome']}!")
    except Exception as e:
        print("Erro ao enviar notificação: {e}")

if __name__ == "__main__":
    novo_pet = {'nome': 'Bobby', 'tipo': 'Cachorro'}
    enviar_notificacao(novo_pet)