import dataclasses
import board
from adafruit_seesaw.seesaw import Seesaw
from flask import Flask


app = Flask(__name__)

@dataclasses.dataclass
class SensorReading:
  moisture: int
  temperature: float


def get_reading(sensor: Seesaw) -> SensorReading:
  return SensorReading(
    moisture=sensor.moisture_read(),
    temperature=sensor.get_temp()
  )


i2c_bus = board.I2C()
seesaw = Seesaw(i2c_bus, addr=0x36)

@app.route("/reading")
def reading():
  reading = get_reading(seesaw)
  return {
    'temperature': reading.temperature,
    'moisture': reading.moisture,
  }
