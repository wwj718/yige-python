#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os.path
import sys

try:
    import yige
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import yige

#import uuid

DEV_ACCESS_TOKEN = os.environ.get("DEV_ACCESS_TOKEN")


def main():
    ai = yige.Yige(DEV_ACCESS_TOKEN)

    # some unuque session id for user identification
    '''
    entries = [
        apiai.UserEntityEntry('Firefox', ['Firefox']), #辅助类
        apiai.UserEntityEntry('XCode', ['XCode']),
        apiai.UserEntityEntry('Sublime Text', ['Sublime Text'])
    ]
    '''
    payload= {}
    payload["name"] = "zhubo_test_from_yige_sdk"
    payload["type"] = 1
    payload["automated_expansion"] = 0
    payload["entries"] = []
    zhubo1 =  {
                "value": "逻辑思维",
                "synonyms": [
                    "罗振宇",
                    "老罗",
                    "罗胖"
                ]
            }
    payload["entries"].append(zhubo1)
    user_entities_request = ai.user_entities_request()
    user_entities_request.user_entities = payload
    user_entities_response = user_entities_request.getresponse() #真正发送
    print(user_entities_response.json())

if __name__ == '__main__':
    main()
