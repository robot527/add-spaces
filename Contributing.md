贡献
================================================================================

如果你想要给 [add-spaces](https://github.com/robot527/add-spaces) 做贡献，请按以下步骤进行：

1. 点击 [fork](https://github.com/login?return_to=%2Frobot527%2Fadd-spaces) 按钮。

2. 通过如下命令从你的 GitHub 帐号 `clone` 这个库： 

    ```
    git clone git@github.com:your_github_username/add-spaces.git
    ```

3. 通过如下命令设置上游仓库 (`upstream`) :

    ```
    git remote add upstream https://github.com/robot527/add-spaces.git
    ```

4. 对本地库进行修改。

5. 备份本地修改，**每次提交**之前先用下面的命令同步上游仓库的更新：

    ```
    git fetch upstream
    git checkout master
    git rebase upstream/master
    ```

6. 加入自己的修改并提交，然后推送 (`push`) 到远程仓库。

    ```
    git add your_changed_files
	git commit -m "change log"
    git push -u origin
    ```

7. 点击 `New pull request` 按钮，将 your_github_username 的 `add-spaces` 库的 master 分支的修改提交到 robot527 的 `add-spaces` 库中。

谢谢！
