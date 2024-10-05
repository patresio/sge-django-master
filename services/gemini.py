import google.generativeai as genai
from django.conf import settings


class Gemini:
    def __init__(self):
        self.__api_key = settings.GOOGLE_API_KEY
        genai.configure(api_key=self.__api_key)

    def get_brand_description(self, name):
        model = genai.GenerativeModel(
            model_name=settings.GOOGLE_MODEL_ID,
            system_instruction="Voce é um assistente virtual de vendas de produtos. Crie uma descrição sobre o nome da marca e mostre detalhes importantes.",
        )
        prompt = f"""
            Faça uma descrição sobre a marca {name} em apenas 100 caracteres. Mostre detalhes importantes.
        """
        response = model.generate_content(prompt)
        return response.text
