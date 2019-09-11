
Dependency
```
sphinx
nbsphinx
sphinx_rtd_theme
recommonmark
m2r
```
Using `pip install` to install the dependencies.


To install the sphinx mx-theme
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
