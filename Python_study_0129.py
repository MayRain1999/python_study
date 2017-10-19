# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:Python_study_0129.py
@time:2017/10/19  18:58
"""


# 二叉树结点类型
class node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# 深度
def depth(tree):
    if tree == None:
        return 0
    left, right = depth(tree.left), depth(tree.right)
    return max(left, right) + 1


##递归实现

# 前序遍历
def pre_order(tree):
    if tree == None:
        return
    print tree.data
    pre_order(tree.left)
    pre_order(tree.right)


# 中序遍历
def mid_order(tree):
    if tree == None:
        return
    mid_order(tree.left)
    print tree.data
    mid_order(tree.right)


# 后序遍历
def post_order(tree):
    if tree == None:
        return
    post_order(tree.left)
    post_order(tree.right)
    print tree.data


# 按层次打印
def level2_order(tree):
    if tree == None:
        return
    q = []
    q.append(tree)
    results = {}
    level = 0
    current_level_num = 1
    nextlevelnum = 0
    d = []
    while q:
        current = q.pop(0)
        current_level_num -= 1
        d.append(current.data)
        if current.left != None:
            q.append(current.left)
            nextlevelnum += 1
        if current.right != None:
            q.append(current.right)
            nextlevelnum += 1
        if current_level_num == 0:
            current_level_num = nextlevelnum
            nextlevelnum = 0
            results[level] = d
            d = []
            level += 1
    print results


if __name__ == '__main__':
    tree = node('D', node('B', node('A'), node('C')), node('E', right=node('G', node('F'))))
    print'前序遍历：'
    pre_order(tree)
    print('\n')
    print('中序遍历：')
    mid_order(tree)
    print('\n')
    print '后序遍历：'
    post_order(tree)
    print('\n')
    print "层次遍历"
    level2_order(tree)

# 构建二叉树
    # class node():
    #     def __init__(self, k=None, l=None, r=None):
    #         self.key = k
    #         self.left = l
    #         self.right = r
    #
    #
    # def create(root):
    #     for a in root:
    #         if a is '#':
    #             root = None
    #         else:
    #             root = node(k=a)
    #             root.left = create(root.left)
    #             root.right = create(root.right)
    #         return root