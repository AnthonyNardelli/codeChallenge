from rest_framework.views import APIView
from rest_framework.response import Response
from ast import literal_eval
from iteration_utilities import deepflatten
from .models import Results

class Flattener(APIView):
    def post(self, request):
        original_list= literal_eval(request.data['items'])
        flat_list = list(deepflatten(original_list))
        Results.objects.create(data=flat_list)
        return Response({"content":flat_list,"type":"Results"})

    def get(self, requests):
        results = [item.data for item in Results.objects.all()]
        print(results)
        return Response({'Results': results})
