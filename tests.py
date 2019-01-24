#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

import os
import numpy as np


# base_dir = 'data/cnews'
# train_dir = os.path.join(base_dir, 'cnews.train.txt')
# test_dir = os.path.join(base_dir, 'cnews.test.txt')
# val_dir = os.path.join(base_dir, 'cnews.val.txt')

base_dir = 'data/cnews_dir'
train_dir = os.path.join(base_dir, 'train')
test_dir = os.path.join(base_dir, 'test')
val_dir = os.path.join(base_dir, 'val')

vocab_dir = os.path.join(base_dir, 'cnews.vocab.txt')

save_dir = 'checkpoints/textcnn'
save_path = os.path.join(save_dir, 'best_validation')  # 最佳验证结果保存路径


if __name__ == '__main__':
    x = np.array(['one', 'two', 'three', 'four'])
    y = np.array([1, 2, 3, 4])
    indices = np.random.permutation(len(x))
    shuffle_x = x[indices]
    shuffle_y = y[indices]
    print(shuffle_x)
    # fps = []
    # labels = []
    # clazzes = os.listdir(train_dir)
    # for clazz in clazzes:
    #     clazz_dir_path = os.path.join(train_dir, clazz)
    #     fns = os.listdir(clazz_dir_path)
    #     for fn in fns:
    #         fp = os.path.abspath(os.path.join(train_dir, clazz, fn))
    #         fps.append(fp)
    #         labels.append(clazz)
    # print(fps)

