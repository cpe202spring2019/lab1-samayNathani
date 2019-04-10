
def max_list_iter(int_list):
   if int_list is None:
      raise ValueError
   else:
      temp = int_list[0]
      for val in int_list:
         if val > temp:
            temp = val
      return temp

def reverse_rec(int_list):
   if int_list is None:
      raise ValueError
   if len(int_list) == 1:
      return(int_list)
   else:
      r = [int_list.pop(-1)]
      return r + (reverse_rec(int_list))

def bin_search(target, low, high, int_list):
   if int_list is None:
      raise ValueError
   if (high < low):
      return None
   mid = (high + low)//2
   if target == int_list[mid]:
      return mid
   else:
      if target < int_list[mid]:
         high = mid - 1
         return bin_search(target, low, high, int_list)
      else:
         low = mid + 1
         return bin_search(target, low, high, int_list)
