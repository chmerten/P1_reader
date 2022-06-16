from lib.P1Serial import P1Serial

p1reader = P1Serial('/dev/ttyUSB0')
print(p1reader.get_telegram())

