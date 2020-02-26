import serial

#https://pureholic.tistory.com/47
#https://sonar2.tistory.com/96

ser = serial.Serial("COM3", 115200)

ser.write(b'h')
print(ser.readline())

# while True:
#     # print("insert op :", end=' ')
#     # op = input()
#     op = "Hello World"
#     ser.write(op.encode())
#
#     rd = ser.read()
#     print("W: ", op)
#     print("R: ", rd)