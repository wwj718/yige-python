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

CLIENT_ACCESS_TOKEN = os.environ.get("YIGE_ACCESS_TOKEN") #export YIGE_ACCESS_TOKEN=xxx

def main():
    ai = yige.Yige(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    #request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>" # 就用微信的openid

    #request.query = "我想听老罗" #ok
    #request.query = "我想听" #ok
    # >>> python send_text_example.py 老罗
    request.query = sys.argv[1] #"老罗" #ok

    response = request.getresponse() #注意置信度 confidence
    # 各个返回值的含义：http://docs.yige.ai/Query%E6%8E%A5%E5%8F%A3.html
    if (sys.version_info > (3, 0)):
        # Python 3 code in this block
        print(response.json())
    else:
        # Python 2 code in this block
        print(repr(response.json()).decode("unicode-escape"))


if __name__ == '__main__':
    main()
