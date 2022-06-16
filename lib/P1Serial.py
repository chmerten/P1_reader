import serial

class P1Serial():
    def __init__(self, port):
        #port='/dev/ttyUSB0'
        self.serial = serial.Serial(port, 115200, xonxoff=1)
        self.obis_codes = {
            "0-0:1.0.0": "Timestamp",
            "0-0:96.3.10": "Switch electricity",
            "0-0:96.1.1": "Meter serial electricity",
            "0-0:96.14.0": "Current rate (1=day,2=night)",
            "1-0:1.8.1": "Rate 1 (day) - total consumption [kWh]",
            "1-0:1.8.2": "Rate 2 (night) - total consumption [kWh]",
            "1-0:2.8.1": "Rate 1 (day) - total production [kWh]",
            "1-0:2.8.2": "Rate 2 (night) - total production [kWh]",
            "1-0:1.7.0": "All phases consumption [kW]",
            "1-0:2.7.0": "All phases production [kW]",
            "0-0:17.0.0" : "Power [kVA]"
        }

    def get_telegram(self):
        p1telegram = bytearray()
        while True:
            try:
                # read input from serial port
                p1line = self.serial.readline()
                # P1 telegram starts with /
                if "/" in p1line.decode('ascii'):
                    p1telegram = bytearray()
                    print('*' * 60 + "\n")
                # add line to complete telegram
                p1telegram.extend(p1line)
                # P1 telegram ends with ! + CRC16 checksum
                if "!" in p1line.decode('ascii'):
                    return p1telegram

            except KeyboardInterrupt:
                print("Stopping...")
                self.serial.close()
                break
            except:
                if debug:
                    print(traceback.format_exc())
                # print(traceback.format_exc())
                print ("Something went wrong...")
                self.serial.close()
            # flush the buffer
            self.serial.flush()

    def parse_telegram(self,p1telegram):
        output = []
        for line in p1telegram.split(b'\r\n'):
            print(line.decode('ascii'))

        