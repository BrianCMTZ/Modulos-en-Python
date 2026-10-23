class Videojuego:
    def __init__(self, titulo, genero, año):
        self.titulo = titulo
        self.genero = genero
        self.año = año

    def resumen(self):
        return f"El Juego es: {self.titulo} su género: {self.genero} y fue lanzado en: {self.año}"
