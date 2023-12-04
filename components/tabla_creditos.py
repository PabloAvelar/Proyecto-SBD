import customtkinter as ctk
import colors

class TablaCredito(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(corner_radius=0, fg_color=colors.grey)
        
        # Encabezados de la tabla
        headers = ["ID Crédito", "ID Cliente", "Fecha", "Límite de Pago", "Total", "Restante"]
        
        # Crear etiquetas para los encabezados
        for col, header in enumerate(headers):
            etiqueta = ctk.CTkLabel(self, text=header, width=30, text_color=colors.darkbrown, font=("Helvetica", 18, "bold"))
            etiqueta.grid(row=0, column=col, sticky='wn')

            fetch_credito = parent.conn.getCredits()  # Reemplaza con la función adecuada de postgres.py

        # Organizar los datos
        data = [(
            credito['idcredito'],
            credito['idcliente'],
            credito['fecha'],
            credito['limitepago'],
            "$"+str(credito['totalapagar']),
            ("$"+(str(credito['restante']) if credito['restante'] != None else str(credito['totalapagar']))
            
            ))
            for credito in fetch_credito]

        # Mostrar datos en la tabla
        for i, fila in enumerate(data, start=1):
            for j, valor in enumerate(fila):
                etiqueta = ctk.CTkLabel(self, text=str(valor), font=("Helvetica", 16))
                etiqueta.grid(row=i, column=j, sticky='w')

        # Ajustar el tamaño de las columnas
        self.grid_columnconfigure(0, weight=1)  # ID Crédito
        self.grid_columnconfigure(1, weight=1)  # ID Cliente
        self.grid_columnconfigure(2, weight=1)  # Fecha
        self.grid_columnconfigure(3, weight=1)  # Límite de Pago
        self.grid_columnconfigure(4, weight=1)  # Límite de Pago
        self.grid_columnconfigure(5, weight=1)  # Límite de Pago

        self.pack(expand=True, fill='both', anchor='ne')
