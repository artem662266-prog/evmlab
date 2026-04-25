class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Создаем пустой словарь для группировки
        slovar_grupp = {}
        
        for tekushchee_slovo in strs:
            # Сортируем буквы и склеиваем их обратно в строку, чтобы получить ключ
            klyuch = "".join(sorted(tekushchee_slovo))
            
            # Проверяем, есть ли уже такая группа в словаре
            if klyuch not in slovar_grupp:
                # Если группы нет, создаем для нее пустой список
                slovar_grupp[klyuch] = []
            
            # Добавляем исходное слово в список этой группы
            slovar_grupp[klyuch].append(tekushchee_slovo)
            
        # Возвращаем все списки слов, которые мы насобирали
        itogoviy_spisok = list(slovar_grupp.values())
        
        return itogoviy_spisok
