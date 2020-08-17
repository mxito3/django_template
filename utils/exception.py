class CommonError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class CommonErrorMessages():
    Invalid_Post_Format = "invalid parameter format,please use json"
    No_Such_field = "please pass {} field"
    No_Such_field_In_Header = "please pass {} field in headers"
    NO_Requst_Args_Error = "please pass args "
    CoinPair_Operate_Invalid = "operate_type can only be 0 or 1"
    CoinPair_Operate_Type_Invalid = 'operate_type can only be int type'
    CoinPair_Name_Type_Error = 'coin_pair_name can only be str type'
    CoinPair_Not_Exsit="don't exsit such coin pair"
    No_Suçh_User = "NO Such User"
    No_Permission = '没有权限'
    No_Header='please pass header'
    Token_Wrong='token is wrong'
    Redis_Error="can't connect to redis"
    Symbol_Name_Type_Error = 'symbol can only be str type'
    Symbol_Not_Exsit="don't exsit such  symbol"
    Symbol_Not_Open="please open symbol {} first"
    Related_Coinpair_Not_Close="please close  {}'s related coin pair first"
    GET_Not_Allowed='get method not allowed!'
    No_Post_Data="please pass post data"

class MQ_Error_Message():
    Cannot_Connect='can not connect to mq'
    Write_Error='can not write to mq'
class Order_Error_Messages():
    Symbol_Not_Exsit="symbol  not open or not exsit"
    Order_Side_Error='order side can only be "BUY" or "SELL"'

class USDT_Combine_Error_Message():
    USDT_Type_Error="usdt type can  only be USDT or EUSDT"
    Withdraw_Address_Exist="usdt withdraw address already exist"
