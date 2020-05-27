# import time;
# from functools import lru_cache;

# @lru_cache(maxsize=3)
# def some(n):
#     time.sleep(n);
#     return n;

# if __name__ == "__main__":
#     print('before calling');
#     some(3);
#     some(1);
#     some(6);
#     some(9);
#     print('hello');
#     some(3);
#     print('4 call');

a = int(input());
import time;

from functools import lru_cache

@lru_cache(maxsize=a)
def some(n):
    time.sleep(n);
    return;

if __name__ == "__main__":
    print('started');
    some(3);
    some(2);
    print('hello');
    some(1);
    some(3);
    print('hello');