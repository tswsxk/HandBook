Using `pip install` to install the [dependencies](requirements.txt).
```bash
pip install requirements.txt
```

To install the sphinx mx-theme (which is exactly the same with [d2l](http://zh.gluon.ai/))
```bash
pip install https://github.com/mli/notedown/tarball/master
cd handbook/
git submodule add https://github.com/mli/mx-theme.git
```
and then modify the following two lines in `conf.py`:
```python
html_theme_path = ['mxtheme']
html_theme = 'mxtheme'
```
[More](https://github.com/mli/mx-theme/blob/master/README.md)

Generate the handbook html
```bash
make html
```

Refer to [Autodoc](Architecture/Autodoc.md) for the information how I generate and publish the blog.
