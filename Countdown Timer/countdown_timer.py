import time


def countdown(t):
    while t:
        minutes, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(minutes, secs)
        print(timer)
        time.sleep(1)
        t -= 1

    print('Timer completed!')


t = input('Enter the time in seconds: ')

countdown(int(t))
