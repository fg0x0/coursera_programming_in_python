import sys

num_steps = int(sys.argv[1])

for i in range(num_steps):
    print('{}{}'.format(" " * (num_steps - i - 1), '#' * (i+1)))
