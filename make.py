# coding: utf-8
# 2019/9/12 @ tongshiwei
import os
from pathlib import Path
import logging

root = os.path.abspath(os.path.dirname(__file__))

clean_dir = set(os.listdir(root)) - {'.git', '.gitignore', '_build', '_static', 'mx-theme'}

clean_dir = [os.path.join(root, d) for d in clean_dir]

rst_exclude = [

]

md_include = [
    "Overview/overview.md",
]

logging.getLogger().setLevel(logging.INFO)


def clean_rst():
    logging.info("clean .rst")
    _rst_exclude = set(rst_exclude)
    for _clean_dir in clean_dir:
        for _root, dirs, files in os.walk(_clean_dir):
            for fn in files:
                if '.rst' in fn:
                    filename = os.path.join(_root, fn)
                    if filename in rst_exclude:
                        continue
                    logging.info("remove %s" % filename)
                    os.remove(filename)


def generate_rst():
    logging.info("converting .md with math expression to .rst")
    _md_include = set([str(Path(os.path.join(root, fn))) for fn in md_include])
    for _clean_dir in clean_dir:
        for _root, dirs, files in os.walk(_clean_dir):
            for fn in files:
                if '.md' in fn:
                    src = Path(os.path.join(_clean_dir, fn))
                    if str(src) not in _md_include:
                        continue
                    tar = src.with_suffix(".rst")
                    logging.info("%s -> %s" % (src, tar))
                    os.system("pandoc %s -t rst > %s" % (src, tar))


logging.info("#" * 30)
clean_rst()
generate_rst()
logging.info("#" * 30)
