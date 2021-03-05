# Github 笔记

## 一. Github 操作记录

 + 清空暂存区

   git rm --cached *

## 二. Git push时遇到的BUG

 1. OpenSSL SSL_read: Connection was reset, errno 10054

```
git config --global http.sslVerify "false"
```

 2. 开梯子后443

```
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy http://127.0.0.1:7890
```

设置为Clash的端口,避免443

git config --global --unset http.proxy

git config --global --unset https.proxy