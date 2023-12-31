import customtkinter as ctk
import colors
from components.header import Header
import controllers.postgres as pg
      
class Form(ctk.CTkFrame):
    def __init__(self, parent, args):
        super().__init__(parent)
        self.configure(fg_color=colors.white)
        
        info = dict(*args)
        
        ctk.CTkLabel(self, text="Descripcion", font=("Helvetica", 18)).pack()
        self.descripcion = ctk.CTkEntry(self,
                                     fg_color=colors.grey,
                                     border_width=1,
                                     corner_radius=7,
                                     width=350,
                                     height=80
                                     )
        self.descripcion.pack(pady=15)
        
        try:
            self.descripcion.insert(0, info['descripcion'])
        except:
            print("No descripcion")
        
        ctk.CTkLabel(self, text="Cantidad", font=("Helvetica", 18)).pack()
        self.cantidad = ctk.CTkEntry(self,
                                     fg_color=colors.grey,
                                     border_width=1,
                                     corner_radius=7,
                                     width=350,
                                     height=50
                                     )
        self.cantidad.pack(pady=15)
        
        try:
            self.cantidad.insert(0, info['cantidad'])
        except Exception as e:
            print("No cantidad: ", e)
        
        self.pack(padx=20, pady=20, anchor='nw')
    
    def getValues(self):
        # Devuelve los campos de texto
        return {
            "descripcion": self.descripcion,
            "cantidad": self.cantidad
        }


class NuevoInventarioFrame(ctk.CTkFrame):
    def __init__(self, parent, args):
        super().__init__(parent)
        self.configure(corner_radius=15, fg_color=colors.white)
        
        # Para consumir las "apis" y armar la conexión
        self.conn = pg.Connection()
        self.cursor = self.conn.cursor
        
        # Frame para la parte de la izquierda XD
        self.form = Form(self, args).getValues()
        self.pack(fill='both', expand=True, padx=20, pady=20)
        
    def getValues(self):
        return {**self.form}

class AgregarInventario(ctk.CTkFrame):
    def __init__(self, parent, change_page, *args): 
        super().__init__(parent)
        
        # Recuperando el ID de la cita si es que se desea editar un registro
        try:
            self.idinventario = dict(*args)['idinventario']
        except:
            self.idinventario = None
            
        # Para cambiar de pantalla
        self.change_page = change_page

        self.configure(corner_radius=0, fg_color=colors.grey)
        Header(self, "Agregar al inventario")
        
        # Para consumir las "apis" y armar la conexión
        self.conn = pg.Connection()
        self.cursor = self.conn.cursor
        
        fields = NuevoInventarioFrame(self, args).getValues()
        
        # Boton para registrar cita
        ctk.CTkButton(self,
                      width=250,
                      height=45,
                      text="Añadir",
                      fg_color=colors.darkbrown,
                      hover_color=colors.brown,
                      text_color=colors.white,
                      font=("Helvetica", 20, 'bold'),
                      command=lambda: self.sendInfo(fields)
        ).pack(pady=15, padx=20, side="bottom", anchor='center')
        
        self.pack(fill='both', expand=True)

    def sendInfo(self, fields):
        
            # Si es el caso de editar una cita
        if self.idinventario != None:
            return self.editInfo(fields)
        
        self.conn.postInventory((
            fields['descripcion'].get(),
            fields['cantidad'].get(),            
        ))
        
        # Cambia a la screen de inventario
        
        self.change_page("Inventario")
        
    def editInfo(self, fields):
        self.conn.putInventory(
            self.idinventario,
            (
            fields['descripcion'].get(),
            fields['cantidad'].get(),
        ))
        
          # Cambia a la screen de inventario
        
        self.change_page("Inventario")
