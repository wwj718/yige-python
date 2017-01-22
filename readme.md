# yige-python

为yige.ai写的python sdk.  [英文版](https://github.com/wwj718/yige-python/blob/master/README.rst)

开源协议: MIT license
Documentation: https://yige-python.readthedocs.io.

# 简介
yige.ai的非官方python sdk，方便大家在python下使用yige.ai

# 特性
*  命令行调试界面
*  query
*  实体创建

# 安装
`pip install yige`

或者源码安装：

`pip install https://github.com/wwj718/yige-python.git`


# 使用

### 在命令行里使用（debug console）
```
export YIGE_ACCESS_TOKEN=xxx #客户端访问令牌
yige --console #初次运行会安装ipython
```

![](http://oav6fgfj1.bkt.clouddn.com/yige0b001117.png)

深入调试

![](http://oav6fgfj1.bkt.clouddn.com/yige792db9bd.png)

### 作为python库使用

1. query

```python
CLIENT_ACCESS_TOKEN = '<YOUR_CLIENT_ACCESS_TOKEN>' #客户端访问令牌
ai = yige.Yige(CLIENT_ACCESS_TOKEN)
request = ai.text_request()
request.query = "我想买鞋"
response = request.getresponse() #注意置信度 confidence
print(response.json())
```

2.  实体创建

```python
DEV_ACCESS_TOKEN = '<YOUR_DEV_ACCESS_TOKEN>' #开发者访问令牌
ai = yige.Yige(DEV_ACCESS_TOKEN)
payload= {}
payload["name"] = "脚型" # 词库名称
payload["type"] = 1 #是否定义同义词 1是  0否
payload["automated_expansion"] = 0
payload["entries"] = [] # 词库内容
entity1 =  {
             "value": "正常内旋", # 同义词中比较权威的名称
             "synonyms": [ #  同义词
                 "正常内旋",
                 "内旋正常",
                 "正常足弓",
                 "足弓正常"
             ]
         }
payload["entries"].append(entity1)
user_entities_request = ai.user_entities_request()
user_entities_request.user_entities = payload
user_entities_response = user_entities_request.getresponse()
print(user_entities_response.json())
```

3. 创景

waiting...

# 例子 🌰

1. 可以直接翻阅examples目录下的例子 🌰
2. 记得在网页里获得你的CLIENT_ACCESS_TOKEN


# 测试
`make test`

# Credits
This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage) project template.
