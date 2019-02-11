#!/usr/bin/python
# -*- coding: utf-8 -*-

import jieba
import jieba.analyse

if __name__ == '__main__':
    with open('../data/toutiao_news/1.txt', 'r', encoding='utf-8') as f:
        content = ''.join(f.readlines())
    # print(content)
    # segments = jieba.cut(content)
    # print('\r\n'.join(segments))
    content = " 新石中路西二环往东五十米路南停放的车子，应该属于智慧泊车停车位上的车。驾驶位玻璃不知是被打碎了还是一直就没关！ http://t.cn/R2WiNt8 ​新石北路"
    tags = jieba.analyse.extract_tags(content, topK=50)
    print(tags)
    # 交警王斌中路路南停放车子应该属于智慧停车位

