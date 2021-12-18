# A notebook for using Laboratory Server
---
2021.6.6 Sunday for this line.

## Tmux usage 

### How to close tmux window
---
> tmux ls(alias tls)

is using to show all windows information. For example, 

`19: 5windows (created Sun Jun 6 16:33:48 2021)`

Then you can close this window `19` by using 

> tmux kill-window -t 19

### How to switch tmux session
---
prefix + s(Ctrl-x + s)

### Tmux add new panel, window and session
---
prefix + c(Ctrl-x + c) : add new window;

prefix + %(Ctrl-x + %) : seperate the current window to left/right panel;

prefix + "(Ctrl-x + ") : seperate the current window to up/down panel;

prefix + x(Ctrl-x + x) : kill the current window;

prefix + d(Ctrl-x + d) : deteach/exit the current tmux (if you want to recall the tmux session you have deteached 

you should type: tatt -t temp, if the session named "temp".);

refix + s(Ctrl-x + s)

### 

## How to change the shell you use

> echo $SHELL

can show the type of shell you are using. And the file `/etc/shells` 

records all the shells in your system. After download a shell(such as tcsh), 

you can change your shell by using :

> chsh -s /bin/tcsh (**chsh** [-s shell] [userid])

to replace bash with tcsh. `chsh` means "change shell", `-s` means "the new shell". 

## Latex texstudio shortcut

### making-comments shortcut

> Ctrl + t : add comments
>
> Ctrl + u : cancel comments

## Vim guideline

### Multi-lines comments in vim

(1) press `v` to come into `visual mode`

(2) press `Ctrl + v` to come into line-selection of `visual mode`

(3) press `I` to come into `insert mode`, at this time, several cursors in vertical 
direction are combined to a long and integrated cursor  

(4) the last step, is to type in the char `#` or `//`

### How to duplicate all context in a file using vim command

> ggyG

`gg` go to the top line of the context, `G` go to the bottom line of the context, `y` - yank, operate duplication.

PS: `ggdG` delete all context, `ggvG` or `ggVG` select all context. 

## Multi-lines in Jupyter

Use the mouse to select several lines, then `Ctrl + /`

## How to change ssh default port(22)

(1) First, look through the current ssh port:

> sudo `netstat` -tunlp | `grep` ssh

(2) Second, change(add new port) the default port:

> sudo vim `/etc/ssh/sshd_config`

Open the `sshd_config`, and then :

> Port 22
>
> Port 19740 # Yann-add

After adding a new port `19740`, save and exit.

The port number is better in the interval 10000~65535.

(3) Third, restart `ssh` service to make modification work:

> sudo service ssh restart

(4) Last, log in ssh remote service by using command below: 

> ssh Yann@10.102.226.188 `-p 19740`

Here is the link of original website [No.port](cnblogs.com/Cqlismy/p/11539702.html)

## Login ssh without password

Here is the link [ssh-passwd](zhuanlan.zhihu.com/p/144159642).

[Connecting to Github with SSH](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh)

## Jupyter remote service

Here is the link [Jupyter](blog.csdn.net/GouGe_CSDN/article/details/104567559).

## Git outline/usage

### Record some weird problems

No.1 ssh: connect to host github.com port 6100 failed, connection time out

Description: I want to push local modifications of git repository to remote 

repository, but when I put in the command

> git push origin main

terminal says that host github port 6100 failed, connection time out.

Solution: I look up `/etc/ssh/ssh_config`, and I find the last line of ssh_config

> Port 6100

and my ASUS Ubuntu's ssh_config file doesn't have this line, and I comment it with 

`#` and then `git push origin main`, well, it works.

No.2 the authenticity of host 'github.com(13.150.177.223)' can't be establised

Description: When I put in `git push origin main`, terminal says it.

[Solution](blog.csdn.net/tree_ifconfig/article/details/81557091): well, actually I changed my ssh keys because I realize that 

the original `id_rsa.pub` which I duplicate to my HMiao-Ian github account 

came from windows10, no private key in workplace Linux matches it. 

Then I operate `ssh-keygen -t rsa -C "XXX@XXX.com"` to reproduce a pair of keys

and duplicate `id_rsa.pub` to github account. 

### How to invite your friends to your project

(1) Make sure that your are the founder of this project, because only the founder can invite collaborators.

For example, Emiya-lin is the founder of `Sharing-between-two-PCs`

(2) Open your project, above the directory, is:

`Code` `Issues` `Pull requests` `Actions` `Projects` `Security` `Settings` `Insights` 

If you are just collaborators rather than founder of this project, `Setting` option won't appear.

(3) Click on `Settings`, then Click on `Manage access` button in the left bar, then 

you'll find a green button `invite a collaborator` in the web page, click it and put in a github username or Email to finist invitation.

## Conda guideline/usage

### list environments

> conda env list
>
> conda info --envs

## All you need to know about ssh keys

> ssh-keygen -t rsa -C "hongmiao.ian@gmail.com"

this command will produce two files in `~/.ssh` directory: 

> id_rsa (private key)
>
> id_rsa.pub (public key)

(1) I use `hongmiao.ian@gmail.com` to produce a pair of keys (old keys) at 

2021/6/19 14:01 in workplace windows10, and access `Yann` in Linux without user 

password of `Yann` by using this old keys: 

(i) copy windows10 ssh keys (old) to workplace (gongwei) 

Linux (little server in LiJia): 

> [scp](runoob.com/linux/linux-comm-scp.html) C:\User\Administrator\.ssh\id_rsa.pub Yann@10.102.226.188:/home/Yann/.ssh

(ii) In Linux, add windows10 id_rsa.pub (old) to ~/.ssh authorized_keys: 

> cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

(iii) This 3rd step is necessary, you should delete `id_rsa.pub` from windows10. 

Because you won't use it again, and if you create a pair of ssh keys (new) in 

workplace Linux, you will be confused by this old and new keys. 

(2) I use `hongmiao.ian@gmail.com` to produce a pair of keys (new keys) at 

2021/9/16 15:02 in workplace Linux.


















