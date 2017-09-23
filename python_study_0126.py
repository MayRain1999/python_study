# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_0126.py
@time:2017/9/21  20:16
"""
# 二叉树遍历  前序遍历 \\\
class node():
    def __init__(self, k=None, l=None, r=None):
        self.key = k
        self.left = l
        self.right = r


def create(root):
    for a in root:
        if a is '#':
            root = None
        else:
            root = node(k=a)
            root.left = create(root.left)
            root.right = create(root.right)
        return root

def preorder(root):  # 前序遍历
    if root is None:
        return
    else:
        print root.key
        preorder(root.left)
        preorder(root.right)

while True:
    try:
        root1= raw_input().split(',')
        root = create(root1)
        preorder(root)

    except:
        break