class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#reversing a linked list

def Reverse(head):
    curr=head
    prev=None
    while curr!=None:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    return prev

#check if the list a palindrome or not

def palindrome(head):
    val=[]
    curr=head
    while curr!=None:
        val.append(curr.data)
        curr=curr.next
    if val==val[::-1]:
        return True
    else:
        return False

#searching for an element in a linked list

def Search(head,key):
    curr=head
    while curr!=None:
        if curr.data==key:
            return True
        curr=curr.next
    return False    




n = int(input())
ll = list(map(int , input().split()))
key = int(input())
head = None
tail = None
for i in range(n):
    node = Node(ll[i])
    if head is None:
        head = node
        tail = node
    else:
        tail.next = node
        tail = node    


print(f" Status of Element which was searched :{Search(head,key)"})
print(f" Is it palindrome ? {palindrome(head)}")

head=Reverse(head)
temp=head
while temp!=None:
    print(temp.data,end=" ")
    temp=temp.next
    
