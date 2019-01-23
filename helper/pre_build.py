#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
将体育, 星座, 政务等文件夹的数据, 组织成train.txt, validate.txt, test.txt三个文件
其数量占比为6:2:2
"""

import os
import sys


train_fn = "tram.txt"
validate_fn = "validate.txt"
test_fn = "test.txt"

train_factor = 0.6
validate_factor = 0.2
test_factor = 0.2


def read_file(file_path):
    with open(file_path, encoding="utf-8") as f:
        lines = f.readlines()
    content = "".join(lines)
    content = content.replace("\r", "")
    content = content.replace("\n", "")
    content = content.replace("\t", "")
    return content.replace("  ", " ")


def get_dco_fps(dir_fp):
    files = os.listdir(dir_fp)
    f_count = len(files)
    train_count = f_count * train_factor
    val_count = f_count * validate_factor
    # test_count = f_count * test_factor
    train_fps = []
    val_fps = []
    test_fps = []

    for i in range(f_count):
        fn = files[i]
        if i < train_count:
            train_fps.append(os.path.join(dir_fp, fn))
        elif i >= train_count and i < train_count + val_count:
            val_fps.append(os.path.join(dir_fp, fn))
        else:
            test_fps.append(os.path.join(dir_fp, fn))

    return train_fps, val_fps, test_fps


def build_files(data_dir):
    # 获取到需要构建数据的文件夹
    if not os.path.exists(data_dir):
        print("directory does not exists: ", data_dir)
        print("1")
        exit(1)

    # 更改工作目录
    os.chdir(data_dir)

    # 创建需要的文件
    if os.path.exists(train_fn):
        os.remove(train_fn)
    if os.path.exists(validate_fn):
        os.remove(validate_fn)
    if os.path.exists(test_fn):
        os.remove(test_fn)

    files = os.listdir(data_dir)
    for file in files:
        fp = os.path.abspath(file)
        basename = os.path.basename(fp)
        print("pre processing ", basename)
        if os.path.isfile(fp):
            continue
        train_fps, val_fps, test_fps = get_dco_fps(fp)
        with open(train_fn, mode='a', encoding="utf-8") as f:
            print("building train file")
            for fp in train_fps:
                text = read_file(fp)
                line = basename + "\t" + text + "\n"
                f.write(line)
        with open(validate_fn, mode='a', encoding="utf-8") as f:
            print("building val file")
            for fp in val_fps:
                text = read_file(fp)
                line = basename + "\t" + text + "\n"
                f.write(line)
        with open(test_fn, mode='a', encoding="utf-8") as f:
            print("building test file")
            for fp in test_fps:
                text = read_file(fp)
                line = basename + "\t" + text + "\n"
                f.write(line)


if __name__ == '__main__':
    wd = os.path.dirname(os.path.realpath(__file__))
    build_files(wd)

    # import codecs
    # with codecs.open("a.txt", "a", 'utf-8') as f:
    #     f.write("hello")
    # with codecs.open("a.txt", "a", 'utf-8') as f:
    #     f.write(" world")

    # s = "\r\r\n\r\n我是\n"
    # s1 = s.replace("\r", "")
    # print(s1)

    # 测试的目录
    # sys.argv[0] = 'F:\\py_ws\\text-classification-cnn-rnn\\data\\test'
    # dd = sys.argv[0]
    #
    # print(os.path.basename(dd))

    #
    # wd = os.path.dirname(os.path.realpath(__file__))
    # # print(wd)
    # build_files(wd)
    # # fp = os.path.join(data_dir, "cnn_model.py")
    # # text = read_file(fp)
    # # print(text)













