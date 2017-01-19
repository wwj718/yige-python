# encoding: utf-8
from __future__ import unicode_literals
import os
import requests


class TextRequest(object):
    '''
        doc:http://docs.yige.ai/Query%E6%8E%A5%E5%8F%A3.html
        todo:action (wit.ai)
    '''
    @property
    def query(self):
        """
            Query parameter, can be string or array of strings.
            Default equal None, nut your should fill this field before send
            request.
            :rtype: str or unicode
        """
        return self._query

    @query.setter
    def query(self, query):
        self._query = query

    def __init__(self, client_access_token, base_url, version,
                 session_id):
        # query是直接请求还是，设置，重复利用
        # 延迟触发 getresponse,使用类来做，初始化好，然后query随时调整
        self.query = None

        path = "/v1/query"
        self.query_url = base_url + path
        self.payload = {}
        self.payload["token"] = client_access_token  #客户端toke
        self.payload["session_id"] = session_id

    def getresponse(self):
        self.payload["query"] = self._query
        r = requests.post(self.query_url, data=self.payload)
        return r  #不做任何处理，直接返回

        # 如果解析出意图 or 如果没有解析出意图 (置信度)



class UserEntitiesRequest(object):
    '''
        doc: http://docs.yige.ai/%E8%AF%8D%E5%BA%93.html
        todo: CURD
    '''
    @property
    def user_entities(self):
        "user_entities parameter for specification of same user entities."
        return self._user_entities

    @user_entities.setter
    def user_entities(self, user_entities):
        self._user_entities = user_entities

    def __init__(self, client_access_token, base_url, version):#,user_entities):
        self._user_entities = None
        #self.client_access_token = client_access_token #os.environ.get("YIGE_DEV_TOKEN")  # export YIGE_DEV_TOKEN=xxx
        self.headers = {
            "Authorization": "{}".format(client_access_token),  # 开发者token
            "Content-Type": "application/json; charset=utf-8"
            #"User-Agent": "PythonClient/0.1 by python client"
        }
        path = "/v1/entities"  
        self.entity_url  = base_url + path
        #self.url = "http://httpbin.org/post"  # test 正常
    
    def getresponse(self):
            response = requests.post(self.entity_url,
                                     json=self.user_entities,
                                     headers=self.headers,
                                     verify=False)
            return response

class IntentsRequest(object):
    '''
    doc:http://docs.yige.ai/%E5%9C%BA%E6%99%AF%E6%8E%A5%E5%8F%A3.html
    todo:
        CRUD : 类比django orm
    '''
    def __init__(self, client_access_token, base_url, version):
        pass