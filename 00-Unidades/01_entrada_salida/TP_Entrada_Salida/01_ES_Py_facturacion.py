import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Camila 
apellido: Lucero 
---
TP: ES_Facturaciones
---
Enunciado:
Para el departamento de facturación:
    A.	Ingresar tres precios de productos y mostrar la suma de los mismos.
    B.	Ingresar tres precios de productos y mostrar el promedio de los mismos.
	C.	ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Producto 1")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_importe_1 = customtkinter.CTkEntry(master=self)
        self.txt_importe_1.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Producto 2")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_importe_2 = customtkinter.CTkEntry(master=self)
        self.txt_importe_2.grid(row=1, column=1)

        self.label_3 = customtkinter.CTkLabel(master=self, text="Producto 3")
        self.label_3.grid(row=2, column=0, padx=20, pady=10)
        
        self.txt_importe_3 = customtkinter.CTkEntry(master=self)
        self.txt_importe_3.grid(row=2, column=1)
       
        self.btn_total = customtkinter.CTkButton(master=self, text="TOTAL", command=self.btn_total_on_click)
        self.btn_total.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_promedio = customtkinter.CTkButton(master=self, text="PROMEDIO", command=self.btn_promedio_on_click)
        self.btn_promedio.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_total_iva = customtkinter.CTkButton(master=self, text="TOTAL c/IVA", command=self.btn_total_iva_on_click)
        self.btn_total_iva.grid(row=5, pady=10, columnspan=2, sticky="nsew")

    def btn_total_on_click(self):
        producto_1=float(self.txt_importe_1.get())
        producto_2=float(self.txt_importe_2.get())
        producto_3=float(self.txt_importe_3.get())
        suma = producto_1 + producto_2 + producto_3 
        alert(title="Resultado", message="La suma del precio de los productos es de ${0} ".format(round(suma,2)))

    def btn_promedio_on_click(self):
        producto_1=float(self.txt_importe_1.get())
        producto_2=float(self.txt_importe_2.get())
        producto_3=float(self.txt_importe_3.get())
        promedio= (producto_1 + producto_2 + producto_3) / 3
        alert(title="Resultado", message="El promedio del precio de los productos es de ${0} ".format(round(promedio,2)))
        
    def btn_total_iva_on_click(self):
        producto_1=float(self.txt_importe_1.get())
        producto_2=float(self.txt_importe_2.get())
        producto_3=float(self.txt_importe_3.get())
        suma = producto_1 + producto_2 + producto_3 
        total_con_iva = suma + (suma * 0.21)
        alert(title="Resultado", message="El precio final con IVA (21%) es de ${0} ".format(round(total_con_iva,2)))
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()