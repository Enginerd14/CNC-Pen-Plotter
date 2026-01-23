from machine import Pin
import time

X_STEP   = Pin(12, Pin.OUT)
X_DIR    = Pin(13, Pin.OUT)
X_LIMIT  = Pin(15, Pin.IN, Pin.PULL_UP)

Y_STEP   = Pin(25, Pin.OUT)
Y_DIR    = Pin(14, Pin.OUT)
Y_LIMIT  = Pin(4, Pin.IN, Pin.PULL_UP)

ENABLE   = Pin(26, Pin.OUT)

STEP_DELAY = 0.001
MOVE_STEPS = 2000

ENABLE.value(0)

def step_motor(step_pin, delay):
    step_pin.value(1)
    time.sleep(delay)
    step_pin.value(0)
    time.sleep(delay)

def move_axis(step_pin, dir_pin, limit_pin, direction):
    dir_pin.value(direction)
    for i in range(MOVE_STEPS):
        if limit_pin.value() == 0:
            break
        step_motor(step_pin, STEP_DELAY)

while True:
    move_axis(X_STEP, X_DIR, X_LIMIT, 1)
    time.sleep(1)

    move_axis(X_STEP, X_DIR, X_LIMIT, 0)
    time.sleep(1)

    move_axis(Y_STEP, Y_DIR, Y_LIMIT, 1)
    time.sleep(1)

    move_axis(Y_STEP, Y_DIR, Y_LIMIT, 0)
    time.sleep(3)
