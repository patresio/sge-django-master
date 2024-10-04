import google.generativeai as genai
from decouple import config

genai.configure(api_key=config("GOOGLE_API_KEY"))


def get_brand_description(name):
    model = genai.GenerativeModel("gemini-1.0-pro-latest")
    prompt = f"""
        Faça uma descrição sobre a marca {name} em apenas 100 caracteres. Mostre detalhes importantes.
    """
    response = model.generate_content(prompt)
    return response.text
