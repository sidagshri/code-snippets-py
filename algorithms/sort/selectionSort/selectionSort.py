def findSmallest(arr):
  smallest = 0

  for i in range(1, len(arr)):
    if arr[i] < arr[smallest]:
      smallest = i

  return smallest

def selectionSort(arr):
  newArr = []

  for i in range(len(arr)):
    smallest = findSmallest(arr)
    newArr.append(arr.pop(smallest))
  
  return newArr

print(selectionSort([10,9,8,7,6,5,4,3,2,1,0]))
