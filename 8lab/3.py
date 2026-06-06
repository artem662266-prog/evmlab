class Solution:
    # Имя функции строго "combinationSum", как требует система
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []       # Сюда складываем готовые списки
        current_comb = [] # Наш рабочий буфер
        
        # Рекурсивный бэктрекинг
        # i — индекс числа, current_target — сколько ещё осталось набрать
        def backtrack(i, current_target):
            # Базовый случай 1: Успех, набрали ровно target
            if current_target == 0:
                result.append(current_comb[:]) # Добавляем копию
                return
                
            # Базовый случай 2: Перебор по сумме или вышли за границы массива
            if current_target < 0 or i >= len(candidates):
                return
                
            # Вариант 1: Берем текущее число в комбинацию
            current_comb.append(candidates[i])
            # Индекс 'i' не меняем, так как это же число можно взять еще раз
            backtrack(i, current_target - candidates[i])
            
            # Бэктрекинг (откат назад)
            current_comb.pop() 
            
            # Вариант 2: Игнорируем текущее число и идем дальше к следующему
            backtrack(i + 1, current_target)

        # Запуск алгоритма с 0-го элемента
        backtrack(0, target)
        return result
