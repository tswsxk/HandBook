# 单元测试

## Pytest

pytest 有两个比较重要的配置文件：
* pytest.ini
* setup.cfg

### Reference

#### [组参数测试](https://docs.pytest.org/en/latest/parametrize.html#pytest-mark-parametrize-parametrizing-test-functions)

```python
@pytest.mark.parametrize("params_name", ["p1", "p2", "p3"])
def test_func(params_name):
  print(params_name)
# 总共三次测试，params_name对应的值依次为 p1,p2和p3
```

#### 标准输入输出

```python
# using global variable capsys
def test_flush_print(capsys):
    print("test")
    captured = capsys.readouterr()
    assert captured.out == "test flush print"
```

### pytest.ini

#### 忽略特定的检查项目

```text
# pep8
pep8ignore = E402 E201 E231
# flake8, see https://flake8.pycqa.org/en/latest/user/error-codes.html for details
flake8-ignore = E402 F401 F403 F405 F821 F841 W605
```

#### 重新设置单行长度限制
```text
# pep8
pep8maxlinelength = 120
# flake8
flake8-max-line-length = 120
```

### setup.cfg

#### 忽略文件或文件夹

```text
[coverage:run]
omit =
    some dir/some dir/some dir/omit.py
    some dir/some dir/omit_dir/*
[coverage:report]
....
```

### Q & A

* pytest 4.5 出现 marker warning 的解决方案：
```text
# for pep8
markers =
    pep8: pep8
# for flake8
markers
  	flake8: flake8
```

* 如何忽略特定的docstring test
  `PYTEST_DONT_REWRITE`
* 模拟

### 参考资料

1. [Pytest 使用手册](https://learning-pytest.readthedocs.io/zh/latest/index.html)