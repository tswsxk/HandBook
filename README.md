# How to make the HB4DSAI

## Quick start
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

## Notice

The math support is not well in sphinx for markdown, so I use `pandoc` to transform `.md` file to `.rst`, the details can also be found in [Autodoc](Architecture/Autodoc.md).

To enable the math convention, all `.md` should be specified in the variable `md_include` in `conf.py`.
  