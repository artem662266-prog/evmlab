class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Создаем словарь для подсчета: число будет ключом, а его количество — значением
        vstrechi = {}
        
        # Проходим по всем числам в массиве
        for chislo in nums:
            # Если число уже есть в словаре, увеличиваем счетчик
            if chislo in vstrechi:
                vstrechi[chislo] += 1
            # Если числа еще нет, записываем его с единицей
            else:
                vstrechi[chislo] = 1
        
        # Получаем список уникальных чисел из ключей словаря
        unikalnye_chisla = list(vstrechi.keys())
        
        # Сортируем этот список. 
        # key=vstrechi.get говорит сортировке смотреть на количество повторений в словаре
        # reverse=True ставит самые частые числа в начало
        unikalnye_chisla.sort(key=vstrechi.get, reverse=True)
        
        # Отрезаем первые k элементов из отсортированного списка, чтобы самые частые показало
        rezultat = unikalnye_chisla[:k]
        
        return rezultat
