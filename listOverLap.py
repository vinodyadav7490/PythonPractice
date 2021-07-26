'''
Ref: https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
'''
import random


def listOverLap(lst1,lst2):
   newList=[] #create a new list

   #check which is smaller list and run for loop on it
   firsts = len(lst1) > len(lst2)
   if firsts:
      a = lst1
      b = lst2
   else:
      a = lst2
      b = lst1

   for element in a:
      if (element in b) and (element not in newList):
         newList.append(element)
   return newList

def oneLiner(lst1,lst2):
   newList=[]
   #newList.append(e) for e in lst1 if (e in lst2) and (e not in newList)
   return newList

def generateRandomLenghtList():
   #a=[]
   n = random.randint(0,100)
   [a.append(random.randint(0,100)) for i in range(0,n)]
   return a

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


print("list Over lap: %s" %listOverLap(a,b))

a = generateRandomLenghtList()
print("List1: %s"%a)
b = generateRandomLenghtList()
print("List2: %s"%b)

print("list Over lap: %s" %listOverLap(a,b))