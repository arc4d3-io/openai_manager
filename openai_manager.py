from logger import Logger
from mac_encryptor import MACAddressEncryptor
import openai
import configparser

class OpenAIManager:
    _instance = None
    _api_key = None

    logger = Logger(__name__, level="ERROR", log_file='logs/openai_manager.log')

    def __new__(cls, api_key=None):
        if not cls._instance:
            cls._instance = super(OpenAIManager, cls).__new__(cls)
            cls._api_key = api_key
            cls._openai = openai
            cls._openai.api_key = cls._api_key if cls._api_key else cls._read_api_key_from_disk()
            cls.logger.log('OpenAIManager instance created', 'info')
        return cls._instance

    @classmethod
    def get_instance(cls) -> openai:
        return cls._openai

    @classmethod
    def get_api_key(cls):
        return cls._api_key

    @classmethod
    def set_api_key(cls, api_key):
        cls._api_key = api_key
        cls._openai.api_key = api_key
        cls.logger.log(f'API key set: {api_key}' , 'info')

    @classmethod
    def _read_api_key_from_disk(cls):
        try:
            config = configparser.ConfigParser()
            config.read('config.ini')
            key_path = config.get('OPENAI', 'api_key_path')
            cls.logger.log('API key read from disk', 'info')
            encrypt = MACAddressEncryptor()
            return encrypt.decrypt(encrypt.load_encryption_from_file(key_path))
        except Exception as e:
            cls.logger.log(f'Failed to read API key from disk: {str(e)}', 'error')
            return None
    @classmethod
    def _list_models(cls):
        cls._openai.organization = "org-C3u9sVYoQKLRSm8Cv02wtytG"
        return cls._openai.Model.list()