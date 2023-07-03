import json;
from openai_manager import OpenAIManager

openai_test = OpenAIManager().get_instance()

# Carregar o JSON
data = json.loads(str(OpenAIManager()._list_models()))

# Listar os nomes dos itens
for item in data['data']:
    print(item['id'])

#// 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