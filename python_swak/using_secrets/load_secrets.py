from dotenv import load_dotenv, dotenv_values
import os
import json


def read_secrets_from_dotenv():
    """
    read secrets from .env file, remember to add .env to .gitignore!
    pip install python-dotenv
    :return:
    """
    load_dotenv()
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")

    print("API_KEY: ", api_key)
    print("API_SECRET: ", api_secret)

    secrets = dotenv_values(".env")
    print("API_KEY: ", secrets["API_KEY"])
    print("API_SECRET: ", secrets["API_SECRET"])
    print('-' * 50)


def read_secrets_from_json():
    """
    read secrets from secrets.json file, remember to add secrets.json to .gitignore!
    :return:
    """

    def get_value_from_json(json_file: str, key: str, sub_key: str) -> str:
        try:
            with open(json_file) as f:
                data = json.load(f)
                return data[key][sub_key]
        except Exception as e:
            print("Error: ", e)

    print(get_value_from_json(".env.json", "db", "host"))
    print('-' * 50)


def read_secrets_from_environment_variables():
    """
    linux: export API_KEY=your_api_key
    windows: setx API_KEY your_api_key
    :return:
    """
    print(os.environ.get("API_KEY"))
    print(os.environ.get("API_SECRET"))
    print('-' * 50)


def read_secrets_from_azure_key_vault():
    print('check: https://learn.microsoft.com/en-us/azure/key-vault/secrets/quick-create-python?tabs=azure-cli')
    print('-' * 50)


def read_secrets_from_hashicorp_vault():
    print('check: https://developer.hashicorp.com/vault/tutorials/getting-started/getting-started-install')
    print('-' * 50)


if __name__ == '__main__':
    read_secrets_from_dotenv()
    read_secrets_from_json()
    read_secrets_from_environment_variables()
    read_secrets_from_azure_key_vault()
    read_secrets_from_hashicorp_vault()
