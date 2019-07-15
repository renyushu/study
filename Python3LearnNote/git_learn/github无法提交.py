"""
将本地仓库与github 关联时，发送无法推送，老是报错，原因是：本地仓库没有README.MD, 需要把远程仓库的README.MD拉到本地，然后才可以提交

git pull --rebase origin master

git push -u origin master

参考：
    https://www.jianshu.com/p/835e0a48c825


"""