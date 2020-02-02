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
    logger.info(f'开始学习')
    time.sleep(3)
    app.watch()
    time.sleep(3)
    app.music()
    time.sleep(3)
    app.read()
    time.sleep(3)
    app.local()
    time.sleep(3)
    app.daily()
    time.sleep(3)
    app.weekly()
    time.sleep(3)
    app.challenge()
    time.sleep(3)
    app.zhuanxiang()
    
    app.logout_or_not()
    logger.info(f'大功告成，功成身退')
    return 0

def test():
    #app.daily()
    #app.weekly()
    app.local()
    logger.info(f'测试完毕')


def python_program():
    logger.info(f'crash ====')
    t = start()
    return t
    b = float(dsd)



if __name__ == "__main__":
    finish = 1
    while finish:
        try:
            finish = python_program()
        except:
            logger.info(f'重启执行====')
            app.return_home()
            app.view_score()
            continue
    #test()