import time
import smbus

bus = smbus.SMBus(1)

def setup(Addr):
    global address
    address = Addr
    
def read(): #channel
    try:
        bus.write_byte(address, 0x41)
    except Exception as e:
        print("Address : %s" % address)
        print(e)
    return bus.read_byte(address)

if __name__ == "__main__":
    setup(0x48)
    while True:
        print("AIN1 = ", read())
        time.sleep(0.1)