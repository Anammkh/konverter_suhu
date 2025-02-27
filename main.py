class Konversi:
    def __init__(self, suhu: float):
        self.suhu = suhu


class Celcius(Konversi):
    def _to_fahrenheit(self):
        return 9/5 * self.suhu + 32

    def _to_kelvin(self):
        return self.suhu + 273.15

    def _to_reaumur(self):
        return 4/5 * self.suhu

    def _to_rankie(self):
        return (self.suhu + 273.15) * 9/5


class Fahrenheit(Konversi):
    def _to_celcius(self):
        return (self.suhu - 32) * 5/9


if __name__ == "__main__":
    suhu = Fahrenheit(90)
    hasil = suhu._to_celcius()
    # hasil_2 = suhu._to_reaumur()
    print(f"hasil konversi {hasil}")
