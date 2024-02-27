import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Camila
apellido: Lucero
---
Ejercicio: for_05
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. mostrar los números pares desde 
el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero = int (prompt("UTN","Ingrese un numero")) 
        contador_pares = 0
        numeros = ""
       
        for i in range (1,numero+1): #de 1 al numero ingresado 
           if i % 2 == 0: 
               numeros += f"{i} "
               contador_pares +=1
               
        alert("Pares", f"Los numeros pares encontrados son: {contador_pares}\n"
                        f"Estos son: {numeros}")           
       

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()