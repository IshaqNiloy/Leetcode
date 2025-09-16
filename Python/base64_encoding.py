import string
import sqlite3
import time

# Base62 character set
BASE62 = string.ascii_letters + string.digits

# Function to convert an integer to a base62 string
def encode_base62(num):
    if num == 0:
        return BASE62[0]
    arr = []
    base = len(BASE62)
    while num:
        num, rem = divmod(num, base)
        arr.append(BASE62[rem])
    arr.reverse()
    return ''.join(arr)


if __name__ == '__main__':
    print(time.time()*1000)
    print(encode_base62(int(time.time()*1000)))

