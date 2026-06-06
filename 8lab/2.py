class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []             # Список для хранения всех готовых перестановок
        current_permutation = [] # Наш рабочий буфер для текущей перестановки
        
        # Рекурсивная функция бэктрекинга
        def backtrack():
            # Базовый случай: если длина текущей перестановки сравнялась с длиной nums,
            # значит мы задействовали все числа. Перестановка готова!
            if len(current_permutation) == len(nums):
                # Добавляем в результат копию [:] буфера
                result.append(current_permutation[:])
                return
            
            # Перебираем все доступные числа из оригинального массива
            for num in nums:
                # Если число еще не было добавлено в текущую перестановку
                if num not in current_permutation:
                    # 1. Шаг вперед: добавляем число в буфер
                    current_permutation.append(num)
                    
                    # 2. Рекурсивный запуск для поиска следующих чисел
                    backtrack()
                    
                    # 3. Бэктрекинг (Шаг назад): убираем число из буфера,
                    # чтобы на его место в цикле могло встать другое число
                    current_permutation.pop()
                    
        # Запускаем алгоритм
        backtrack()
        return result
