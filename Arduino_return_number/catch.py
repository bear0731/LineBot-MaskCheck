import serial

comPort="COM3"
baudRate=9600
si=serial.Serial(comPort,baudRate)

while True:
    try: 
        while si.in_waiting:
            data=si.readline().decode('utf-8')
            print(data)
            
    except KeyboardInterrupt:
        si.close()
        print('shotDown')
