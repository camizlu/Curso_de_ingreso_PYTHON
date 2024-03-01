import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Camila 
apellido: Lucero
---
Simulacro parcial 
---
Enunciado:

Se desea desarrollar un programa que permita al usuario ingresar el nombre, 
año emitido (inferior al 2000, Superior a 2000 e inferior a 2015 y superior al 2015),
si es online u offline y costo (500 a 10000) de 10 videojuegos.
Realizar las siguientes operaciones:

A - Encontrar el videojuego más caro y el más barato ingresado.
B - Calcular el promedio de los costos de los videojuegos, pero solo para aquellos que son online.
C - Encontrar los videojuegos con el costo máximo y mínimo de aquellos emitidos antes de 2015.
D - Calcular el porcentaje de videojuegos offline en relación al total de videojuegos ingresados.
E - Informar a que rango de año emitido pertenecen la mayor parte de los videojuegos vendidos.

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        
        mas_caro_valor = None
        mas_barato_valor = None
        
        mas_caro_set = False
        mas_barato_set = False 
        
        mas_caro_nombre = ""
        mas_barato_nombre = ""
        
        mas_caro_valor_15 = None
        mas_barato_valor_15 = None
        
        mas_caro_set_15 = False
        mas_barato_set_15 = False 
        
        costos_totales_online = 0
        contador_online = 0 
        contador_videojuegos = 0 
        contador_offline = 0 
        
        contador_menos2000 = 0
        contador_mas2000_menos15 = 0
        contador_mas2015 = 0  
       
        
        for i in range (10): 
            
            #Validación de datos 
            
            nombre = prompt("UTN","Ingrese el nombre del videojuego: ")
            while nombre == None or nombre == "": 
                nombre = prompt("Error","Ingrese un nombre valido: ")
                
            anio_emitido = prompt("UTN","Ingrese el año de emisión: [-2000/+2000,-2015/+2015]")
            while anio_emitido != "-2000" and anio_emitido != "+2000,-2015" and  anio_emitido != "+2015": 
                anio_emitido = prompt("Error","Ingrese el año de emisión: [-2000/+2000,-2015/+2015]")
                
            on_off_line = prompt("UTN","Ingrese si es [online/offline]")
            while on_off_line != "online" and on_off_line != "offline": 
                    on_off_line = prompt("Error","Ingrese un mensaje valido [online/offline]")

            costo = prompt("UTN","Ingrese el costo de videojuego: [500 - 10000]")
            while int (costo) < 500 or int (costo) > 10000: 
                costo = prompt("Error","Ingrese un costo valido: [500 - 10000]")
                
            #A
            if not mas_caro_set or costo > mas_caro_valor: 
                mas_caro_set = True
                mas_caro_valor = costo
                mas_caro_nombre = nombre
            
            if not mas_barato_set or costo < mas_barato_valor: 
                mas_barato_set = True
                mas_barato_valor = costo
                mas_barato_nombre = nombre
                
                
            #B 
            if on_off_line == "online": 
                costos_totales_online += costo
                contador_online +=1                 
                
            #C    
            if anio_emitido == "+2000,-2015": 
                if not mas_caro_set_15 or costo > mas_caro_valor_15: 
                    mas_caro_set_15 = True
                    mas_caro_valor_15 = costo
            
                if not mas_barato_set_15 or costo < mas_barato_valor_15: 
                    mas_barato_set_15 = True
                    mas_barato_valor_15 = costo
                    
            #D
                contador_videojuegos += 1
                if on_off_line == "offline": 
                    contador_offline += 1
                
            #E 
                match(anio_emitido): 
                    case "-2000": 
                        contador_menos2000 +=1 
                    case "+2000,-2015": 
                        contador_mas2000_menos15 +=1 
                    case "+2015": 
                        contador_mas2015 +=1
                                    
        #salgo del for 
        
            if contador_online > 0 : 
                promedio = costos_totales_online / contador_online
            else: 
                promedio = 0 
                
            if contador_offline > 0: 
                porcentaje_offline = (contador_videojuegos/contador_offline) * 100 
            else: 
                porcentaje_offline = 0 
                
                           
            if contador_menos2000 > contador_mas2000_menos15 and contador_menos2000 > contador_mas2015: 
                rango_mayor = "aquellos emitidos antes del 2000"
            elif contador_mas2000_menos15 > contador_mas2015:
                rango_mayor = "aquellos emitidos entre el 2000 y el 2015"
            else: 
                rango_mayor = "aquellos emititdos despues el 2015"
            
        
        print(f"A) El videojuego más caro es {mas_caro_nombre} y el más barato es {mas_barato_nombre}")
        print(f"B) El promedio del costo de los videojuegos online es ${promedio}")
        print(f"C) Para los juegos emitidos antes del 2015, el costo máximo es {mas_caro_valor_15}, y el costo minimo es {mas_barato_valor_15} ")
        print(f"D) El porcentaje de videojuegos offline es {porcentaje_offline}%")
        print(f"E) La mayoria de juegos vendidos pertence al rango de {rango_mayor}")

                      
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
