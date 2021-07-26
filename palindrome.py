'''
what is palindrome
if string and its reverse is same then we call the string as palindrome

'''

def palindromeUsingList(s):
   ps = s[::-1]
   if ps == s:
      return True
   else:
      return False

def palindromeUsingBuiltInFn(s):
   ps = ''.join(reversed(s))
   if ps == s:
      return True
   else:
      return False
   return

def palindromeUsingForLoop(s):
   ps=''
   ln =len(s)
   for i in range(ln):
      ps += s[ln -1 - i]
   if ps == s:
      return True
   else:
      return False
   return

s = "rekha"
print("Is '%s' a palindrome" %s)

print("Using List: %s "%palindromeUsingList(s))
print("Using Built in fn: %s "%palindromeUsingBuiltInFn(s))

print("Using for loop: %s "%palindromeUsingForLoop(s))