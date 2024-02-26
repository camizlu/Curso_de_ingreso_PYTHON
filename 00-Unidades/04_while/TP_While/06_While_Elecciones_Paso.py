import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Camila 
apellido: Lucero 
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        
        suma_edades = 0 
        total_votos = 0
        candidato_mas_votos = ""
        candidato_menos_votos = ""
        edad_c_menos_votos = 0 
        total_candidatos = 0 
        
        mas_votos = 0
        menor_votos = float('inf')

       
        while (True): 
            nombre = (prompt ("Elecciones","Ingrese el nombre de uno de los candidatos"))
            if (nombre == None): 
                break
            edad = int (prompt("Elecciones","Ingrese la edad del candidato"))
            while (edad < 25): 
                edad = int (prompt("ERROR","Ingrese una edad valida [+25]"))
            cantidad_votos = int (prompt("Elecciones","Ingrese la cantidad de votos"))
            while (cantidad_votos < 0): 
                cantidad_votos = int (prompt("Error","Ingrese una cantidad valida"))
                
            #analisis de datos
                
            if cantidad_votos > mas_votos:
                mas_votos = cantidad_votos  
                candidato_mas_votos = nombre
                
            if cantidad_votos < menor_votos: 
                menor_votos = cantidad_votos
                candidato_menos_votos = nombre
                edad_c_menos_votos = edad
                   
            suma_edades += edad 
            total_votos += cantidad_votos
            total_candidatos +=1
            
            promedio = suma_edades/total_candidatos
            promedio = round(promedio,1)
            
        alert("Resultados elecciones",f"Candidato con más votos: {candidato_mas_votos}\n"
            f"Candidato menos votos: {candidato_menos_votos} Edad: {edad_c_menos_votos}\n"
            f"Promedio de edades: {promedio}\n"
            f"Total de votos emitidos: {total_votos}"
            )
        
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()