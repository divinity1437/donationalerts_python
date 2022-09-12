# Donationalerts python automatic tool
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

Donationalerts python is a tool for getting in 24/7 way about new donations, subs and other alerts from <a href="https://www.donationalerts.com/">Donationalerts</a> 

# Setup
knowledge of linux, python will certainly help, but are by nomeans required.

this guide will be targetted towards ubuntu - other distros may have slightly different setup processes.

## download the codebase onto your machine
```sh
# clone repository
git clone https://github.com/divinity1437/donationalerts_python

# enter directory
cd donationalerts_python

# install dependencies
python -m pip install -r requirements.txt
```

## configuring .env file
all configuration can be done from the
`.env` file. we provide an example `.env.example` file which you can use as a base.
```sh
# create a configuration file from the sample provided
cp .env.example .env

# open the configuration file for editing
nano .env
```

## congratulations! you just end with setup! 
if everything went well, you should be able to start your server up:

```sh
# start the server
python main.py
```

Everything is under GPL license. Free-to-use tool.
