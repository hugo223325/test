import random

from utils import PLC_SAMPLES, PLC_PERIOD_SEC
from minicps.devices import PLC
from utils import PLC3_DATA, STATE
import time

T101 = ('T101', 1)
H101 = ('H101', 1)
T201 = ('T201', 2)
H201 = ('H201', 2)
F201 = ('F201', 2)
P301 = ('P301', 3)

class PhysicalProcess(PLC):
    def main_loop(self):
        count = 0
        while (count <= PLC_SAMPLES):
            # 更新T101温度值
            current_temp_T101 = float(self.get(T101))
            if current_temp_T101 >= 70:
                self.set(T101, 30.0)
            else:
                self.set(T101, current_temp_T101 + 1)  # 每次循环温度上升1度

            # 更新H101湿度值
            current_humidity_H101 = float(self.get(H101))
            if current_humidity_H101 <= 12:
                self.set(H101, 22.0)
            else:
                self.set(H101, current_humidity_H101 - 0.5)  # 每次循环湿度下降0.5%

            # 更新T201温度值
            current_temp_T201 = float(self.get(T201))
            if current_temp_T201 >= 30:
                self.set(T201, 20.0)
            else:
                self.set(T201, current_temp_T201 + 0.5)  # 每次循环温度上升0.5度

            # 更新H201湿度值
            current_humidity_H201 = float(self.get(H201))
            if current_humidity_H201 >= 18:
                self.set(H201, 15.0)
            else:
                self.set(H201, current_humidity_H201 + 0.1)  # 每次循环湿度上升0.1%

            # 设置F201流量，固定值
            self.set(F201, 20.0)

            # 更新P301气压值
            current_pressure_P301 = float(self.get(P301))
            if current_pressure_P301 < 0.98 or current_pressure_P301 > 1.06:
                self.set(P301, 1.00)
            else:
                self.set(P301, random.uniform(0.99, 1.05))  # 在0.99至1.05之间随机设置气压值

            # 等待一段时间后进行下一次循环
            time.sleep(PLC_PERIOD_SEC)
            count += 1

        print('DEBUG: physical process shutdown')



if __name__ == "__main__":
    # notice that memory init is different form disk init
    plc1 = PhysicalProcess(
        name='pp',
        state=STATE,
        protocol=None,
        memory=PLC3_DATA,
        disk=PLC3_DATA)
