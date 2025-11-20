import spidev
import time
from core.env_data import EnvStore

class KY037:
    def __init__(self, channel=1, bus=0, device=0):
        self.channel = channel
        self.spi = spidev.SpiDev()
        try:
            self.spi.open(bus, device)
            self.spi.max_speed_hz = 1350000
        except Exception as e:
            print(f"Lỗi khởi tạo SPI cho KY037: {e}")

    def read_raw(self):
        try:
            adc = self.spi.xfer2([1, (8 + self.channel) << 4, 0])
            data = ((adc[1] & 3) << 8) + adc[2]
            return data
        except Exception as e:
            print(f"Lỗi đọc cảm biến KY037: {e}")
            return 0 

    def update(self):
        level = self.read_raw()
        EnvStore.update(sound_level=level)

    def close(self):
        self.spi.close()