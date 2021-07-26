'''
Let’s say I give you a list saved in a variable:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].

Write one line of Python that takes this list a and makes a new list
that has only the even elements of this list in it.

'''

def listComprehension(lst1):
   lst = [lst1[i] for i in range(0,len(lst1),2)]
   return lst
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(listComprehension(a))