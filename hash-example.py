from hashlib import sha256
import argparse
import time

# Lets decide that the hash of some integer x multiplied by another y must end in 0.
# So hash(x * y) = ac23dc...0.

# setup the arguments for the command line
parser = argparse.ArgumentParser()
parser.add_argument('-x', '--first_number', type=int, default=5, help='number of 0 in hash end')
parser.add_argument('-n', '--number_of_zero', type=int, default=5, help='number of 0 in hash end')
args = parser.parse_args()

x = args.first_number  # default to 5
y = 0

n = args.number_of_zero  # default to 5

ending_zeros = '0' * n  # n zeros at the end of the hash

start_time = time.time()  # start time of the program

while sha256(f'{x*y}'.encode()).hexdigest()[-n:] != ending_zeros:
    print(sha256(f'{x*y}'.encode()).hexdigest()[-n:])
    y += 1

print(sha256(f'{x*y}'.encode()).hexdigest()[-n:])
# calculate the running time
total_seconds = time.time() - start_time
print(f'total seconds are {total_seconds}')
m, s = divmod(total_seconds, 60)
h, m = divmod(m, 60)

# Tried 840258 numbers and took 0:00:07 to be correct when n=5
# Tried 5199280 numbers and took 0:00:42 to be correct when n=6
# Tried 73102419 numbers and took 0:10:31 to be correct when n=7
print("Tried %d numbers and took %d:%02d:%02d to be correct" % (y, h, m, s))
