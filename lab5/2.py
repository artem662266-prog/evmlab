# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Базовый случай: если дерева нет или мы спустились ниже листьев,
        # глубина этой ветки равна 0
        if root is None:
            return 0
        
        # Шаг 1: Рекурсивно узнаем глубину левого поддерева
        left_depth = self.maxDepth(root.left)
        
        # Шаг 2: Рекурсивно узнаем глубину правого поддерева
        right_depth = self.maxDepth(root.right)
        
        # Шаг 3: Выбираем, какая ветка оказалась длиннее, 
        # и прибавляем 1 (текущий узел)
        return max(left_depth, right_depth) + 1
