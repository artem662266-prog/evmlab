import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # Минимально возможная скорость — 1 банан в час
        # Максимально эффективная скорость — самая большая куча
        levo = 1
        pravo = max(piles)
        
        # Сюда будем записывать подходящую скорость
        rezultat = pravo
        
        while levo <= pravo:
            # Берем среднюю скорость из нашего диапазона
            skorost = (levo + pravo) // 2
            
            # Считаем, сколько всего часов потратит Коко при такой скорости
            vsego_chasov = 0
            for kucha in piles:
                # Делим количество бананов на скорость и округляем вверх
                # Так как Коко не начинает новую кучу в тот же час
                vsego_chasov += math.ceil(kucha / skorost)
            
            # Если Коко уложилась в отведенное время h
            if vsego_chasov <= h:
                # Запоминаем скорость как возможный ответ
                rezultat = skorost
                # И пробуем еще сильнее уменьшить скорость (идем влево)
                pravo = skorost - 1
            else:
                # Если времени не хватило, значит надо есть быстрее (идем вправо)
                levo = skorost + 1
                
        return rezultat
