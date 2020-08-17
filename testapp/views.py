from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from utils.exception import CommonError,CommonErrorMessages
from utils.response import Result_Factory,Result_Util
# Create your views here.
class Test_View():
    # get mothod
    @staticmethod
    def get(request):
        need_args_list=['uid']
        try:
            args=Result_Util.get_fields_from_get_method_args(request,need_args_list)
        except CommonError as e:
            result = Result_Factory.generate_result(status=False, message=e.args[0])
            return result
        uid=args['uid']
        result = Result_Factory.generate_result(status=True, data=uid)
        return result 
       
    #post method
    @staticmethod
    @csrf_exempt
    def post(request):
        if request.method == "GET":
            result = Result_Factory.generate_result(status=False, message=CommonErrorMessages.GET_Not_Allowed)
            return result
        need_args_list=['uid']
        try:
            args=Result_Util.get_fields_from_body(request,need_args_list)
        except CommonError as e:
            result = Result_Factory.generate_result(status=False, message=e.args[0])
            return result
        uid=args['uid']
        result = Result_Factory.generate_result(status=True, data=uid)
        return result 
