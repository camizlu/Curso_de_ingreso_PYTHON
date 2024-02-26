import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Camila 
apellido: Lucero

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        
        cantidad_personas = 0 
        #sexo [F/M/NB]
        cantidad_femenino = 0 
        cantidad_masculino = 0 
        cantidad_nb = 0 
        #temperatura 
        si_fiebre = 0 
        no_fiebre = 0
        #edades
        edad_masculino = 0 
        
        while cantidad_personas <5: 
            
            # Datos y validación 
            nombre = str(prompt("Datos","Ingrese su nombre: ")) 
            
            temperautra = int (prompt ("Datos", "Ingrese su temperatura: [35-42]"))
            while temperautra <35 or temperautra > 42: 
                temperautra = int (prompt ("Error", "Reingrese su temperatura: [35-42]"))
                
            sexo = str (prompt ("Datos","Ingrese su sexo [F/M/NB]"))
            while sexo != "F" and sexo != "M" and sexo != "NB":
                sexo = str (prompt ("Error","Reingrese su sexo [F/M/NB]"))

            edad = int (prompt ("Datos","Ingrese su edad: "))
            while edad < 0: 
                edad = int (prompt ("Error","Reingrese su edad: "))
                
            print (nombre, sexo, edad, temperautra)
                
            #Cantidad por genero 
                
            if sexo == "F": 
                cantidad_femenino = cantidad_femenino + 1 
            elif sexo == "M": 
                cantidad_masculino = cantidad_masculino + 1
                edad_masculino = edad_masculino + edad
            else: 
                cantidad_nb = cantidad_nb + 1   
                
            #Personas con fiebre 
            
            if temperautra > 36: 
                si_fiebre = si_fiebre + 1 
            else: 
                no_fiebre + 1                         
                                    
            cantidad_personas = cantidad_personas + 1 # salir del while 
            
        #A) informar cual fue el sexo mas ingresado   
         
        if cantidad_femenino > cantidad_masculino and cantidad_femenino > cantidad_nb: 
            mayor = "Femenino"
        elif cantidad_masculino > cantidad_nb: 
            mayor = "Masculino"
        else: 
            mayor = "No binario"
    
        print (f"A) El sexo más ingresado es {mayor}")
        
        #B) informar el porcentaje de personas con fiebre y el porcentaje sin fiebre
        
        porcentaje_fiebre = si_fiebre * 100 / cantidad_personas
        porcentaje_no_fiebre = no_fiebre * 100 / cantidad_personas
        
        print (f"B)El porcentaje de personas con fiebre es: {porcentaje_fiebre}% y de las personas sin fiebre es:{porcentaje_no_fiebre}%")
        
        #C) 
        print (f"C1) La cantidad de personas del sexo femenino es {cantidad_femenino}")
        promedio_edad_m = edad_masculino/cantidad_masculino 
        print (f"C2)La edad promedio de personas de sexo masculino{round(promedio_edad_m,2)}")
        #print (f"C3)La {}") #revisar como calcular los max y min, y el tema de banderas
        
        '''
        if temperatura > mayor_temperatura_nb:
                        mayor_temperatura_nb = temperatura
                        nombre_temp_alta_nb += nombre
                    else:
                        if temperatura < menor_temperatura_nb:
                            menor_temperatura_nb = temperatura
                            nombre_temp_baja_nb += nombre
            
        '''

            

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
