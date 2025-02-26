import tkinter as tk
from tkinter import messagebox
from crud import create_user,read_users,update_user,delete_user

class CRUDApp:
    def __init__(self,root):
        self.root = root
        self.root.title("CRUD USUARIOS")

        #criação de WIDGETS
        self.create_widgets()
        
    def create_widgets(self):
        #Labels
        tk.Label(self.root,text="Nome: ").grid(row=0,column=0)
        tk.Label(self.root,text="telefone: ").grid(row=1,column=0)
        tk.Label(self.root,text="Email: ").grid(row=2,column=0)
        tk.Label(self.root,text="Usuario: ").grid(row=3,column=0)
        tk.Label(self.root,text="senha: ").grid(row=4,column=0)