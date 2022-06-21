import dataclasses
import time
import board
from adafruit_seesaw.seesaw import Seesaw


@dataclasses.dataclass
class SensorReading:
  moisture: int
  temperature: float


def get_reading(sensor: Seesaw) -> SensorReading:
  return SensorReading(
    moisture=sensor.moisture_read(),
    temperature=sensor.get_temp()
  )


def main() -> None:
  i2c_bus = board.I2C()
  seesaw = Seesaw(i2c_bus, addr=0x36)
  while True:
    reading = get_reading(seesaw)
    print(f"temperature: {reading.temperature}  moisture: {reading.moisture}")
    time.sleep(1)


if __name__ == '__main__':
  main()
