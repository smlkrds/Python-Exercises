def nested_sum() :
  t = [[1, 9, 2], [3], [4, 5, 6]]
  sum = 0

  for i in t :
      if type(i) == list :
          for j in i :
              sum += j
      else :
          sum += i
  print(sum)

nested_sum()
