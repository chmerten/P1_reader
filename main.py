from lib.P1Serial import P1Serial

p1reader = P1Serial('/dev/ttyUSB0')
p1telegram = p1reader.get_telegram()
print(p1telegram)
print(p1reader.parse_telegram(p1telegram))

