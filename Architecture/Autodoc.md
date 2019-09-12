# 自动文档


## sphinx

`sphinx` 无法支持 `markdown` native 数学公式 $X^2 + Y^2 = 1$ 的显示，可以通过 [pandoc](https://pandoc.org/) 将markdown转换为 `.rst`文件

```bash
pandoc xxx.md -t rst > xxx.rst
```

## Read The Docs

[创建、托管和浏览文档](https://readthedocs.org/)

the example configuration file [.readthedocs.yml](https://github.com/readthedocs/readthedocs.org/blob/master/readthedocs/rtd_tests/fixtures/spec/v2/schema.yml) and the [explanation](https://docs.readthedocs.io/en/stable/config-file/v2.html#supported-settings)
