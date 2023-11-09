import math

from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path


DIR = Path(__file__).parent


@dataclass
class TemperatureData:
    datetime: datetime
    value_in_kelvin: float

    @staticmethod
    def from_csv(csv: str) -> "TemperatureData":
        dt, kelvin = csv.split(",")
        return TemperatureData(datetime.fromisoformat(dt), float(kelvin))


def write_celsius_values_in_timeframe_to_log(start: datetime, end: datetime) -> None:
    data = []
    for line in (DIR / "values.csv").read_text().splitlines():
        data.append(TemperatureData.from_csv(line))

    celsius_values: list[float] = []
    for d in data:
        if not math.isnan(d.value_in_kelvin):
            if start < d.datetime < end:
                celsius_values.append(d.value_in_kelvin - 273.15)

    (DIR / "logfile.txt").write_text("\n".join(map(str, celsius_values)))


START_DATE = datetime(2023, 9, 20, hour=8)
END_DATE = START_DATE + timedelta(hours=2)

if __name__ == "__main__":
    write_celsius_values_in_timeframe_to_log(START_DATE, END_DATE)
