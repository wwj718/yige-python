#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
python2/3
todo:
    *  在ipython中直接调用action调试更爽
    *  命令行工具 yige --console
    *  可替换的后端 yige/zhima
'''

from __future__ import unicode_literals

try:
    #install ipython
    from IPython import embed
except:
    import pip
    pip.main(["install", "ipython"]) # install package dynamically

from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory#InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit.styles import style_from_dict
from prompt_toolkit.token import Token
from prompt_toolkit.validation import Validator, ValidationError #验证

#from pygments.lexers import JsonLexer
import os.path
import sys
import uuid
import json

#from pprint import pprint

try:
    import yige
except ImportError:
    sys.path.append(os.path.join(
        os.path.dirname(os.path.realpath(__file__)), os.pardir))
    import yige

CLIENT_ACCESS_TOKEN = os.environ.get("YIGE_ACCESS_TOKEN"
                                     )  #export YIGE_ACCESS_TOKEN=xxx


######## prompt
DEFAULT_MAX_STEPS = 5
INTERACTIVE_PROMPT = '> '
BOTTOM_TOOLBAR_STYLE = style_from_dict({
        Token.Toolbar: '#ffffff bg:#333333',
        })

def get_bottom_toolbar_tokens(cli):
    return [(Token.Toolbar, '使用: 1.query: 我想买鞋  2.简单调试: !run xxx  3.复杂调试: !debug ')]

class myValidator(Validator):
    def validate(self, document):
        if  not  document.text: #输入为空
            raise ValidationError(message='输入不能为空',
                                  cursor_position=len(document.text))  # Move cursor to end of input.

###########


from pygments import highlight, lexers, formatters
def output_format(obj):
    '''
    python2/3
    中文没有被解析
    obj is dict
    http://stackoverflow.com/questions/35950573/python-unicode-string-to-javascript
    '''
    formatted_json = json.dumps(obj, sort_keys=True, indent=4,ensure_ascii=False).encode('utf8')
    if (sys.version_info > (3, 0)):
            # Python 3 code in this block
            colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
            return colorful_json
    else:
            colorful_json = highlight(unicode(formatted_json, 'UTF-8'), lexers.JsonLexer(), formatters.TerminalFormatter())
            return colorful_json #中文没有解决




def main():
    try:
        input_function = raw_input
    except NameError:
        input_function = input  #python3
    session_id = uuid.uuid1()
    history = FileHistory('/tmp/.yige_prompt') #InMemoryHistory()
    my_completer = WordCompleter(['!print','response',"!run","!debug"])

    # yige
    ai = yige.Yige(CLIENT_ACCESS_TOKEN)
    request = ai.text_request()

    response = None
    while True:
        try:
            # lexer 从网上把词库拉下来缓存到本地，然后高亮
            # 本地输入先做好分词
            # 看文章 sqlite
            # https://github.com/eliangcs/http-prompt yige-prompt
            # https://github.com/donnemartin/haxor-news
            # 自然语言 https://github.com/jonathanslenders/python-prompt-toolkit/blob/master/examples/regular-language.py
            message = prompt(INTERACTIVE_PROMPT,
                             history=history,
                             enable_history_search=True,
                             auto_suggest=AutoSuggestFromHistory(),
                             completer=my_completer,
                             get_bottom_toolbar_tokens=get_bottom_toolbar_tokens,# 底部转态栏
                             style = BOTTOM_TOOLBAR_STYLE,
                             validator = myValidator(),
                             #get_title= fun #"Yige_prompt",
                             ).rstrip()
                             #mouse_support=True).rstrip() #支持鼠标会导致翻页问题
        except (KeyboardInterrupt, EOFError):
            return
        # 用户输入一句话，然后解析，颜色 方便调试？ console ,语法高亮
        #context = run_actions(session_id, message, context, max_steps)
        if message:
            # 仅仅是拿到输入而已，之后要做什么自己决定
            if message.startswith("!run"):
                #在当前上下文执行python
                #上次执行的结果 response 关键词 使用grep?
                code = message.split("run")[-1].strip()
                # 把response变为类似对象
                # 复杂的调试使用ipython 或者进入ipython上下文? 把当前环境带入
                # 在ipython之前诸如上下文?
                try:
                    exec(code) #在上下文执行，python提示
                except Exception as e :
                    print(str(e))
            elif message.startswith("!debug"):
                #帮助安装
                embed(header='yige.ai debug console \n    --  by 『wwj718』(blog.just4fun.site) \n    --  如有建议或bug,欢迎发我邮件:wuwenjie718@gmail.com', banner1='')

            else:
                #查询
                try:
                    request.query = message
                    response = request.getresponse()  #注意置信度 confidence
                    request.session_id = session_id
                    response = request.getresponse()
                    print(output_format(response.json()))
                except Exception as e:
                    print(str(e))


    # 各个返回值的含义：http://docs.yige.ai/Query%E6%8E%A5%E5%8F%A3.html

if __name__ == '__main__':
    main()
