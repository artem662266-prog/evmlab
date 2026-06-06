# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Базовый случай: если мы дошли до пустого узла (уперлись в None),
        # то отражать ничего не нужно, просто возвращаем None
        if root is None:
            return None
        
        # Шаг 1: Меняем местами левого и правого ребенка у текущего узла.
        # Используем временную переменную, чтобы не потерять ссылку.
        temporary = root.left
        root.left = root.right
        root.right = temporary
        
        # Шаг 2: Запускаем рекурсию для левого поддерева
        self.invertTree(root.left)
        
        # Шаг 3: Запускаем рекурсию для правого поддерева
        self.invertTree(root.right)
        
        # Возвращаем корень уже измененного (отраженного) дерева
        return root
