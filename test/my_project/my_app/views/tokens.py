from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.tokens import Tokens
from ..models.cars import Cars
import json
from ..helpers.helper import create_token
from cerberus import Validator

class TokensApi(APIView):
    def post(self,request):
        if not Validator({
            "user" : {"required" : True, "type": "string"},
            "permissions" : {"required" : True, "type": "string","allowed":["user","admin"]},
        }).validate(request.data):
            return Response({
                "code" : "invalid_body",
                "detailed": "Cuerpo con estructura inválida",
            },status = status.HTTP_400_BAD_REQUEST)
        request.data["exp"] = datetime.now() + timedelta(minutes=2)
        token = str(create_token(request.data))
        Tokens.objects.create(**{
            "token" : token
        })
        return Response({"token" : token}, status = status.HTTP_201_CREATED)