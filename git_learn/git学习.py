
# git learn
# git是目前世界上最先进的分布式版本控制系统
# 工作原理
#    remote -- pull --> workspace
#           -- fetch/clone --> repository -- checkout --> workspace
#
#    workspace -- add --> index -- commit--> repository -- push --> remote

#

"""

在github上创建仓库之后，可以从这个仓库克隆出新的仓库，也可以把一个已有的本地仓库与之关联
    1，克隆新的仓库
    2，关联本地仓库
        关联本地仓库命令：git remote add origin git@github.com:renyushu/study.git
            origin: 远程库的默认名字
        推送本地内容到远程库：
             git push -u origin master tip: 第一次推送需要加参数 -u, 否则 git push origin master就可以


# 撤销修改
    git checkout -- filename.txt

# 删除文件
    git mv

# 本地版本回退
    git log --pretty=oneline : 查看提交日志
    git reset --hard commit_id : 回退到特定版本

# 远程仓库版本回退：
    1，先本地回退
    2，在强制推送远程仓库：git push -f origin master


# 删除本地文件夹
    git rm out build -r -f // 删除本地out和build文件夹
    git commit -am "删除out和build文件夹" // 添加备注
    git push origin master // 提交至服务端




"""
