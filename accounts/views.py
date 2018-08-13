# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.views.generic import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.utils.encoding import python_2_unicode_compatible
from django.views.generic import View
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
#from accounts.forms import PhotoForm
#from accounts.models import Photo
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.conf import settings
from models import FileNameModel
from models import Result
from time import sleep

import sys, os
import base64
import logging
from datetime import datetime

import requests
import json
import base64
import config
import os
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.dirname(os.path.abspath(__file__)) + "/Datalab-9920cee474e2.json"

bucket_name = 'pictoname'
bucket = storage.Client().get_bucket(bucket_name)
storage_path = 'https://storage.googleapis.com/%s/' % bucket_name

UPLOADE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/static/files/'
UPLOADE_DIR_Storage=storage_path+ 'static/files/'

def form(request):
    if request.method != 'POST':
        return render(request, 'accounts/index.html')
    #print (1)
    postPara=request.POST['photo']
    #print ('debug:'+postPara)
    file = base64.decodestring(postPara)
    filename=datetime.now().strftime("%Y%m%d%H%M%S")+'.png'
    path = os.path.join(UPLOADE_DIR, filename)
    destination = open(path, 'wb')

    destination.write(file)

    KEY = config.API_KEY
    url = 'https://vision.googleapis.com/v1/images:annotate?key='
    api_url = url + KEY

    # 画像読み込み
    img_content = postPara

    #print('img_content:' + img_content)

    # リクエストBody作成
    req_body = json.dumps({
        'requests': [{
            'image': {
                'content': img_content
            },
            'features': [{
                'type': 'LABEL_DETECTION',
                'maxResults': 10,
            }]
        }]
    })
    # リクエスト発行
    res = requests.post(api_url, data=req_body)
    #print ('res:' + json.dumps(req_body))
    # リクエストから画像情報取得
    res_json = res.json()
    #print ('res_json:'+json.dumps(res_json))

    labels = res_json['responses'][0]['labelAnnotations']
    for value in labels:
        print 'description:'+value['description']+'score:'+str(value['score'])
    #print 'description111111111111:'+res_json['responses'][0]['labelAnnotations'][0]['description']
    insert_data_result = \
        Result(
            result1=res_json['responses'][0]['labelAnnotations'][0]['description'],
           result2 = res_json['responses'][0]['labelAnnotations'][1]['description'],
            result3=res_json['responses'][0]['labelAnnotations'][2]['description'],
            result4=res_json['responses'][0]['labelAnnotations'][3]['description'],
            result5=res_json['responses'][0]['labelAnnotations'][4]['description'],
            result6=res_json['responses'][0]['labelAnnotations'][5]['description'],
            result7=res_json['responses'][0]['labelAnnotations'][6]['description'],
             result8=res_json['responses'][0]['labelAnnotations'][7]['description'],
            result9=res_json['responses'][0]['labelAnnotations'][8]['description'],
            result10=res_json['responses'][0]['labelAnnotations'][9]['description'],
            score1=res_json['responses'][0]['labelAnnotations'][0]['score'],
            score2=res_json['responses'][0]['labelAnnotations'][1]['score'],
            score3=res_json['responses'][0]['labelAnnotations'][2]['score'],
            score4=res_json['responses'][0]['labelAnnotations'][3]['score'],
            score5=res_json['responses'][0]['labelAnnotations'][4]['score'],
            score6=res_json['responses'][0]['labelAnnotations'][5]['score'],
            score7=res_json['responses'][0]['labelAnnotations'][6]['score'],
            score8=res_json['responses'][0]['labelAnnotations'][7]['score'],
             score9=res_json['responses'][0]['labelAnnotations'][8]['score'],
             score10=res_json['responses'][0]['labelAnnotations'][9]['score'],
            result_from_user=request.user.username,
            file_name=filename
                    )
    insert_data_result.save()
    insert_data = FileNameModel(file_name=filename, userID=request.user.username,result_id=insert_data_result.id)
    #print ('request.user.id:' + request.user.username)
    insert_data.save()
    upload_blob(bucket_name,UPLOADE_DIR+filename,'static/files/'+filename)
    os.remove(UPLOADE_DIR+filename)
    return redirect('/list')

def list(request):
    data={
        'Files':FileNameModel.objects.filter(userID=request.user.username).order_by('-upload_time'),
        'UPLOADE_DIR_Storage':UPLOADE_DIR_Storage
    }
    return render(request,'accounts/list.html',data)

class Index(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'accounts/index.html')

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))