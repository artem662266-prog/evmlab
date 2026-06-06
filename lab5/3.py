from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Если дерево изначально пустое, возвращаем пустой список
        if root is None:
            return []
            
        result = [] # Общий список, куда будем складывать этажи
        queue = deque([root]) # Создаем очередь и сразу кладем туда корень дерева
        
        # Цикл работает, пока в очереди есть хотя бы один узел
        while queue:
            # Фиксируем, сколько узлов сейчас находится на текущем уровне (этаже)
            level_size = len(queue)
            current_level_values = [] # Список для значений только этого этажа
            
            # Обрабатываем ровно то количество узлов, сколько на этом этаже
            for _ in range(level_size):
                # Достаем узел с левого конца очереди
                node = queue.popleft()
                
                # Добавляем его значение в список текущего уровня
                current_level_values.append(node.val)
                
                # Если у узла есть левый ребенок, добавляем его в очередь (на следующий этаж)
                if node.left is not None:
                    queue.append(node.left)
                    
                # Если есть правый ребенок, тоже добавляем его в очередь
                if node.right is not None:
                    queue.append(node.right)
            
            # Когда весь этаж обработан, добавляем его список в общий результат
            result.append(current_level_values)
            
        return result
