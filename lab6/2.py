"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Optional[Node]') -> 'Optional[Node]':
        # Если граф пустой, то и клонировать нечего
        if not node:
            return None
            
        # Словарь-переводчик для связи: {оригинальный_узел: его_клон}
        old_to_new = {}
        
        # Наша рекурсивная функция для обхода графа
        def dfs(current_node):
            # Если мы этот узел уже клонировали раньше, 
            # просто возвращаем его готовую копию из словаря
            if current_node in old_to_new:
                return old_to_new[current_node]
                
            # Если узел новый, создаем его точную копию (пока без соседей)
            copy = Node(current_node.val)
            # Сразу же записываем в словарь, что у этого узла появился клон
            old_to_new[current_node] = copy
            
            # Теперь проходимся по всем соседям оригинального узла
            for neighbor in current_node.neighbors:
                # Рекурсивно клонируем соседа и добавляем его клон в список соседей нашей копии
                copy.neighbors.append(dfs(neighbor))
                
            # Возвращаем полностью собранный клон узла
            return copy
            
        # Запускаем процесс с самого первого узла графа
        return dfs(node)
