# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # Напишем вспомогательную функцию, которая проверяет узел в рамках дозволенного коридора
        def validate(node, low_boundary, high_boundary):
            # Пустой узел (конец ветки) не нарушает правил BST, возвращаем True
            if node is None:
                return True
            
            # Если значение текущего узла вышло за рамки (меньше минимума или больше максимума)
            if node.val <= low_boundary or node.val >= high_boundary:
                return False
            
            # Рекурсивно проверяем детей:
            # 1. Для левого ребенка: верхняя граница становится равной значению текущего узла
            left_is_valid = validate(node.left, low_boundary, node.val)
            
            # 2. Для правого ребенка: нижняя граница становится равной значению текущего узла
            right_is_valid = validate(node.right, node.val, high_boundary)
            
            # Дерево валидно, только если и левое, и правое поддеревья верны
            return left_is_valid and right_is_valid

        # Изначально для корня ограничений нет, передаем минус и плюс бесконечность
        return validate(root, float('-inf'), float('inf'))
