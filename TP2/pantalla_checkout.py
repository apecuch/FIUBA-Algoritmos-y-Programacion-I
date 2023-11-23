import tkinter as tk
import endpoints


def pantalla_checkout(venta:dict) -> None:
    
    total:float = 0.0
    total_entradas:float = 0.0
    total_snacks:float = 0.0
    
    window = tk.Tk(screenName='Pantalla Checkout')
    window.geometry("1280x720")
    window.configure(bg= '#2B2A33')
    window.title('>>> CHECKOUT')
    
    # Create a canvas for the window content
    canvas = tk.Canvas(window, bg= '#2B2A33')
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Add a scrollbar to the window
    scrollbar = tk.Scrollbar(canvas, command=canvas.yview)
    scrollbar.pack(side='right', fill='y')

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', canvas.configure(scrollregion=canvas.bbox('all')))

    # Create a frame to contain all elements
    main_frame = tk.Frame(canvas, bg= '#2B2A33')
    canvas.create_window((00,0), window=main_frame, anchor=tk.NW)
    
    # Titulo
    titulo_texto = ' 🛒 '
    titulo = tk.Label(main_frame, text = titulo_texto, font = ("Calibri", 50, "bold"), bg= '#2B2A33', fg = 'white', anchor='center')
    titulo.pack(pady = 15)   
    titulo_texto2 = ' RESUMEN DE COMPRA '
    titulo2 = tk.Label(main_frame, text = titulo_texto2, font = ("Calibri", 30, "bold"), bg= '#2B2A33', fg = 'white', anchor='center')
    titulo2.pack(pady = 15)
    
    # Entradas
    entradas_canvas = tk.Canvas(main_frame, bg= '#2B2A33')
    entradas_canvas.pack(side=tk.LEFT, fill=tk.NONE, expand=True)
    titulo_entradas_texto = ' ENTRADAS '
    titulo_entradas = tk.Label(entradas_canvas, text = titulo_entradas_texto, font = ("Calibri", 20, "bold"), bg = 'white', fg = 'black', anchor='center')
    titulo_entradas.pack(pady = 20)   
    titulo_pelicula_texto = venta['entradas'][0]
    titulo_pelicula = tk.Label(entradas_canvas, text = titulo_pelicula_texto, font = ("Calibri", 15, "underline"), bg= '#2B2A33', fg = 'white', anchor='center')
    titulo_pelicula.pack(pady = 5)
    titulo_cantidad_entradas_texto = "- Entradas: " + str(venta['entradas'][2])
    titulo_cantidad_entradas = tk.Label(entradas_canvas, text = titulo_cantidad_entradas_texto, font = ("Calibri", 10), bg= '#2B2A33', fg = 'white', anchor='center')
    titulo_cantidad_entradas.pack(pady = 5)   
    titulo_entradas_precio_texto = "- Precio Unitario: $" + str(venta['entradas'][1])
    titulo_entradas_precio = tk.Label(entradas_canvas, text = titulo_entradas_precio_texto, font = ("Calibri", 10), bg= '#2B2A33', fg = 'white', anchor='center')
    titulo_entradas_precio.pack(pady = 5)   
    
    total_entradas = venta['entradas'][1]*venta['entradas'][2]
    
    titulo_entradas_total_texto = "TOTAL ENTRADAS: $" + str(total_entradas)
    titulo_entradas_total = tk.Label(entradas_canvas, text = titulo_entradas_total_texto, font = ("Calibri", 13, "bold"), bg= '#2B2A33', fg = 'black', anchor='center')
    titulo_entradas_total.pack(pady = 5)  
    
    # Snacks
    snacks_canvas = tk.Canvas(main_frame, bg= '#2B2A33')
    snacks_canvas.pack(side=tk.RIGHT, fill=tk.NONE, expand=True)
    
    titulo_snacks_texto = ' SNACKS '
    titulo_snacks = tk.Label(snacks_canvas, text = titulo_snacks_texto, font = ("Calibri", 20, "bold"), bg = 'white', fg = 'black', anchor='center')
    titulo_snacks.pack(pady = 20)
    
    for snack in venta['snack']:
        titulo_snack_nombre_texto = "+ " + snack[0]
        titulo_snack_nombre = tk.Label(snacks_canvas, text = titulo_snack_nombre_texto, font = ("Calibri", 15, "bold"), bg= '#2B2A33', fg = 'white', anchor='center')
        titulo_snack_nombre.pack(pady = 10)
        titulo_cantidad_snack_texto = "Cantidad: " + str(snack[2])
        titulo_snack_entradas = tk.Label(snacks_canvas, text = titulo_cantidad_snack_texto, font = ("Calibri", 10), bg= '#2B2A33', fg = 'white', anchor='center')
        titulo_snack_entradas.pack(pady = 5)   
        titulo_entradas_precio_texto = "Precio: $" + str(snack[1]*snack[2])
        titulo_entradas_precio = tk.Label(snacks_canvas, text = titulo_entradas_precio_texto, font = ("Calibri", 10), bg= '#2B2A33', fg = 'white', anchor='center')
        titulo_entradas_precio.pack(pady = 5)
        
        total_snacks += snack[1]*snack[2]
        
    titulo_snacks_total_texto = "TOTAL SNACKS: $" + str(total_snacks)
    titulo_snacks_total = tk.Label(snacks_canvas, text = titulo_snacks_total_texto, font = ("Calibri", 13, "bold"), bg= '#2B2A33', fg = 'black', anchor='center')
    titulo_snacks_total.pack(pady = 5)  
    
    # Total
    total = total_entradas + total_snacks
    
    titulo_total_texto = ' TOTAL: $' + str(total)
    titulo_total = tk.Label(main_frame, text = titulo_total_texto, font = ("Calibri", 20, "bold"), bg = 'black', fg = 'white', anchor='center')
    titulo_total.pack(pady = 20)  
    
    boton_pagar = tk.Button(main_frame, text="PAGAR", command='Aca iria la funcion para crear el QR')
    boton_pagar.configure(
        relief=tk.RAISED,
        bd=3,
        font=('Calibri', 15, 'bold'),
        foreground='white',
        background='grey',
        padx=20,
        pady=5,
    )
    boton_pagar.pack(pady = 25)
    
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    
    window.mainloop()


venta:dict = {
    'entradas' : [ 'Mago de Oz', 1000, 2],
    'snack' : [ [ 'papitas', 500, 1], [ 'coca', 1500, 2], [ 'pochoclos', 500, 2] ]
}

pantalla_checkout(venta)
    