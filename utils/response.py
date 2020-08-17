from __future__ import unicode_literals
import json
from .exception import CommonErrorMessages, CommonError
from django.http import HttpResponse

import json
class Result(object):
    def __init__(self, code, message, data):
        self.code = code
        self.message = message
        self.data = data


class Response_Code(object):
    success = 200
    fail = 500

    def __init__(self):
        pass


class Result_Factory(object):
    @staticmethod
    def generate_result(status, data=None, message=None):
        result = None

        if status is True:
            result = Result(Response_Code.success, "success", data)
            status = 200
        else:
            result = Result(Response_Code.fail, message, None)
            status = 500
        serilized_result = Result_Util.serilization_result(result)
        return HttpResponse(serilized_result, status=status, content_type='application/json')

    @staticmethod
    def generate_result_base64(status, data=None, message=None):
        if status is True:
            status = 200
        return Response(data=data, status=status)


class Result_Util(object):
    @staticmethod
    def serilization_result(result: Result):
        response = json.dumps(result.__dict__)
        return response

    @staticmethod
    def get_json_from_request(request):
        try:
            json = request.get_json()
            return json
        except Exception as e:
            raise CommonError(CommonErrorMessages.Invalid_Post_Format)

    @staticmethod
    def get_field_from_json(json, field):
        try:
            value = json[field]
            return value
        except Exception as identifier:
            raise CommonError(CommonErrorMessages.No_Such_field.format(field))

    @staticmethod
    def get_args_from_request(request):
        try:
            args = request.GET
            return args
        except Exception as e:
            raise CommonError(CommonErrorMessages.NO_Requst_Args_Error)
    
    @staticmethod
    def get_fields_from_get_method_args(request,fileds_list):
        result={}
        args=Result_Util.get_args_from_request(request)
        for per in fileds_list:
            filed=Result_Util.get_field_from_request_args(args,per)
            result[per]=filed
        return result

    @staticmethod
    def get_fields_from_body(request,fileds_list):
        result={}
        args=Result_Util.__get_post_data(request)
        for per in fileds_list:
            filed=Result_Util.get_field_from_request_args(args,per)
            result[per]=filed
        return result

    @staticmethod
    def __get_post_data(request):
        try:
            args = request.body
            return json.loads(args)
        except Exception as e:
            print(e)
            raise CommonError(CommonErrorMessages.No_Post_Data)

    @staticmethod
    def get_field_from_request_args(args, field):
        try:
            value = args[field]
            return value
        except Exception as identifier:
            raise CommonError(CommonErrorMessages.No_Such_field.format(field))

    @staticmethod
    def get_file_from_request(request):
        try:
            args = request.FILES
            return args
        except Exception as e:
            raise CommonError(CommonErrorMessages.NO_Requst_Args_Error)

    @staticmethod
    def get_header_from_request(request):
        try:
            args = request.headers
            return args
        except Exception as e:
            raise CommonError(CommonErrorMessages.No_Header)

    @staticmethod
    def get_filed_from_header(headers,filed_name):
        try:
            value = headers[filed_name]
            return value
        except Exception as identifier:
            raise CommonError(CommonErrorMessages.No_Such_field_In_Header.format(filed_name))
