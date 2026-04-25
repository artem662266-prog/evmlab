class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Превращаем список во множество для мгновенного поиска чисел
        chisla_set = set(nums)
        
        # Переменная для хранения длины самой длинной цепочки
        maks_dlina = 0
        
        for chislo in chisla_set:
            # Проверяем, является ли текущее число началом цепочки.
            # Если в множестве нет числа на единицу меньше (chislo - 1), значит это старт!
            if (chislo - 1) not in chisla_set:
                tekushchee_chislo = chislo
                tekushchaya_dlina = 1
                
                # Пока следующее число (+1) есть в множестве, увеличиваем длину цепочки
                while (tekushchee_chislo + 1) in chisla_set:
                    tekushchee_chislo += 1
                    tekushchaya_dlina += 1
                
                # Обновляем наш рекорд, если текущая цепочка оказалась длиннее
                if tekushchaya_dlina > maks_dlina:
                    maks_dlina = tekushchaya_dlina
                    
        return maks_dlina
