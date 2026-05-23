# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Создаем "заглушку" — пустую голову для нашего нового списка
        dummy_head = ListNode(0)
        # Указатель current поможет нам строить новый список шаг за шагом
        current = dummy_head
        
        # Переменная для хранения переноса (то, что "в уме")
        carry = 0
        
        # Цикл работает, пока есть элементы в l1 ИЛИ в l2 ИЛИ если остался перенос
        while l1 is not None or l2 is not None or carry > 0:
            
            # Получаем значение из l1 (если список не кончился, иначе 0)
            val1 = l1.val if l1 is not None else 0
            # Получаем значение из l2 (если список не кончился, иначе 0)
            val2 = l2.val if l2 is not None else 0
            
            # Считаем сумму текущих цифр и переноса из прошлого шага
            current_sum = val1 + val2 + carry
            
            carry = current_sum // 10
            # Цифра, которую мы запишем в текущий узел
            digit = current_sum % 10
            
            # Создаем новый узел с полученной цифрой и цепляем его к нашему результату
            current.next = ListNode(digit)
            # Сдвигаем указатель результата вперед
            current = current.next
            
            # Переходим к следующим узлам в исходных списках (если они еще есть)
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
                
        # dummy_head — это наша пустая заглушка (ноль). Настоящий ответ начинается со следующего узла.
        return dummy_head.next
