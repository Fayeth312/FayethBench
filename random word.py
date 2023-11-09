with open('filename.txt', 'r') as f:
  line = f.readline()
  while line:
    # do something to the line, for example
    # saving it to disk
    line = f.readline()