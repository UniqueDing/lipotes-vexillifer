# git 使用笔记

## 版本回退

回退历史版本  
`git reset --hard (commit-id)`  
查看历史版本  
`git reflog`  

## 撒销修改  

从版本库恢复到暂存区  
`git reset HEAD (file)`  
从暂存区恢复到工作区  
`git checkout -- (file)`  

## 添加到远程库

关联  
`git remote add origin (repository ssh)`  

## 标签

添加标签  
`git tag (tag-name) [commit-id]`  
显示信息  
`git show (tag-name)`  
标签信息  
`git tag -a (tag-name) -m "(info)"`  
删除  
`git tag -d (tag-name)`  
推送  
`git push origin (tag-name)`  
全部推送  
`git push origin --tags`  
远程删除  
`git tag -d (tag-name)`  
`git push origin :refs/tags/(tag-name)`  

## 分支

创建分支  
`git branch (branch-name)`  
切换  
`git checkout (branch-name) | git switch (branch-name)`  
创建+切换  
`git checkout -b (branch-name) | git switch -c (branch-name)`  
合并  
`git merge (branch-name)`  
普通模式合并（可以看见历史分支）  
`git merge --no-ff -m "(info)" (branch-name)`  
删除  
`git branch -D (branch-name)`  
查看远程库信息  
`git remote -v`  
对应本地和远程分支  
`git checkout -b (branch-name) (origin/branch-name)`  
关联本地和远程分支  
`git branch --set-upstream (branch-name) (origin/branch-name)`  

## Stash

储藏  
`git stash`  
恢复  
`git stash apply [@{stash-number}]` 不删除stach  
`git stash pop`  
删除  
`git stash drop`  
列出  
`git stash list`  
合并到其它分支  
`git cherry-pick (commit-id)`  

## Rebase

整理分叉到一条直线  
`git rebase`  
查看log  
`git log --grph --pretty-oneline --abbrev-commit`  

## 参考文献

[https://www.liaoxuefeng.com/wiki/896043488029600][1]

[1]: https://www.liaoxuefeng.com/wiki/896043488029600
