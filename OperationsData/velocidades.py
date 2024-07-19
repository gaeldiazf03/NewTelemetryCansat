class CalculoVelocidades:
    def __init__(
            self,
            h_inicio, h_final,
            time_inicio, time_final
    ) -> None:
        # Asignación de las variables
        self.h_inicio = float(h_inicio)
        self.h_final = float(h_final)
        self.time_inicio = float(time_inicio)
        self.time_final = float(time_final)
        self.velocidad = self.calculo()  # Velocidad en Y

    def calculo(self) -> float:
        return round(((self.h_final-self.h_inicio) / (self.time_final-self.time_inicio)), 12)


if __name__ == '__main__':
    h_inicial: str = '0'
    h_end: str = '375'
    time_inicial: str = '0'
    time_end: str = '5'
    print(CalculoVelocidades(h_inicial, h_end, time_inicial, time_end).velocidad)
