# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Если список пустой или в нем всего 1-2 элемента, ничего делать не нужно
        if not head or not head.next or not head.next.next:
            return

        # --- ШАГ 1: Находим середину списка с помощью двух указателей ---
        # "Медленный" шагает по одному разу, "Быстрый" — по два.
        # Когда быстрый дойдет до конца, медленный будет ровно посередине.
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        # Теперь slow — это начало второй половины списка. 
        # Откусим вторую половину от первой, запомнив её старт
        second_half = slow.next
        slow.next = None  # Отрезаем первую половину от второй
        
        prev = None
        current = second_half
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
        # Теперь в переменной prev лежит голова развернутой второй половины
        first_half = head
        second_half = prev  # Переименуем для понятности
        
        while second_half is not None:
            # Запоминаем следующие шаги для обеих половин, чтобы не потерять их
            next_first = first_half.next
            next_second = second_half.next
            
            # Соединяем элемент первой половины с элементом второй половины
            first_half.next = second_half
            # Соединяем элемент второй половины со СЛЕДУЮЩИМ элементом первой половины
            second_half.next = next_first
            
            # Двигаем указатели вперед, к сохраненным вершинам
            first_half = next_first
            second_half = next_second
