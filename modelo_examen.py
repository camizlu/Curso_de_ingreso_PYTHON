import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Camila Zoe
apellido: Lucero

Enunciado:
De 5  mascotas que ingresan a una veterinaria  se deben tomar y validar los siguientes datos.

Nombre
Tipo (gato ,perro o exotico)
Peso ( entre 10 y 80)
Sexo( F o M  )
Edad(mayor a 0)

Pedir datos por prompt y mostrar por print, sDATOSe debe informar:
Informe A- Cuál fue el sexo menos ingresado (F o M)
Informe B- El porcentaje de mascotas hay  por tipo  (gato ,perro o exotico)
Informe C- El nombre y tipo de la mascota menos pesada
Informe D- El nombre del perro más joven
Informe E- El promedio de peso de todas las mascotas

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        
        MASCOTAS = 5
        contador_fem = 0 
        contador_mas = 0 
        
        sexo_menos_set = False 
        sexo_menos_ing = ""
        
        contador_gatos = 0 
        contador_perros = 0 
        contador_exotico = 0 
        
        menos_pesada_set = False
        menos_pesada_valor = None 
        menos_pesada_nombre = ""
        menos_pesada_tipo = ""
        
        
        perro_joven_set = False
        perro_joven_valor = None
        perro_joven_nombre = ""
        
        acumulador_peso_total = 0
        
        
        for i in range (MASCOTAS): 
            #validacion de datos 
            
            nombre = prompt ("Veterinaria","Ingrese el nombre: ")
            while nombre == None or nombre == "": 
                nombre = prompt ("Error","Ingrese el nombre: ")
                
            tipo = prompt ("Veterinaria","Ingrese el tipo [gato, perro o exotico]: ")
            while tipo != "gato" and tipo != "perro" and tipo != "exotico" or tipo == None or tipo == "" : 
                tipo = prompt ("Error","Ingrese el tipo [gato, perro o exotico]: ")
             
            peso = prompt ("Veterinaria","Ingrese el peso: ")
            while peso == None or int (peso) < 10 or int(peso) > 80: 
                peso = prompt ("Error","Ingrese el peso: ")    

            sexo = prompt ("Veterinaria","Ingrese el sexo [F/M]: ").upper()  
            while sexo == None or sexo == "" or (sexo != "F" and sexo != "M" ): 
                sexo = prompt ("Error","Ingrese el sexo [F/M]: ").upper()  

            edad = prompt ("Veterinaria","Ingrese la edad: ")
            while edad == None or int (edad) <1:
                edad = prompt ("Error","Ingrese la edad: ")
                
                
            #A Informe A- Cuál fue el sexo menos ingresado (F o M) 
            
            if sexo == "F":
                contador_fem +=1
            else: 
                contador_mas +=1
            
        
            if not sexo_menos_set or contador_fem < contador_mas: 
                sexo_menos_set = True 
                sexo_menos_ing = "F"
                
            if not sexo_menos_set or contador_mas < contador_fem: 
                sexo_menos_set = True 
                sexo_menos_ing = "M" 
                
            #Informe B- El porcentaje de mascotas hay  por tipo  (gato ,perro o exotico) 
        
            if tipo == "gato":
                contador_gatos +=1
            elif tipo == "perro": 
                contador_perros +=1 
            else: 
                contador_exotico +=1
                
                
            #Informe C- El nombre y tipo de la mascota menos pesada
            
            if not menos_pesada_set or menos_pesada_valor < int (peso): 
                menos_pesada_set = True
                menos_pesada_valor = peso
                menos_pesada_nombre = nombre
                menos_pesada_tipo = tipo
                
                
            #Informe D- El nombre del perro más joven
            
            if tipo == "perro":
                if not perro_joven_set or perro_joven_valor < int (edad): 
                    perro_joven_set = True 
                    perro_joven_valor = edad 
                    perro_joven_nombre = nombre 
                    
                    
            acumulador_peso_total += int (peso)
            acumulador_peso_total = int (acumulador_peso_total)
                    
            
        # salgo del for 
        
            porcentaje_gatos = (contador_gatos / MASCOTAS) * 100
            porcentaje_perros = (contador_perros / MASCOTAS) * 100
            porcentaje_exoticos = (contador_exotico / MASCOTAS) * 100
            
            
            # Informe E- El promedio de peso de todas las mascotas
    
            promedio_mascotas = acumulador_peso_total / MASCOTAS

            
            
        print ("A)",f"El sexo menos ingresado fue {sexo_menos_ing}")
        print ("B)",f"El porcentaje de gatos es {porcentaje_gatos}%, el de perros {porcentaje_perros}% y el de exoticos {porcentaje_exoticos}% ")
        print ("C)",f"El tipo de mascota más pesada es {menos_pesada_tipo} y su nombre es {menos_pesada_nombre}")
        print ("D)",f"El nombre del perro más joven es {perro_joven_nombre}")
        print ("E)",f"El promedio del peso de todas las mascotas es {promedio_mascotas}")

        
            

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
