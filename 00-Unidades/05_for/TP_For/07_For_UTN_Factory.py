import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Camila 
apellido: Lucero
---
TP: For_UTN_Factory
---
Enunciado:
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        
        CANTIDAD_ITERACIONES = 10
        contador_puntoA = 0 
        contador_fem = 0 
        contador_mas = 0 
        contador_nb = 0 
        edad_fem = 0 
        edad_mas = 0
        edad_nb = 0
        contador_JS = 0 
        contador_PY = 0 
        contador_ASP = 0          
        
        menor_edad_junior = None
        menor_edad_junior_nombre = None
        
        
        
        for i in range (CANTIDAD_ITERACIONES): 
            nombre = prompt("UTN Software","Ingrese su nombre")
            while nombre == None or nombre == "": 
                nombre = prompt("Error","Ingrese un nombre valido")
            edad = prompt("UTN Software","Ingrese su edad")
            while edad == None or int (edad) < 18: 
                edad = prompt("Error","Ingrese una edad valida [+18]")
            genero = prompt("UTN Software","Ingrese su género [F/M/NB]").upper()
            while  (genero == None or (str(genero) != "F" and str(genero) != "M" and str(genero) != "NB")): 
                genero = prompt("Error","Ingrese un genero válido [F/M/NB]").upper()
            tecnología = prompt("UTN Software","Ingrese su tecnología[PYTHON - JS - ASP.NET]")
            while (str (tecnología) == None or (str(tecnología) != "PYTHON" and str(tecnología) != "JS" and str(tecnología) != "ASP.NET")): 
                tecnología = prompt("UTN Software","Ingrese una tecnología valida [PYTHON - JS - ASP.NET]")
            puesto = prompt("UTN Software","Ingrese su puesto [Jr - Ssr - Sr]")
            while (puesto == None or (str (puesto) != "Jr" and str (puesto) != "Ssr" and str (puesto) != "Sr")): 
                puesto = prompt("Error","Ingrese un puesto valido [Jr - Ssr - Sr]")
               
            #A 
            if (genero == "NB" and (tecnología == "JS" or tecnología == "ASP.NET")and edad > 24 and edad < 41 and puesto == "Ssr"): 
                contador_puntoA +=1 
                
                
            #B
                
                
            #C ver si lo puedo hacer con matcb
            if genero == "F":
                contador_fem +=1
                edad_fem += edad 
            elif genero == "M": 
                contador_mas +=1
                edad_mas += edad
            else: 
                contador_gen_total +=1
                contador_nb += 1
                edad_nb += edad
                
            #D
            if tecnología == "JS": 
                contador_JS +=1 
            elif tecnología == "PY": 
                contador_PY +=1
            else: 
                contador_ASP +=1
        
        #salgo del for 
                
        if contador_JS > contador_PY and contador_JS > contador_ASP: 
            mas_postulantes = "JS"
        elif contador_PY > contador_ASP :
            mas_postulantes = "PYTHON"
        else: 
            mas_postulantes = "ASP.NET"   
            
        #E
        porcentaje_fem = (contador_fem / CANTIDAD_ITERACIONES) * 100
        porcentaje_mas = (contador_mas/CANTIDAD_ITERACIONES) * 100
        porcentaje_nb = (contador_nb/CANTIDAD_ITERACIONES) * 100
            
        if contador_fem > 0: 
            promedio_fem = edad_fem / contador_fem 
        if contador_mas > 0: 
            promedio_mas = edad_mas / contador_mas
        if contador_nb > 0: 
            promedio_nb = edad_mas / contador_nb       
        
        print (f"A) Hay {contador_puntoA} postulantes con esas categorías")
        print(f"C)El promedio de edades del genero femenino es {promedio_fem}, el de masculino es {promedio_mas} y el de no binario es {promedio_nb}")
        print(f"D)La tecnología con más postulantes es: {mas_postulantes}")
        print(f"E)El porcentaje de postulantes femeninas es {porcentaje_fem}, el de masculinos {porcentaje_mas} y el de no binarios es {porcentaje_nb}")


# Verificamos si hay mujeres para evitar dividir por cero
if total_mujeres != 0:
    promedio_edades_mujeres = suma_edades / total_mujeres
    print("El promedio de edades femeninas es:", promedio_edades_mujeres)
else:
    print("No hay mujeres en el conjunto de datos.")         
            
                
                
            


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
