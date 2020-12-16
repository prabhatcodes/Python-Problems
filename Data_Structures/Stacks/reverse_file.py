def reverse_file(filename):
    """Overwriting a given file line by line
       in reversed order"""
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rsstrip('\n')) # we will re-insert newlines while writing
    original.close()

    # now we overwrite with contents in LIFO order
    output = open(filename, 'w') # reopening file overwrites original
    while not S.is_empty():
        output.write(S.pop() + '\n') # re-insert newline characters
    output.close()
