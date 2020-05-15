class Coche:
    def __init__(self, marca, color, combustible, cilindrada):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada

    def mostrar(self):
        print("\nMarca: ",self.marca,"\nColor: ",self.color,"\nCombustible: ",self.combustible,
        "\nCilindrada: ",self.cilindrada,)


media = lambda nota1, nota2, nota3 : (nota1 + nota2 + nota3) / 3
