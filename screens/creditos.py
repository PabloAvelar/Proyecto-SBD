import customtkinter as ctk
import colors
from components.header import Header
import controllers.postgres as pg
from components.tabla_creditos import TablaCreditos, TablaCreditos


class Creditos(ctk.CTkFrame):
    def __init__(self, parent, change_page):
        super().__init__(parent)
        self.configure(corner_radius=0)
        # Cabecera con título
        Header(self, "Créditos")
        
        # Para cambiar de pantalla
        self.change_page = change_page
        
        ctk.CTkLabel(self, text="CREDITOS").pack()
        
        self.conn = pg.Connection()
        self.cursor = self.conn.cursor
        
        TablaCreditos(self)
    
        self.pack(fill='both', expand=True)
        