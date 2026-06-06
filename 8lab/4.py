class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        # Рекурсивная функция бэктрекинга
        # r, c — текущие координаты на доске
        # k — индекс буквы в слове word, которую мы сейчас ищем
        def backtrack(r, c, k):
            # Базовый случай 1: Если мы нашли все буквы, значит слово собрано!
            if k == len(word):
                return True
                
            # Базовый случай 2: Выход за границы, или буква не совпадает, 
            # или мы наступили на уже посещенную клетку (где стоит '#')
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
                board[r][c] != word[k]):
                return False
                
            # Шаг вперед: Сохраняем букву и "стираем" её с доски, чтобы не использовать дважды
            temp = board[r][c]
            board[r][c] = '#'
            
            # Проверяем все 4 направления для следующей буквы (k + 1)
            # Если хотя бы одно направление вернет True, то и всё слово найдено
            found = (backtrack(r + 1, c, k + 1) or # вниз
                     backtrack(r - 1, c, k + 1) or # вверх
                     backtrack(r, c + 1, k + 1) or # вправо
                     backtrack(r, c - 1, k + 1))   # влево
                     
            # БЭКТРЕКИНГ (Шаг назад): Восстанавливаем оригинальную букву на доске
            board[r][c] = temp
            
            return found

        # Главный цикл: ищем стартовую точку (первую букву слова)
        for r in range(rows):
            for c in range(cols):
                # Если первая буква совпала, запускаем отсюда бэктрекинг
                if board[r][c] == word[0]:
                    if backtrack(r, c, 0):
                        return True # Если слово нашлось, сразу выходим
                        
        return False
