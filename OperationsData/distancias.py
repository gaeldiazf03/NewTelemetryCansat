import math
import decimal
from measurement import measure_time


class CalculoDistancia:
    _radio_ecuatorial: float = 6378.0

    def __init__(self, gps1: tuple[str], gps2: tuple[str]) -> None:
        # Conversión de Grados a Radianes
        self.lat1: float = self.get_radians(float(gps1[0]))
        self.lon1: float = self.get_radians(float(gps1[1]))
        self.lat2: float = self.get_radians(float(gps2[0]))
        self.lon2: float = self.get_radians(float(gps2[1]))
        # Diferencias
        self.dif_lat: float = self.get_radians(float(gps2[0]) - float(gps1[0]))
        self.dif_lon: float = self.get_radians(float(gps2[1]) - float(gps1[1]))
        # distancia entre cargas
        self.distancia = self.distancias()

    def distancias(self) -> float:
        a1 = math.pow(math.sin(self.dif_lat / 2), 2)
        a2 = math.cos(self.lat1) * math.cos(self.lat2) * math.pow(math.sin(self.dif_lon / 2), 2)
        a = a1 + a2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))  # Haversine xd
        return round(self._radio_ecuatorial * c * 1000, 12)  # Return on meters

    @staticmethod
    def get_radians(grads: float) -> float:
        return round(math.radians(decimal.Decimal(grads)), 12)


if __name__ == '__main__':
    @measure_time
    def main():
        ubi_1: tuple = ('19.326689667', '-99.187261')
        ubi_2: tuple = ('19.326711833', '-99.187336667')
        dist = CalculoDistancia(ubi_1, ubi_2)
        print(dist.distancia, ' metros')
    main()
