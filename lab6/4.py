class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
            
        rows = len(heights)
        cols = len(heights[0])
        
        # Множества для хранения клеток, до которых может дойти вода ИЗ конкретного океана
        pacific_cells = set()
        atlantic_cells = set()
        
        # Функция DFS для подъема "вверх" по склонам
        # prev_height — высота клетки, с которой мы только что пришли
        def dfs(r, c, visited, prev_height):
            # Условия выхода:
            # 1. Вышли за границы матрицы
            # 2. Клетка уже посещена этим океаном
            # 3. Высота текущей клетки МЕНЬШЕ, чем у предыдущей (вода снизу вверх течь не может)
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
                (r, c) in visited or heights[r][c] < prev_height):
                return
                
            # Отмечаем клетку как достижимую для текущего океана
            visited.add((r, c))
            
            # Идем во все 4 стороны, передавая высоту текущей клетки как ориентир
            dfs(r + 1, c, visited, heights[r][c]) # вниз
            dfs(r - 1, c, visited, heights[r][c]) # вверх
            dfs(r, c + 1, visited, heights[r][c]) # вправо
            dfs(r, c - 1, visited, heights[r][c]) # влево

        # Шаг 1: Запускаем DFS для левой и правой границ (столбцы)
        for r in range(rows):
            # Левая граница — Тихий океан (высота для старта берется из самой клетки)
            dfs(r, 0, pacific_cells, heights[r][0])
            # Правая граница — Атлантический океан
            dfs(r, cols - 1, atlantic_cells, heights[r][cols - 1])
            
        # Шаг 2: Запускаем DFS для верхней и нижней границ (строки)
        for c in range(cols):
            # Верхняя граница — Тихий океан
            dfs(0, c, pacific_cells, heights[0][c])
            # Нижняя граница — Атлантический океан
            dfs(rows - 1, c, atlantic_cells, heights[rows - 1][c])
            
        # Шаг 3: Находим общие клетки для обоих множеств
        # Оператор & находит пересечение множеств (то, что есть и там, и там)
        result = []
        for cell in pacific_cells & atlantic_cells:
            result.append([cell[0], cell[1]])
            
        return result
