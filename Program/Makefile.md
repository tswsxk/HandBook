# Makefile 基础

## FAQ

* Missing separator
```text
Makefile:xx: *** missing separator.  Stop.
```

可能的原因：命令开头应使用`\t`的地方却使用了空格

* Error 127
```text
make: execvp: xxx: Permission denied
make: *** [install] Error 127
```

可能的原因：
1. 命令不存在,可能是因为命令引用忘记加 `$`, 例如本想使用的是 `$(CC)`，却写成 `CC`


## 参考资料
1. [makefile介绍](https://seisman.github.io/how-to-write-makefile/introduction.html)