import ctypes
import threading
import queue,time
import serial,sys
import cross_corr_via_serial_sub
from picosdk.usbtc08 import usbtc08 as tc08
from picosdk.functions import assert_pico2000_ok
from pico_single import pico_single

i=1
q =queue.Queue()  # queue which stores a result of a thread
th = threading.Thread(target=cross_corr_via_serial_sub.serial_cross_corr, args=(sys.argv[1],sys.argv[2],q),daemon=True)
th.start()
print("start thread: "+str(i))
#th.join()
while True:
  if threading.active_count()==1:
    ix = q.get()
    print(ix)
    i=i+1
    if i>5:
      break;
    th = threading.Thread(target=cross_corr_via_serial_sub.serial_cross_corr, args=(sys.argv[1],sys.argv[2],q),daemon=True)
    th.start()
    print("start thread: "+str(i))
  else:
    print(str(i)+": "+str(pico_single()))
exit()
