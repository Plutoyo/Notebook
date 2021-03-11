# Github 笔记

## 一. 清空暂存区

   git rm --cached *

   删除缓冲区中的文件

   1.  git rm --cached "文件路径"，不删除物理文件，仅将该文件从缓存中删除；
   2.  git rm --f "文件路径"，不仅将该文件从缓存中删除，还会将物理文件删除（不会回收到垃圾桶）；

​    

   　　如果一个文件已经add到暂存区，还没有 commit，此时如果不想要这个文件了，有两种方法：

   1. 用版本库内容清空暂存区，git reset HEAD 回退到当前版本（在Git中，用HEAD表示当前版本，上一个版本就是HEAD^，上上一个版本就是HEAD^^，当然往上100个版本写100个^比较容易数不过来，所以写成HEAD~100）；

   2. 只把特定文件从暂存区删除，git rm --cached xxx；

## 二. Git push时遇到的BUG

 2. OpenSSL SSL_read: Connection was reset, errno 10054

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

## 三. Git 合并操作

​	1.git branch xxx

​		建立一个分支

​	2.git checkout xxx

​		切换到xxx分支

​	3.修改后切回到主分支

​		git checkout master

​	4.使用使用git diff修改矛盾的地方

​	5.git merge xxx

## 四.重新commit

如果提交完发现有个别文件没有提交上去,那么使用先git add 漏掉的文件,再次提交git commit --amend

## 五.取消已经add暂存区的文件

使用git reset HEAD <file>来取消暂存

## 六.添加远程仓库

1. 对于已经在本地建立好的使用

```
git remote add <shortname> <url>
```

2. 对于新项目或者服务器已经有的项目使用 git clone <url>

3. 推送 使用 git push <remote> <branch>

   remote表示推送的目标,branch表示推送的分支

4. 删除推送目标 git remote remove <name>,如果使用clone 少用,默认就好