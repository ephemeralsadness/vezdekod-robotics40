import sys
import time
import random
import math


def a1():
  return brick.sensor("A1").read()
  
def a2():
  return brick.sensor("A2").read()

def a3():
  return brick.sensor("A3").read()
  
def d1():
  return brick.sensor("D1").read()
  
def d2():
  return brick.sensor("D2").read()
  

def move_from_line(speed, left=True, right=True):
  while True:
    if left and right:
      if a1() != 0 and a2() != 0:
        break
    elif left:
      if a1() != 0:
        break
    elif right:
      if a2() != 0:
        break
    else:
      break
    brick.motor("M3").setPower(speed)
    brick.motor("M4").setPower(speed)
  
  
def move_to_line(speed, left=True, right=True):
  while True:
    if (left and a1() == 0) or (right and a2() == 0):
      break;
    brick.motor("M3").setPower(speed)
    brick.motor("M4").setPower(speed)


def rotate(speed, left=True, stop_left=False):
  if left:
    while True:
      if stop_left and a2() != 0:
        break
      if not stop_left and a1() != 0:
        break
      brick.motor("M4").setPower(0)
      brick.motor("M3").setPower(speed)
  else:
    while True:
      if stop_left and a2() != 0:
        break
      if not stop_left and a1() != 0:
        break
      brick.motor("M3").setPower(0)
      brick.motor("M4").setPower(speed)


# правое колесо в начале линии
def move_round(speed):
  while d2() > 40:
    if (a1() != 0):
      brick.motor("M3").setPower(0)
      brick.motor("M4").setPower(speed)
    else:
      brick.motor("M3").setPower(speed)
      brick.motor("M4").setPower(speed)
  brick.motor("M3").setPower(speed)
  brick.motor("M4").setPower(speed)
  time.sleep(0.02 * d2())


def rotate_to_ball(speed):
  while (a3() > 40):
    brick.motor("M3").setPower(0)
    brick.motor("M4").setPower(speed)
    brick.motor("M3").setPower(-speed)
    brick.motor("M4").setPower(0)
  brick.motor("M3").setPower(0)
  brick.motor("M4").setPower(speed)
    
    
def push_ball(speed):
  brick.motor("M3").setPower(speed)
  brick.motor("M4").setPower(speed)
  time.sleep(1)
  while a1() + a2() == 0:
    brick.motor("M3").setPower(speed)
    brick.motor("M4").setPower(speed)
  brick.motor("M3").setPower(speed)
  brick.motor("M4").setPower(speed)
  time.sleep(0.2)
    
    
def comeback(speed):
  brick.motor("M3").setPower(-speed)
  brick.motor("M4").setPower(-speed)
  time.sleep(0.8)
  brick.motor("M3").setPower(0)
  brick.motor("M4").setPower(speed)
  time.sleep(1.2)
  brick.motor("M3").setPower(speed)
  brick.motor("M4").setPower(speed)
  
  while a1() == 0:
    brick.motor("M3").setPower(int(speed * (9 / 10)))
    brick.motor("M4").setPower(speed)
    
  brick.motor("M3").setPower(0)
  brick.motor("M4").setPower(speed)
  time.sleep(0.5)


def return_to_home(speed):
  brick.motor("M3").setPower(speed)
  brick.motor("M4").setPower(speed)
  time.sleep(1)
  
  while a1() + a2() == 0:
    brick.motor("M3").setPower(speed * (75 / 100))
    brick.motor("M4").setPower(speed)
  time.sleep(1)


class Program():
  interpretation_started_timestamp = time.time() * 1000

  pi = 3.141592653589793
  
  def execMain(self):
    move_from_line(100)
    move_to_line(100)
    move_from_line(100)
    move_to_line(100)
    for i in range(8):
      rotate(100)
      move_round(100)
      rotate_to_ball(100)
      push_ball(100)
      comeback(100)
    return_to_home(100)
    brick.stop()
    return

def main():
  program = Program()
  program.execMain()

if __name__ == '__main__':
  main()
