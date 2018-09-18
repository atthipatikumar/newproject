from django.http import Http404, HttpResponse, HttpResponseBadRequest
import json
from django.conf import settings
from newproject.db import query
#import MySQLdb
#db = MySQLdb.connect(host="",user="root",passwd="kumar5225",db="onlineindia",port="")


def register1(request):
    ID = request.POST.get('ID', '')
    firstname = request.POST.get('firstname', '')
    lastname = request.POST.get('lastname', '')
    email = request.POST.get('email', '')
    zipcode = request.POST.get('zipcode', '')
    sex = request.POST.get('sex', '')
    birth = request.POST.get('birth', '')
    password = request.POST.get('password', '')

    if ID != '':
        sql = "SELECT * from onlineregister WHERE ID= %s"
        param_for_user_details = [ID]

    elif firstname != '':
        sql = "SELECT * from onlineregister WHERE firstname= %s"
        param_for_user_details = [firstname]
    elif lastname != '':
        sql = "SELECT * from onlineregister WHERE lastname= %s"
        param_for_user_details = [lastname]
    elif email != '':
        sql = "SELECT * from onlineregister WHERE email= %s"
        param_for_user_details = [email]
    elif zipcode != '':
        sql = "SELECT * from onlineregister WHERE zipcode= %s"
        param_for_user_details = [zipcode]
    elif sex != '':
        sql = "SELECT * from onlineregister WHERE sex= %s"
        param_for_user_details = [sex]
    elif birth != '':
        sql = "SELECT * from onlineregister WHERE birth= %s"
        param_for_user_details = [birth]
    elif password != '':
        sql = "SELECT * from onlineregister WHERE password= %s"
        param_for_user_details = [password]
    else:
        sql = "SELECT * from onlineregister"
        param_for_user_details = []
    results = query(sql, *param_for_user_details)
    final_test_map = []
    metadata_totalcount = 0
    # result is constructed in the expected format
    for result in results:
        metadata_totalcount = metadata_totalcount + 1
        response_map = {}
        response_map['ID'] = result['ID']
        response_map['firstname'] = result['firstname']
        response_map['lastname'] = result['lastname']
        response_map['email'] = result['email']
        response_map['zipcode'] = result['zipcode']
        response_map['sex'] = result['sex']
        response_map['birth'] = result['birth']
        response_map['password'] = result['password']
        final_test_map.append(response_map)
    metadata = {"total_count": metadata_totalcount}
    response = {"metadata": metadata, 'data_test': final_test_map}
    data = json.dumps(response, encoding='ISO-8859-1')
    http_response = HttpResponse(data, content_type="application/json")
    #kwargs['encoding'] = 'safe-utf-8'
    return http_response


def login1(request):
    user_id = request.POST.get('user_id', '')
    email_id = request.POST.get('email_id', '')
    password = request.POST.get('password', '')

    if user_id != '':
        sql = "SELECT * from login WHERE user_id= %s"
        param_for_user_details = [user_id]

    elif email_id != '':
        sql = "SELECT * from login WHERE email_id= %s"
        param_for_user_details = [email_id]
    elif password != '':
        sql = "SELECT * from login WHERE password=%s"
        param_for_user_details = [password]

    else:
        sql = "SELECT * from login"
        param_for_user_details = []
    results = query(sql, *param_for_user_details)
    final_test_map = []
    metadata_totalcount = 0
    # result is constructed in the expected format
    for result in results:
        metadata_totalcount = metadata_totalcount + 1
        response_map = {}
        response_map['user_id'] = result['user_id']
        response_map['email_id'] = result['email_id']
        response_map['password'] = result['password']
        final_test_map.append(response_map)
    metadata = {"total_count": metadata_totalcount}
    response = {"metadata": metadata, 'data_test': final_test_map}
    data = json.dumps(response, encoding='ISO-8859-1')
    http_response = HttpResponse(data, content_type="application/json")
    #kwargs['encoding'] = 'safe-utf-8'
    return http_response

