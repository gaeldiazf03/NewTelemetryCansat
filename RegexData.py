import regex
import measurement

@measurement.singleton
class RegexData:
    def __init__(self, string: str) -> None:
        self.string = string
        self.list_q_data = self.get_data_q()

    def get_data_q(self) -> list[tuple[str, str]]:
        # Regex para buscar cadenas de Q's
        # which_load = regex.compile(r'(Serial:\(\+RCV=\d,(.*?)\)')
        which_load = regex.compile(r'''(
                                   (Serial\d):  # Parte inicial del Serial. Ejemplo: Serial1 || Serial2
                                   \(([^)]*)\)  # Grupo que captura todo lo que esta dentro del serial.
                                   )''', regex.VERBOSE)
        list_q_data = which_load.findall(self.string)
        return list_q_data

    def get_status(self, q: int, looking: str) -> float:
        # Regex para la búsqueda de datos
        look_for = regex.compile(r'''(
                                 ({}):  # Búsqueda de la palabra clave.
                                 (\-?\d+(?:\.\d+)?)  # Datos a buscar.
                                 )'''.format(looking), regex.VERBOSE)
        try:
            alldata = str(self.list_q_data[q-1][2])
        except IndexError:
            return None
        else:
            seeing = look_for.search(alldata)
            if seeing is not None:
                return float(seeing.group(3))
            else:
                return None
            

@measurement.measure_time
def main(text: str):
    data = RegexData(text)

    print("/*Búsqueda de datos*/")
    data_temp = data.get_status(1, "TEMP")
    data_Q2 = data.get_status(2, "LONG")

    print(data_temp)
    print(data_Q2)


if __name__ == '__main__':
    text = "Serial1:(+RCV=3,137,TEMP:31.69,Ax:1.14,Ay:1.17,Az:9.50,Gx:-0.01,Gy:-0.07,Gz:-0.03,LAT1:22.29,LON1:-97.88,PRES:1012.78,HUM:61.26,ALT:4.36,Pila:0.00,0%,ETAPA:1,-47,30),Serial2:()"
    main(text)
