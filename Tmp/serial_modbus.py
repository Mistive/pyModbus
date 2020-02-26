import serial
import pymodbus as pm
#https://pureholic.tistory.com/47
#https://sonar2.tistory.com/96
ser = serial.Serial("COM3", 115200, timeout = 500)

#op = bytearray([1,1,0,9,0,1,200,45])      #이런 식으로 사용
#op = bytearray(b'\x01\x01\x00\x03\x00\x12') #이런 식으로 사용
#op1 = bytearray(b'0x0100020001C079') #이런 식으로 사용
op = b"\x01\x01\x00\x09\x00\x01\xc8\x2d"
print("W(b): ", op)
#print("W(ascii): ", op.decode())
ser.write(op)
print("send")
print("R(b): ", ser.readline())

# while True:
#     print("R: ", ser.readline())

# while True:
#     op = bytearray(b'%$')
#     # op_b = op.encode()
#     # ser.write(op_b)
#     print("W: ", op)
#     #print("R: ", ser.readline())