# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        # Начинаем с головы списка
        current = head 
        
        # Будем идти вперед, пока не дойдем до конца (пока current не станет None)
        while current is not None:
            # Шаг 1: Временно запоминаем, кто идет СЛЕДУЮЩИМ, чтобы не потерять хвост
            next_node = current.next 
            
            # Шаг 2: Разворачиваем стрелку! Теперь текущий смотрит НАЗАД (на prev)
            current.next = prev 
            
            # Шаг 3: Двигаем наши указатели вперед для следующей итерации
            # Тот, кто был текущим, теперь становится "предыдущим"
            prev = current 
            # Переходим к следующему узлу, который мы запомнили в Шаге 1
            current = next_node 
            
        # Когда цикл закончится, current станет None, а prev окажется на бывшем последнем узле (новой голове)
        return prev
