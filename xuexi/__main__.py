#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@project: AutoXue
@file: __main__.py
@author: kessil
@contact: https://github.com/kessil/AutoXue/
@time: 2019-10-26(星期六) 10:22
@Copyright © 2019. All rights reserved.
'''
from argparse import ArgumentParser
import time
from . import App
from .unit import logger
from .secureRandom import SecureRandom as random

parse = ArgumentParser(description="Accept username and password if necessary!")

parse.add_argument("-u", "--username", metavar="username", type=str, default='', help='User Name')
parse.add_argument("-p", "--password", metavar="password", type=str, default='', help='Pass Word')
args = parse.parse_args()
app = App(args.username, args.password)

def shuffle(funcs):
    random.shuffle(funcs)
    for func in funcs:
        func()
        time.sleep(5)

def start():
    logger.debug(f'开始学习')
    app.watch()
    time.sleep(5)
    app.music()
    time.sleep(5)
    app.read()
    time.sleep(5)
    app.challenge()
    time.sleep(5)
    app.daily()
    time.sleep(5)
    app.weekly()
    time.sleep(5)
    app.zhuanxiang()
    time.sleep(5)
    app.logout_or_not()
    
    logger.info(f'大功告成，功成身退')

def test():
    #app.daily()
    app.weekly()
    logger.info(f'测试完毕')

if __name__ == "__main__":
    start()
    #test()