from ds.stacks.ArrayStack import ArrayStack

def reverse_file(filename):
    """Use stack to reverse contents of file"""
    s = ArrayStack()
    original_file = open(filename)
    for line in original_file:
        s.push(line.rstrip('\n'))
    original_file.close()

    # We will overwrite the file with stacked contents in reverse 
    # order that original file
    output_file = open(filename, 'w')
    while not s.is_empty():
        output_file.write(s.pop() + '\n')
    output_file.close()

if __name__ == "main":
    file_name = input()
    reverse_file(file_name)