from Note import Note
import numpy as np

class Linked:
    def __init__(self):

        self.head = None

    def insertAtBegin(self, data, duration):
        new_node = Note(data, duration)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtEnd(self, data, duration):
        new_node = Note(data, duration)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def insert_silence(self, duration):

        new_node = Note.rest(duration)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node



    def tocar(self):

        curr = self.head
        while curr:
            curr.play()
            curr = curr.next

    def imprimirNotas(self):
        curr = self.head
        while curr:
            try:
                print(curr.note)
                curr = curr.next
            except:

                print('silencio')
                curr = curr.next



linked = Linked()
linked.insertAtEnd('F4',0.5)
linked.insertAtEnd('g4',0.5)
linked.insertAtEnd('F4',0.5)
linked.insertAtEnd('Bb4',0.5)
linked.insertAtEnd('a4', 1)
linked.insertAtEnd('F4',0.5)
linked.insertAtEnd('g4',0.5)
linked.insertAtEnd('F4',0.5)
linked.insertAtEnd('C5',0.5)
linked.insertAtEnd('Bb4',1)
linked.tocar()
linked.imprimirNotas()



