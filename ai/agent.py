import json

import google.generativeai as genai
from django.conf import settings
from django.core import serializers

from ai.models import AIResult
from ai.prompt import SYSTEM_PROMPT, USER_PROMPT
from outflows.models import Outflow
from products.models import Product


class SGEAgent:
    def __init__(self):
        self.__client = settings.GOOGLE_API_KEY
        genai.configure(api_key=self.__client)

    def __get_data(self):
        products = Product.objects.all()
        outflows = Outflow.objects.all()
        return json.dumps(
            {
                "products": serializers.serialize("json", products),
                "outflows": serializers.serialize("json", outflows),
            }
        )

    def invoke(self):
        model = genai.GenerativeModel(
            model_name=settings.GOOGLE_MODEL_ID, system_instruction=SYSTEM_PROMPT
        )
        prompt = USER_PROMPT.replace("{{data}}", self.__get_data())
        result = model.generate_content(prompt)
        AIResult.objects.create(result=result.text)
