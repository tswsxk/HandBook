# linux 基本指令

## 显示操作系统版本

## 压缩解压缩
1. gz
```shell
# 压缩
gzip $src
# 解压缩
gzip -d $file.gz
```
2. tar
```shell
# tar.gz 压缩
tar zcvf $tar $src
# tar.gz 解压缩
tar zxvf $src
```
## 显示文本特定行内容
```shell
# 打印$file中的第4行
sed -n 4p $file
# 打印file中的4-8行
sed -n 4,8p $file
```

### 参考资料 
[Linux压缩和解压常用命令](https://cloud.tencent.com/developer/article/1426584)