# -*- coding: utf-8 -*-
import uuid
#import requests
from .yige_requests import (
    #VoiceRequest,
    TextRequest,
    UserEntitiesRequest,
    #events
)

DEFAULT_VERSION = '20170115' #python client version

class Yige(object):
    """
    Main endpoint for using yige.ai
    Provides request.

    Basic Usage::
            >>> ...
            >>> import yige
            >>> ai = yige.Yige(<CLIENT_ACCESS_TOKEN>)
            >>> text_request = ai.text_request()
            >>> ...
        :param client_access_token: client access token provided by http://yige.ai/
        :type client_access_token: str or unicde
    """
    # property 允许设置前校验

    @property
    def client_access_token(self):
        """
            Client access token provided by https://yige.ai/
            :rtype: str or unicode
        """

        return self._client_access_token

    @client_access_token.setter
    def client_access_token(self, client_access_token):
        """
            :type client_access_token: str or unicode

            todo: use env var? os.environ.get("yige_client_access_token")
        """

        self._client_access_token = client_access_token

    @property
    def session_id(self):
        """
            session_id user for unique identifier of current application user.
            And it provide different contexts and entities for different users.
            Default it generated like uuid for every object of `Yige` class.
            :rtype: str or unicode
        """

        return self._session_id



    @session_id.setter
    def session_id(self, session_id):
        """
            :type session_id: str or unicode
        """

        self._session_id = session_id

    def __init__(self, client_access_token, session_id=None):
        super(Yige, self).__init__()
        self._client_access_token = client_access_token

        self._base_url = 'http://api.yige.ai'
        self._version = DEFAULT_VERSION

        if session_id is None:
            self._session_id = uuid.uuid4().hex
        else:
            self._session_id = session_id

    def text_request(self):
        """
            Fields of request default filled from `Yige` parameters
            (session_id, version,client_access_token).
            Returns `TextRequest` object.
            :rtype TextRequest:
        """

        request = TextRequest(
            self.client_access_token,
            self._base_url,
            self._version,
            self.session_id
        )

        return request
    
    # 增删，自定义实体
    def user_entities_request(self, user_entities=None):
        """
            Construct a `UserEntitiesRequest`, prepare it.
            Returns `UserEntitiesRequest` object.
            :rtype UserEntitiesRequest:
        """

        if user_entities is None:
            user_entities = []

        request = UserEntitiesRequest(
            self.client_access_token, # 这个是dev token
            self._base_url,
            self._version
            #user_entities
        )

        return request