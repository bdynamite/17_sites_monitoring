# Sites Monitoring Utility

Check site status

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:
Download whois.exe from https://technet.microsoft.com/ru-ru/sysinternals/whois.aspx and put it in C:/Windows

To install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

# Quick Start

Example of script launch on Windows, Python 3.5:

```#!bash

$ python downloader.py
# input example

input urls file path: urls.txt

# output example

devman.org monitoring:
    http status: 200
    expiry date: 2017-08-28
meduza.io monitoring:
    http status: 200
    expiry date: 2018-07-21
arzamas.academy monitoring:
    http status: 200
    expiry date: 2017-08-24
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
