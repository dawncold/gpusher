# gpusher

Github asynchronous mirror helper

## Setup

1. `git` user on OS with `git-shell`
2. SSH key for `git` user
3. clone Github repository

```shell
git clone --mirror git@github.com:xxx/xxx.git
```

4. install gpusher

```shell
git clone https://github.com/dawncold/gpusher.git
```

5. add `post-receive` hook for xxx.git project

```shell
#!/bin/sh

echo "Mirror to GitHub"
/path/to/gpusher/cli.sh `pwd`

exec git update-server-info
```

6. start gpusher worker

```shell
cd /path/to/gpusher
sudo -H -u git ./start.sh
```