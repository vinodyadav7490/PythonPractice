'''
Fibonacci Number:
Each number in the sequence is the sum of the two numbers that precede it.
So, the sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on.
'''

def fibonacci(n):
   seq=[]
   if n == 0:
      seq.append(n)
      seq.append(1)
      n=1
   for i in range(1,10):
      seq.append(n)
      n = seq[i] + n
   return seq

print(fibonacci(0))