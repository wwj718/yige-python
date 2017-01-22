# 开发笔记

# python trick
[stackoverflow-py-top-qa](https://github.com/wklken/stackoverflow-py-top-qa/blob/master/contents/qa-func.md)

### 用函数名字符串调用一个函数
```
import actions
methodToCall = getattr(actions, 'get_track')
result = methodToCall()
```

### `**`和`*`
*  `*args`(args名字无所谓)将函数所有参数转为序列

```
def foo(*args):
    for a in args:
        print a
```

*  `*`的另一个用法是用于函数调用时的参数列表解包(unpack):foo(*l)
*  `**kwargs` 将函数所有关键字参数转为一个字典 , **kwargs允许你处理那些你没有预先定义好的已命名参数

```
def bar(**kwargs):
    for a in kwargs:
        print a, kwargs[a]

*  调用的时候使用**kwargs,解包,dict->var

#for name, value in kwargs.items():
```

*  和hasattr配合使用:`if hasattr(obj, 'attr_name')` ,使用"in"而不是"has_key()"

# 字典
### 如何给字典添加一个值
*  data = {}
*  data['a']=1
*  data.update(dict(a=1))

### 如何将字段转换成一个object，然后使用对象-属性的方式读取
使用namedtuple

# yige console
yige --console

说明使用方法在开始, 问号 ,help()

直接解析 类似网页
!debug
!run


# test
```bash
make test # 使用pytest 
```


# todo
兼容python2/3

兼容性：https://github.com/wwj718/NeuralWritingMachine

通过html-input.py案例，可以自定义词法解析高亮



# 参考
https://github.com/api-ai/api-ai-python



