'''


'''

import tkinter as tk



window = tk.Tk(screenName='Pantalla Principal') # Inicio mi ventana

window.title('PANTALLA PRINCIPAL')

texto1 = tk.Label(window, text='Bienvenidos a Village cines!')
texto1.grid(row=0)

texto2 = tk.Label(window, text='Ingresa tu nombre: ')
texto2.grid(row=1)
opcion = tk.Entry(window)
opcion.grid(row=1, column=1)

def mostarTexto():
    
    texto2.configure(text = opcion.get())

tk.Button(window, text= "Submit",width= 20, command=mostarTexto).grid(row=1, column=2)

window.mainloop() # Mantengo la ventana abierta a espera de algun evento