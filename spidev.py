# spidev.py (fake SPI to allow testing on Windows)

class SpiDev:
    def open(self, bus, device):
        print("[Fake SPI] open")

    def xfer2(self, data):
        print("[Fake SPI] Transfer:", data)
        return [0, 0, 0]  # giả lập dữ liệu trả về

    def close(self):
        print("[Fake SPI] close")

    max_speed_hz = 1350000
