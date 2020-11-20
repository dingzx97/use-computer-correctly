# 如何做一个安静的github仓库管理者

## 第一步：新建一个仓库

直接去github点击新建仓库就好，自己起个名字即可。

下面是新建完之后官方说的步骤，果然官方的还是写的简单明了

### …or create a new repository on the command line

```bash
echo "# use-computer-correctly" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:dingzx97/use-computer-correctly.git
git push -u origin main
```

### …or push an existing repository from the command line

```bash
git remote add origin git@github.com:dingzx97/use-computer-correctly.git
git branch -M main
git push -u origin main
```

### …or import code from another repository

You can initialize this repository with code from a Subversion, Mercurial, or TFS project.

`Import code`

## 第二步：？？？

我也不知道接下来该怎么做，慢慢摸索了。