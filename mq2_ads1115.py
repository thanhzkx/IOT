# mq2_ads1115.py
import time
import board
import busio
from adafruit_ads1x15.ads1115 import ADS1115, Mode
from adafruit_ads1x15.analog_in import AnalogIn

class MQ2ADS:
    def __init__(self, channel=0, gain=1):
        """
        channel: 0–3 tương ứng A0–A3
        gain: mức khuếch đại ADS1115 (1: ±4.096V thường dùng)
        """
        i2c = busio.I2C(board.SCL, board.SDA)
        self.ads = ADS1115(i2c)
        self.ads.mode = Mode.SINGLE
        self.ads.gain = gain

        if channel == 0:
            self.chan = AnalogIn(self.ads, ADS1115.P0)
        elif channel == 1:
            self.chan = AnalogIn(self.ads, ADS1115.P1)
        elif channel == 2:
            self.chan = AnalogIn(self.ads, ADS1115.P2)
        elif channel == 3:
            self.chan = AnalogIn(self.ads, ADS1115.P3)
        else:
            raise ValueError("Channel phải từ 0-3")

    def read_voltage(self):
        """
        Trả về điện áp MQ2 (Volt)
        """
        return self.chan.voltage

    def read_raw(self):
        """
        Giá trị 16-bit (-32768 → 32767)
        """
        return self.chan.value

    def read_percentage(self):
        """
        Chuyển đổi điện áp sang % gas tương đối
        """
        volt = self.read_voltage()
        return min(100, max(0, (volt / 5.0) * 100))   # MQ2 ăn 5V

