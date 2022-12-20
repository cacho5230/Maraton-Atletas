from pymysql import Error
import pymysql

#DATABASE + CURSOR
db = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    port=3306,
    database="maraton_atletas")

cursor = db.cursor()

#definicion de clase atleta

class Atletas():
    def __init__(self, idatleta, apellido, nombre, edad):
        self.idatleta = idatleta
        self.apellido = apellido
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def conseguir_todos_atletas(self):
        try:
            cursor.execute("SELECT * FROM atletas")
            resultado = cursor.fetchall()
            return resultado
        except Error as ex:
            print("Error en la base de datos: {0}".format(ex))

    @classmethod
    def crear_atleta_nuevo(self,atleta):
        try:
            cursor.execute("INSERT INTO atletas(apellidos,nombres,edad) VALUES(%s,%s,%s)", [atleta['apellido'], atleta['nombre'], int(atleta['edad'])])
            db.commit()
        except Error as ex:
            print("Error en la base de datos: {0}".format(ex))

    @classmethod
    def eliminar_atleta(self, id):
        try:
            cursor.execute("DELETE FROM atletas WHERE idatleta = %s", [id])
            db.commit()
        except Error as ex:
            print("Error en la base de datos: {0}".format(ex))


class Inscripciones():
    def __init__(self):
        pass

    @classmethod
    def conseguir_posiciones_atletas(self):
        try:
            cursor.execute(
                "SELECT * FROM atletas JOIN inscripciones ON atletas.idatleta = inscripciones.idatleta")
            resultado = cursor.fetchall()
            return resultado
        except Error as ex:
            print("Error en la base de datos: {0}".format(ex))

    @classmethod
    def mostrar_posiciones(self):
        try:
            cursor.execute(
                "SELECT posicion,tiempo,dorsal,apellidos,nombres FROM atletas JOIN inscripciones ON atletas.idatleta = inscripciones.idatleta ORDER BY inscripciones.tiempo")
            resultados = cursor.fetchall()
            return resultados
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    @classmethod
    def inscribir_atleta(self, inscripcion):
        try:
            cursor.execute("INSERT INTO inscripciones(idatleta,dorsal,distancia) VALUES(%s,%s,%s)", [
                           int(inscripcion['idatleta']), int(inscripcion['dorsal']), int(inscripcion['distancia'])])
            db.commit()
        except Error as ex:
            print("Error en la base de datos: {0}".format(ex))

    @classmethod
    def registrar_posicion_atleta(self, inscripcion):
        try:
            cursor.execute("UPDATE inscripciones SET tiempo = %s, posicion = %s WHERE idatleta = %s", [
                           inscripcion['tiempo'], int(inscripcion['posicion']), int(inscripcion['idatleta'])])
            db.commit()
        except Error as ex:
            print("Error en la base de datos: {0}".format(ex))
