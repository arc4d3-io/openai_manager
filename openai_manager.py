import configparser
import openai
from logger import Logger
from mac_encryptor import MACAddressEncryptor

class OpenAIManager:
    def __init__(self, api_key=None, api_key_path='config.ini', log_level="ERROR", log_file='logs/openai_manager.log'):
        self.api_key = api_key
        self.api_key_path = api_key_path
        self.logger = Logger(__name__, level=log_level, log_file=log_file)
        self._openai = openai

        # Initialize OpenAI with the API key
        self._openai.api_key = self.api_key if self.api_key else self._read_api_key_from_disk()

    def _read_api_key_from_disk(self):
        try:
            config = configparser.ConfigParser()
            config.read(self.api_key_path)
            key_path = config.get('OPENAI', 'api_key_path')
            self.logger.log('API key read from disk', 'info')
            encrypt = MACAddressEncryptor()
            return encrypt.decrypt(encrypt.load_encryption_from_file(key_path))
        except Exception as e:
            self.logger.log(f'Failed to read API key from disk: {str(e)}', 'error')
            return None

    def get_available_models(self, organization=None):
        if organization:
            self._openai.organization = organization
        try:
            return self._openai.Model.list()
        except Exception as e:
            self.logger.log(f'Failed to list models: {str(e)}', 'error')
            return []

    def set_api_key(self, api_key):
        self.api_key = api_key
        self._openai.api_key = api_key
        self.logger.log(f'API key set: {api_key}', 'info')

    def get_api_key(self):
        return self.api_key

    @classmethod
    def get_instance(cls, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = cls(**kwargs)
        return cls._instance

    def get_openai_instance(self):
        return self._openai

if __name__ == "__main__":
    # Example usage:
    openai_manager = OpenAIManager(log_level="DEBUG")
    models = openai_manager.get_available_models()
    print(models)
