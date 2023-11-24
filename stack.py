from screens.trabajos import Trabajos
from screens.registrocliente import RegistroCliente
from screens.historial import Historial
from screens.inventario import Inventario
from screens.creditos import Creditos
import customtkinter as ctk

class PageStack(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.pack(side='right', fill='both', expand=True)

    @property  
    def stack(self) -> dict:
        """
        Aquí se tienen que agregar las pantallas que vayamos a crear

        Args:
            screen (string): El nombre de la clase de la pantalla
        """
                
        return {
                "Trabajos": Trabajos,
                "RegistroCliente": RegistroCliente,
                "Historial": Historial,
                "Inventario": Inventario,
                "Creditos": Creditos
                }
        
        
        
    def hide_pages(self):
        try:
            for frame in self.winfo_children():
                frame.destroy()
        except Exception as e:
            print("Error destroying screen from stack: ", e)
            
    def switch_page(self, screen):
        # Limpiando la pantalla para hacer el cambio
        self.hide_pages()
        
        # print(self.stack[screen])
        # Cambiando de pantalla
        Current_screen = self.stack[screen]
        Current_screen(self)