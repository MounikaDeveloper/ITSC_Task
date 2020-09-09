from django.views.generic import View
import json
import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def ping():
    return 200


class DateTime1(View):

    def get(self,request):
        x = datetime.datetime.now()
        current_date=x.strftime("%d-%m-%Y")
        print(current_date)
        data = {"statuscode": 200}
        json_data = json.dumps(data)
        #current date is matched to specified date then display status-ok else only display statuscode 200
        if current_date=='09-09-2020':
            status= ping()
            print(status)
            if status==200:
                data={"status":"OK"}
                #converting dictionary to json
                json_data=json.dumps(data)
                return HttpResponse(json_data, content_type="application/json")

        return HttpResponse(json_data, content_type="application/json")
