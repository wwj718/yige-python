# -*- coding: utf-8 -*-
try:
    from inspect import signature
except ImportError:
    from funcsigs import signature
import logging
class ActionHandle(object):

    """help to manage yige action flow
    """

    def __init__(self,query_response,logger=None):
        # module log https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/
        self.logger = logger or logging.getLogger(__name__)
        assert query_response.status_code == 200 #断言它是有效的query response 200
        self.query_response = query_response

    def action_a(self):
        """
        for test
        """
        return "action_a"


class MyActionHandle(ActionHandle):

    def __init__(self,query_response):
        ActionHandle.__init__(self,query_response)
    def action_c(self,**kwargs):
        '''
        可选参数
        kwargs.get("") 直接拿到key value
        '''
        return "action_c:"+str(kwargs)

def run_action(actionHandleInstance,confidence =0.5,logger=None):
        '''
        执行action
        获取所有以action开头的函数 然后拿到签名，调用它 模仿pytest
        同名函数优先级越往下越高
        conferance  默认高于0.5时才运行
        返回 {success:True,data:,message:""}
        ? 是否需要自动参数补全功能，不全的化自动要求补全  和网页一样
        '''
        #import IPython;IPython.embed()
        # todo log 输入输出都记录下
        logger = logger or logging.getLogger(__name__)
        query_response_json = actionHandleInstance.query_response.json()

        status_code = query_response_json["status"]["code"]
        answer = query_response_json["answer"]
        if status_code == 201 :
            # 不存在，直接被闲聊接手
            # todo : status 201 更精确
            response={}
            response["success"] = False
            response["answer"] = answer
            response["message"] = "chat auto by yige"
            # warning_type
            # todo 定义出一堆错误码 模仿微信
            return response
        response_confidence = query_response_json.get("confidence")
        if  response_confidence <= confidence:
            response={}
            response["success"] = False
            response["message"] = "confidence is low: {} , is should >= {}".fotmat(query_response_json["confidence"],confidence)
            logger.warning(response["message"])
            return response
        action = query_response_json["action"]
        action_complete = action["complete"]
        if  not action_complete:
            # 强制参数是否收集完成
            response={}
            response["success"] = False
            response["answer"] = answer
            response["message"] = "action parameters do not be collect completely "
            logger.warning(response["message"])
            return response
        action_name = action["name"]# 可能不存在
        parameters_json = action["parameters"] #list to  [{}{}] 取出来然后聚合 [(a,b)(c,d)]   {} key value
        # dict([("a","b"),("c","d")])
        # 把answer加上
        parameters = dict([(p["name"],p["value"]) for p in parameters_json])
        parameters["_answer"] = answer
        action_functions_name = [function for function in dir(actionHandleInstance) if function.replace("action_","")== action_name]
        #print(action_functions_name) #none
        for action_function_name in action_functions_name:
            func = getattr(actionHandleInstance,action_function_name)
            # 根据函数的参数数量决定传参
            #fun_arg_len = len(signature(func).parameters.keys())
            #print(fun_arg_len) #0 ,1
            #return func(*[query_response][:fun_arg_len]) #动态传参 应该直接传入 action对应的参数 **kwargs
            response={}
            response["success"] = True
            response["message"] = None
            response["action_name"] = action_name #记录下命中的action
            response["data"] = func(**parameters)
            return response
        return None

# http://stackoverflow.com/questions/4374563/python-call-all-methods-of-an-object-with-a-given-set-of-arguments

