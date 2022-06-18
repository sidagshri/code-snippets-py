# Binary Search

- It can be implemented on a sorted or ordered list
- We start with initial start and end of given list
- We keep guessing the middle element, to match
- If guessed element is higher, we need to cut the lower half of list
- If guessed element is lesser, we need to cut the upper half of list
- When ends are reversed or list finishes, element is not present
- This way we keep dividing the list to half and excluding the half of list where we wont find the element

# Algorithm

```
  low = 0 # begining of list
  high = length(list) - 1   # end of list

  loop low <= high:
    mid = (low + high) / 2  # middle of current list
    guess = list[mid]       # middle element of current list
    if guess == item:       # middle element of current list is same as item to be found
      return mid            # return current position of middle element
    else if guess > item:   # middle element of current list is greater than item to be found
      high = mid - 1
    else:                   # middle element of current list is smaller than item to be found
      low = mid + 1

  return NOT_FOUND          # element was not found

```

# Complexity

- Big O - `O(log N)`
