# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.x = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Запускаем простой цикл. Будем спускаться по дереву, пока не найдем ответ.
        current = root
        
        while current is not None:
            # Если оба узла больше текущего, значит общий предок находится где-то СВЕРХУ-СПРАВА
            if p.val > current.val and q.val > current.val:
                current = current.right # Спускаемся в правое поддерево
                
            # Если оба узла меньше текущего, значит общий предок находится где-то СВЕРХУ-СЛЕВА
            elif p.val < current.val and q.val < current.val:
                current = current.left # Спускаемся в левое поддерево
                
            # Если один узел слева, а другой справа (или мы стоим на одном из них),
            # значит текущий узел — это и есть точка разделения, то есть наш LCA!
            else:
                return current
