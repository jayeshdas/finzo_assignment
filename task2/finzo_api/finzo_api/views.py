
from rest_framework.views import APIView
from django.http import JsonResponse
import os
from .utils import *

class Report(APIView):
    def post(self,request):
        __body=request.data
        file=__body.get('file')
        if file:
            data=readFile(file)
            if data.shape[0]:
                result=dataAnalysis(data)
                print(result)
                return JsonResponse(result)
            else:
                return JsonResponse({"msg":"data not found!!"})
        else:
            return JsonResponse({"msg":"file not found!!"})
