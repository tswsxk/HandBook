# 单元测试

## Pytest

pytest 有两个比较重要的配置文件：
* pytest.ini
* setup.cfg

### 忽略特定的 pep8 项目

```text
pep8ignore = E402 E201 E231
```

### 重新设置 pep8 单行长度限制
```text
pep8maxlinelength = 120
```

### Q & A
* pytest 4.5 出现 marker warning 的解决方案：
```text
markers =
    pep8: pep8
```

* 如何忽略特定的docstring test
`PYTEST_DONT_REWRITE`

### 参考资料
1. [Pytest 使用手册](https://learning-pytest.readthedocs.io/zh/latest/index.html)