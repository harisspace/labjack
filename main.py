from labjack import ljm
from time import sleep

handle = ljm.openS("T7", "ANY", "ANY")  # T7 device, Any connection, Any identifier

info = ljm.getHandleInfo(handle)
print("Opened a LabJack with Device type: %i, Connection type: %i,\n"
      "Serial number: %i, IP address: %s, Port: %i,\nMax bytes per MB: %i" %
      (info[0], info[1], info[2], ljm.numberToIP(info[3]), info[4], info[5]))

# Setup and call eReadName to read a value from the LabJack.
name = "AIN0"
i = 0

name1 = "DAC0"
value = 10  # 4 V
ljm.eWriteName(handle, name1, value)

while True:
    if (i<20):
        sleep(0.3)
        voltage = ljm.eReadName(handle, name)

        print("\neReadName result: ")
        print("    Name - %s, value : %f" % (name, voltage))
        i+=1
    else:
        s=input()
        if(s=="i"):
            i=0
        else:
            break    
