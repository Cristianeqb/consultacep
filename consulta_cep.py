import requests

def consulta_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        response = requests.get(url)
        data = response.json()
        if 'erro' in data:
            return None
        else:
            return data
    except Exception as e:
        return None
