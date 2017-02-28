#!/usr/bin/env python
# encoding: utf-8
from yige import Yige,ActionHandle,run_action

class MyActionHandle(ActionHandle):

    def __init__(self,query_response):
        ActionHandle.__init__(self,query_response)
    def action_c(self,**kwargs):
        '''
        可选参数
        kwargs.get("") 直接拿到key value
        '''
        return "action_c:"+str(kwargs)

    def action_get_zhubo_track(self,**kwargs):
        # kwargs is dict _answer
        for name, value in kwargs.items():
            print(name,value)
        return "action ok"
    # todo 如果什么都没命中 yige会接入到闲聊


CLIENT_ACCESS_TOKEN = "E27EAB221C2FF041ABC8D1B3C40373BB" #跑鞋示例
ai = Yige(CLIENT_ACCESS_TOKEN)
request = ai.text_request()
request.query = "哈哈哈" #"我想听老罗" #"我想买鞋"
query_response = request.getresponse()
#print(query_response.json())
a_h = MyActionHandle(query_response)
action_res = run_action(a_h) #try
print(action_res)

