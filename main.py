from time import sleep

from tasks import fib
import sys


if __name__ == '__main__':
    value = int(sys.argv[1])
    task = fib.delay(value)
    print(task.id)

    while not task.ready():
        sleep(0.2)
        print(f'Processing......')
    print(task.get())






