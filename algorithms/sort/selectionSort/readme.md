# Selection Search

- Search smallest element from current list (array) of items
- remove smallest element and append to new list (array) of items

# Algorithm

```
  findSmallest(arr):
    smallest = 0            # start with first element of current list

    for i to len(arr):
      if arr[i] < arr[smmallest]
        smallest = i        # if a new smallest element is found, update smallest index
    return smallest

  selectionSort(arr):
    newArr = []

    for i to len(arr):
      smallest = findSmallest(arr)
      newArr.append(arr.pop(smallest))  # remove smallest element from current list
                                        # and append to new arr

    return newArr

```

# Complexity

- Big O - `O(n^2)`
