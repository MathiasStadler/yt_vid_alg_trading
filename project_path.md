
# setup 

## date

```bash
date - Thu Oct 17 03:25:28 PM CEST 2024
```

## base system

```bash
uname -a
Linux debian 6.1.0-26-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.1.112-1 (2024-09-30) x86_64 GNU/Linux
```

## install python

```bash
sudo apt update
sudo apt upgrade
sudo apt autoclean
```

## test / install python

```bash
python3 --version
> Python 3.11.2

[install python](https://reintech.io/blog/install-python3-pip-debian-12)

pip3 --version
> pip 24.2 from /home/trapapa/workspace_python/yt_vid_alg_trading/.venv/lib/python3.11/site-packages/pip (python 3.11)

[install venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html)

```

## [download](https://interactivebrokers.github.io/#) and install ibkr api

```bash
```

## create and init venv
## TODO HOW DEAS WORK'S

```bash
# into env
source .venv/bin/activate
#leave env
deactivate

```

## 
[Interactive Brokers Python API (Native) – A Step-by-step Guide](https://www.interactivebrokers.com/campus/ibkr-quant-news/interactive-brokers-python-api-native-a-step-by-step-guide/)


## [setupibkr](https://www.interactivebrokers.com/campus/trading-lessons/accessing-the-tws-python-api-source-code/) 

```bash
python setup.py install
python3 IBJts/source/pythonclient/setup.py install

```

## start first sample python program INSIDE .venv

```bash

python3 IBJts/samples/Python/Testbed/Program.py

```


pip3 install ibapi
