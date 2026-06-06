class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
            
        rows = len(grid)
        cols = len(grid[0])
        islands_count = 0 
        
        # Функция для "затопления" (стирания) обнаруженного острова
        def dfs(r, c):
            # Выход за границы матрицы или если наступили на воду
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            
            # Затапливаем текущую клетку (превращаем в воду)
            grid[r][c] = '0'
            
            # Рекурсивно плывем во все 4 стороны
            dfs(r + 1, c)  # вниз
            dfs(r - 1, c)  # вверх
            dfs(r, c + 1)  # вправо
            dfs(r, c - 1)  # влево

        # Главный обход всей карты
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands_count += 1 # Нашли новый остров!
                    dfs(r, c)          # Затапливаем его целиком
                    
        return islands_count
