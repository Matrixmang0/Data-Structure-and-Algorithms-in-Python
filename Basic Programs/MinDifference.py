def MinDifference(List, num):

  """Function to find the minimum difference that can be obtained from the unique sub-lists that can be stripped out from the given list from the parameter"""
  List = sorted(List)             # Sorting the list
  count = len(List)-num+1         # Number of unique lists that can be generated
  diff_list = []                  # List to store the differences between max and min in all the lists
  for i in range(count):
    diff = List[i+num-1]-List[i]  # Computing the difference between first and last elementin the list
    diff_list.append(diff)
  mini = min(diff_list)           # Finding the minimum of the list
  return (mini)

li = eval(input().strip())
P = int(input())
print(MinDifference(li, P))
