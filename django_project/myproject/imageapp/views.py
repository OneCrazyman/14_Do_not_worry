from django.shortcuts import render
from .serializers import ImageContentSerializer,AudioContentSerializer
from .models import ImageContent,AudioContent
from rest_framework import viewsets

from django.http import JsonResponse,HttpResponse

import json 
import requests
import time
import os
from gtts import gTTS
import random

class ImageContetnView(viewsets.ModelViewSet):
    serializer_class = ImageContentSerializer
    queryset = ImageContent.objects.all()

    def list(self,request):
        print("--------")
        r = super().list(request)
        print("here")
        print(r)
        print("--------")
        return r

    def create(self,request):

        r = super().create(request)

        data = request.data.dict()

        image_path = f"http://220.69.209.111:8000/media/uploads/{data['image']}"

        text = "안녕하세요"
        try:
            text = OCR(image_path,"jpg")
            tts = gTTS(
                text = text,
                lang = "ko",
                slow = False,
            )
            print(text)
            

            audio_name = f"{random.randint(100000,999999)}"
            #audio_name ="123"
            tts.save(f"/home/bigdata/gdsc/14_Do_not_worry/django_project/myproject/media/uploads/music/{audio_name}.mp3")
            audio_path = f"http://220.69.209.111:8000/media/uploads/music/{audio_name}.mp3"
            print("success")

            return JsonResponse({"text":text,"audio_path":audio_path},json_dumps_params={'ensure_ascii': False})
        except:
            audio_path = f"http://220.69.209.111:8000/media/uploads/music/fail.mp3"
            return JsonResponse({"text":"이미지 인식이 불가합니다.","audio_path":audio_path},json_dumps_params={'ensure_ascii': False})




def test(request):
    fname= "/home/bigdata/gdsc/resource/ex_ko.mp3"
    file = open(fname, "rb")
    print("파일")
    print(file)
    response = HttpResponse()
    response.write(file.read())
    response['Content-Type'] ='audio/mp3'
    response['Content-Length'] =os.path.getsize(fname )
    return response



def OCR(image_url,file_format):
    url = r"https://o4w2xz6c6e.apigw.ntruss.com/custom/v1/14095/94e44585f1c3b04fbe32a517993fd4a6e966ca98cf1b37651517ccdec3efce6c/general"
    headers = {"Content-Type":"application/json",
           "X-OCR-SECRET":"b0pJS1p2R3lHQ0RhYUV4Vlp0WWpYd2RWZ0FUdm5mSUc="
          }
    timestamp = time.time()
    print(timestamp)
    body = {
    "images": [
      {
        "format": file_format,
        "name": "medium",
        "data": None,
        "url": image_url
      }
    ],
    "lang": "ko",
    "requestId": "string",
    "resultType": "string",
    "timestamp": timestamp,
    "version": "V1"
}

    r = requests.post(url,headers=headers,json=body).json()
  
    text = ""
    for i in r['images']:
        for j in i['fields']:
            text += j['inferText']+ " "

    text = text.strip()
    return text




class AudioContetnView(viewsets.ModelViewSet):
    serializer_class = AudioContentSerializer
    queryset = AudioContent.objects.all()