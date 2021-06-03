import os
import requests


def get_secret_message():
    url = 'https://localhost:8080'
    response = requests.get(url, verify='ca_certificates_for_client/ca_public_key.pem')
    print(f'Secret message: {response.text}')


if __name__ == '__main__':
    get_secret_message()
