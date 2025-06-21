import random

class Node:
    """연결 리스트의 개별 노드"""
    def __init__(self, data):
        self.data = data  # 노드에 저장될 데이터
        self.next = None  # 다음 노드 참조 (초기값 None)
        self.prev = None  # 이전 노드 참조 (단순 연결 리스트이므로 사용 X, 하지만 직접 제어 가능)

class LinkedList:
    """단순 연결 리스트 구현"""
    def __init__(self):
        self.head = None  # 첫 번째 노드
        self.tail = None  # 마지막 노드 (직접 제어를 위해 추가)
        self.size = 0  # 리스트 크기

    def append(self, data):
        """리스트 끝에 데이터 추가"""
        new_node = Node(data)
        if not self.head:  # 리스트가 비어있다면
            self.head = new_node
            self.tail = new_node  # 첫 노드가 곧 마지막 노드
        else:
            self.tail.next = new_node  # 마지막 노드의 next를 새 노드로 연결
            new_node.prev = self.tail  # 새 노드의 prev를 기존 tail로 설정 (직접 제어)
            self.tail = new_node  # 새 노드를 마지막 노드로 설정
        self.size += 1

    def delete(self, data):
        """특정 값을 가진 노드를 삭제"""
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next  # 이전 노드의 next를 현재 노드의 next로 연결
                else:
                    self.head = current.next  # 삭제할 노드가 head이면 변경

                if current.next:
                    current.next.prev = current.prev  # 다음 노드의 prev를 현재 노드의 prev로 연결
                else:
                    self.tail = current.prev  # 삭제할 노드가 tail이면 변경

                self.size -= 1
                return True  # 삭제 성공
            current = current.next
        return False  # 삭제할 값이 없음

    def display(self):
        """리스트 출력 (head → tail 방향)"""
        current = self.head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        print("LinkedList:", result)

   
# 사용 예제
linked_list = LinkedList()

# 10개의 랜덤 숫자를 연결 리스트에 추가
for _ in range(10):
    linked_list.append(random.randint(1, 100))

linked_list.display()  # 리스트 출력

delete_value = linked_list.head.data  # 첫 번째 노드를 삭제해보기
linked_list.delete(delete_value)

print(f"삭제 후 ({delete_value} 제거):")
linked_list.display()
