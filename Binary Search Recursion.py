
def binarysearch(list, idx0, idxn, val):
   if (idxn < idx0):
      return None
   else:
      midvalue = idx0 + ((idxn - idx0) // 2)

   if list[midvalue] > val:
      return binarysearch(list, idx0, midvalue-1,val)
   elif list[midvalue] < val:
      return binarysearch(list, midvalue+1, idxn, val)
   else:
      return midvalue

    
list = [8,11,24,56,88,131]
print(binarysearch(list, 0, 5, 24))
print(binarysearch(list, 0, 5, 51))
