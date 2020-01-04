# linux 基本指令

## 压缩解压缩
1. gz
```shell
# 压缩
gzip $src
# 解压缩
gzip -d $file.gz
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