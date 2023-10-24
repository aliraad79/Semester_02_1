class Heater:
    def __init__(self) -> None:
        self.water_temp = 60
        self.is_on = False

    def update_heat(self, currentTemp):
        if currentTemp <= 15 and not self.is_on:
            self.water_temp = 50
            self.is_on = True
        if currentTemp <= 5 and self.water_temp == 50:
            self.water_temp = 60
        if currentTemp <= -5 and self.water_temp == 60:
            self.water_temp = 80

        # Reverse
        if currentTemp > 0 and self.water_temp == 80:
            self.water_temp = 60
        if currentTemp > 10 and self.water_temp == 60:
            self.water_temp = 50
        if currentTemp > 30 and self.water_temp == 50:
            self.is_on = False

    def __repr__(self) -> str:
        return f"<Heater: isOn={self.is_on} ,water_temp={self.water_temp}>"


class Cooler:
    def __init__(self) -> None:
        self.CRS = 4
        self.isOn = False

    def update_fanspeed(self, currentTemp):
        if currentTemp >= 35 and not self.isOn:
            self.CRS = 4
            self.isOn = True
        if currentTemp >= 40 and self.CRS == 4:
            self.CRS = 6
        if currentTemp >= 45 and self.CRS == 6:
            self.CRS = 8

        # Reverse
        if currentTemp < 40 and self.CRS == 8:
            self.CRS = 6
        if currentTemp < 35 and self.CRS == 6:
            self.CRS = 4
        if currentTemp < 25 and self.CRS == 4:
            self.isOn = False

    def __repr__(self) -> str:
        return f"<Cooler: isOn={self.isOn} ,FanSpeed={self.CRS}>"


class ControllSystem:
    def __init__(self) -> None:
        self.heater = Heater()
        self.cooler = Cooler()

    def update_state(self, current_temp):
        self.heater.update_heat(current_temp)
        self.cooler.update_fanspeed(current_temp)

    def get_state(self) -> str:
        return f"{self.heater}\n{self.cooler}"


system = ControllSystem()
for i in [
    5,
    10,
    15,
    20,
    25,
    30,
    40,
    60,
    100,
    150,
    90,
    80,
    70,
    45,
    29,
    24,
    19,
    16,
    14,
    20,
    24,
    10,
    4,
    0,
    -5,
    -6,
    -15,
]:
    system.update_state(i)
    print(f"System At temprature of {i}:")
    print(system.get_state())
