#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys


train_factor = 0.6
validate_factor = 0.2
test_factor = 0.2


if __name__ == '__main__':
    print(sys.argv)
    op = sys.argv[1]
    wd = sys.argv[2]
    if op == '1':
        pass
    clazzes = os.listdir(wd)
    for clazz in clazzes:
        clazz_dir = os.path.join(wd, clazz)
        fns = os.listdir(clazz_dir)
        train_count = int(len(fns) * train_factor)
        val_count = int(len(fns) * validate_factor)
        for i in range(len(fns)):
            fn = fns[i]
            fp = os.path.join(clazz_dir, fn)
            if op == '1' and i >= train_count:
                os.remove(fp)
            if op == '2':
                if i < train_count or i >= train_count + val_count:
                    os.remove(fp)
            if op == '3' and i <= train_count + val_count:
                os.remove(fp)
