def enviar_notificacao(novo_pet):
    print(f"Notificação: Novo pet disponível para adoção: {novo_pet['nome']}!")
    
if __name__ == "__main__":
    novo_pet = {'nome': 'Bobby', 'tipo': 'Cachorro'}
    enviar_notificacao(novo_pet)