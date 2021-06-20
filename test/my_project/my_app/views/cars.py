from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.cars import Cars
from django.core import serializers
import json
from cerberus import Validator
from datetime import datetime
from ..helpers.helper import check_token

class CarsApi(APIView):
    def get(self,request):
        return Response({
            "data" : json.loads(serializers.serialize('json', Cars.objects.all())),
        }, status = status.HTTP_200_OK)

    def post(self,request):
        to_date = lambda s: datetime.strptime(s, '%Y-%m-%d')
        if not Validator({
            "model" : {"required" : True, "type": "string"},
            "color" : {"required" : True, "type": "string"},
            "date" : {"required" : True, "type": "datetime", "coerce": to_date},
        }).validate(request.data):
            return Response({
                "code" : "invalid_body",
                "detailed": "Cuerpo con estructura inválida",
            },status = status.HTTP_400_BAD_REQUEST)
        if not check_token(request):
            return Response(status = status.HTTP_401_UNAUTHORIZED)
        car = Cars.objects.create(**request.data)
        return Response({
            "car_id" : car.id
        },status =status.HTTP_201_CREATED)

    def patch(self,request, pk):
        to_date = lambda s: datetime.strptime(s, '%Y-%m-%d')
        if not Validator({
            "model" : {"required" : True, "type": "string"},
            "color" : {"required" : True, "type": "string"},
            "date" : {"required" : True, "type": "datetime", "coerce": to_date},
        }).validate(request.data):
            return Response({
                "code" : "invalid_body",
                "detailed": "Cuerpo con estructura inválida",
            },status = status.HTTP_400_BAD_REQUEST)
        if not check_token(request):
            return Response(status = status.HTTP_401_UNAUTHORIZED)
        car = Cars.objects.filter(pk = pk)
        if not car:
            return Response({
                "code" : "not_found",
                "detailed": "El ID de automovil no existe",
            },status = status.HTTP_404_NOT_FOUND)
        car.update(**request.data)
        return Response({
            "data" : json.loads(serializers.serialize('json', car))
        },status =status.HTTP_200_OK)
    
    def delete(self,request,pk):
        car = Cars.objects.filter(pk = pk)
        if not car:
            return Response({
                "code" : "not_found",
                "detailed": "El ID de automovil no existe",
            },status = status.HTTP_404_NOT_FOUND)
        if not check_token(request):
            return Response(status = status.HTTP_401_UNAUTHORIZED)
        car.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)