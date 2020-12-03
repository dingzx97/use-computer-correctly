# 如何做一个安静的github仓库管理者

## 第一步：环境配置

### 安装与配置git

去[git官网](https://git-scm.com/)下载安装包，或者是直接下载[github桌面版](https://desktop.github.com/)使用（github desktop修改不了安装路径）。

一般不用配置git，安装完后鼠标右键就有`Git Bash Here`这个选项，直接选这个就在当前目录下打开命令行了。

### git配置与github的ssh连接

> 使用github desktop登录下就好，可跳过。

github官网[教程](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/connecting-to-github-with-ssh)。

1. 创建公钥和私钥，命令行输入`ssh-keygen -t rsa -b 4096 -C "your_email@example.com"`，建议不要去修改密钥的保存位置，默认是放在~/.ssh/目录下；

   - -t 是加密算法，有 [dsa | ecdsa | ecdsa-sk | ed25519 | ed25519-sk | rsa]算法
   - -b 是密钥对长度
   - -C 是注释
   - -f 是文件名

2. 将密钥添加到ssh-agent中，输入`eval $(ssh-agent -s)`启动ssh-agent服务，`ssh-add ~/.ssh/id_rsa`将密钥添加到 ssh-agent服务中；

3. 在github中添加公钥，将`id_rsa.pub`文件的内容复制下来，去账户的[设置页](https://github.com/settings/keys)添加一个新的ssh key，把公钥的内容复制进去；

4. 测试连接，命令行输入`ssh -T git@github.com`运行，确认连接，如果出现以下信息表示连接成功。

   ```
   Hi username! You've successfully authenticated, but GitHub does not provide shell access.
   ```

## 第二步：新建一个本地仓库

> 使用github desktop就直接点新建仓库就好。

1. 新建一个文件夹；
2. 命令行进到这个文件夹里，输入`git init`初始化即可，会生成一个.git的隐藏文件夹；

## 第三步：分支管理

在创建完仓库后，会有默认的`main`或`master`分支，没有使用分支的需要就不用再创建了，直接跳过这块。

- 列出分支：`git branch`
- 创建分支：`git branch (branchname)`
- 切换分支：`git checkout (branchname)`
- 合并分支：`git merge (branchname)`  将(branchname)分支合并到当前分支
- 删除分支：`git branch -d (branchname)`

## 第四步：添加说明文件与开源许可证

> 使用github desktop创建仓库时就可以选择自动创建一个README.md文件和许可证。

在仓库的文件夹中添加文件，比如代码或者是其他的东西，这里可以先添加一个`README.md`文件，用于说明这个仓库是做什么的。

直接在仓库的根目录下创建`README.md`文件，然后写写字。

创建好了项目，还需要思考用一个什么样的开源许可证，这个[网站](https://choosealicense.com)可以帮助我们选择。创建一个`LICENSE`文件，将选好的许可证内容粘贴进去就好。

我的这个项目用的是MIT许可证，毕竟是第一个项目，也只是些教程类的东西，就随便选择了个简单的许可证就好。

## 第五步：暂存修改与提交

> 在github desktop界面会显示出所有修改过的文件，写好概要点提交就好。

在对仓库里的文件进行修改之后，使用`git add`命令将修改保存到暂存区中。例如，新建了`README.md`文件后，命令行输入`git add README.md`将保存文件的修改。如果有多个文件进行了修改，可以直接输入`git add .`命令，会自动找到所有修改的文件。

命令行输入`git commit`提交修改，需要写一个概要说明下这次提交，或者是带参数输入`git commit -m "first commit"`来写概要。

## 第六步：上传代码至远程仓库中

> github desktop直接点击Publish repository即可。

1. 在github中或者是其他的仓库网站中创建一个新的仓库；

2. 在`git remote`中添加远程仓库地址，输入:

   ```bash
   git remote add origin git@github.com:username/repo_name.git
   ```
	- `origin`是仓库地址的别名，起其他的名字也是可以；
	- `username/repo_name`是用户名和仓库名称。
	
3. 使用`git push <remote_name> <local_branch>:<remote_branch> `上传代码，输入`git push -u origin master:master`将本地仓库的master分支上传至远程仓库的master分支，两个分支名字相同的话可以简写成`git push -u origin master`，如果主分支是叫main的话就把master改成main。

   - -u 指定`origin`为默认主机，后面就可以不加任何参数使用`git push`了。

## 第七步：查看远程仓库

直接去仓库看看代码有没有传上去就好。



## 撤销Commit

有时候，自己的强迫症换了，commit后又进行了文件内容的更改，正常来说，再进行一次commit就好了，但是这样就有两次commit了，有强迫症的我觉得明明一次commit就好，为什么搞两次，就想着弄一个commit就好，这个时候就需要用到`git reset`修改HEAD到指定的状态。

1. 输入`git log`查看日志；

```
commit de16b924d2c9c8850670dc45995cb7a107c3a6ff (HEAD -> master,origin/master)

    b

commit 587feb29610f5a08c59cbef130c1e4df05707998

    a
```

2. 假设a是以前提交的，b是刚刚提交的，现在我又进行了修改，但是不想再次提交，想着把b删了，之后把b提交时的修改和我现在修改弄成一个commit。
3. 输入`git reset 587feb29610f5a08c59cbef130c1e4df05707998`，将HEAD移动到之前提交的a处，在输入`git log`查看日志；

```
commit 587feb29610f5a08c59cbef130c1e4df05707998 (HEAD -> master)

    a
```

4. HEAD就移动到之前提交的a处，此时再进行`git add .`和`git commit -m "c"`,再输入`git log`查看日志；

```
commit 02684f204122a8fce7cbd9c8bc95c5f59ef253fa (HEAD -> master)

    c

commit 587feb29610f5a08c59cbef130c1e4df05707998

    a
```

5. 提交的b没有了，只有一次新的提交c在了，此时就能进行`git push`了。如果在提交了b之后马上进行了push操作，现在删了b弄成一个c去push时就会出问题，会报一下错误：

```
error: failed to push some refs to <url>
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

6. 出现这个问题主要是因为远程仓库里面有了提交b，但是本地仓库没有这个提交，就不一致，提示需要先进行同步。但是我们并不想要b的那次提交，因此我们就需要强制提交本地的长裤，输入`git push -f origin master`，加一个`-f`就是强制更新。

