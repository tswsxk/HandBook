# Python基础

## 数据与数据类型

## 基本数据结构

## 基本控制流

## 常用语法糖

### Ellipsis

[Python 的 Ellipsis 对象](https://farer.org/2017/11/29/python-ellipsis-object/)


## pip
安装本地包
```shell
pip install -e .
```
安装 extra_requires
```shell
pip install -e .[test,dev,...]
```

## 包的发布

### setup.py

#### 命令行
在`setup()`中添加：
```python
entry_points={
    "console_scripts": [
        "$command_name = $path2script:$function_name",
    ],
},
```

## 参考资料
[震惊了！每30秒学会一个Python小技巧，Github星数4600+](https://mp.weixin.qq.com/s/ZGNJ2fEb_sFCSE2sZbrDhA)