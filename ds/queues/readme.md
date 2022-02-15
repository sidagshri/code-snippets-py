# Queues

- It's a collection of objects where insertion and deletion is followed by First In First Out (FIFO)

# Std Operations

- _enqueue_: Add element to back of queue
  ```
    Q.enqueue(e)
  ```
- _dequeue_: Remove an element from front of queue
  ```
    Q.dequeue()
  ```

Some additional methods:

- _first_: return reference to first element, without removing from queue
  ```
    Q.first()
  ```
- _is_empty_: return True if queue is empty
  ```
    Q.is_empty()
  ```
- _len_: return number of elements in queue
  ```
    len(Q)
  ```
