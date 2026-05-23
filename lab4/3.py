# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Создаем фиктивную вершину перед головой списка, чтобы застраховаться от удаления самой головы
        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy
        
        # Шаг 1: Отправляем Быстрого вперед на n шагов
        for i in range(n):
            fast = fast.next
            
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
            
        # Шаг 3: Теперь slow стоит ПЕРЕД удаляемым элементом. !
        slow.next = slow.next.next
        
        # Возвращаем измененную голову списка (она лежит сразу за dummy)
        return dummy.next
