 client =self.master.treeview.focus()
      campos =self.master.treeview.item(db.Cliente, "values")
      dni.insert(0, campos[0])
      dni.config(state=DISABLED)
      nombre.insert(0, campos[1])
      apellido.insert(0, campos[2])


      actualizar = Button(frame, text="Actualizar", command=self.edit_client)
      actualizar.grid(row=3, column = 0)
      Button(frame, text="Cancelar", command=self.close).grid(row=3, column=1)
      Button(frame, text="Modificar", command=self.edit).grid(row=0, column= 2)

      self.validaciones = [1, 1]
      self.actualizar = actualizar
      self.dni = dni
      self.nombre = nombre 
      self.apellido= apellido


   def edit_client(self):
        dni = self.dni_entry.get()
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()

        cliente = self.master.treeview.focus()
        self.master.treeview.item(cliente, values=(
           self.dni.get(), self.nombre.get(), self.apellido.get()))

       

        self.close()

        if not dni:
         messagebox.showerror("Error", "El DNI no puede estar vacío")
         return

        if not nombre:
         messagebox.showerror("Error", "El nombre no puede estar vacío")
         return

        if not apellido:
         messagebox.showerror("Error", "El apellido no puede estar vacío")
         return

        if not len(dni) == 9:
         messagebox.showerror("Error", "El DNI debe tener 9 caracteres")
         return

        if not dni[0].isalpha():
         messagebox.showerror("Error", "El DNI debe empezar por una letra")
         return

        for i in range(1, len(dni)):
         if not dni[i].isdigit():
           messagebox.showerror("Error", "El DNI debe contener solo números")
           return

        if not len(nombre) >= 2 and len(nombre) <= 30:
         messagebox.showerror("Error", "El nombre debe tener entre 2 y 30 caracteres")
         return

        if not len(apellido) >= 2 and len(apellido) <= 30:
         messagebox.showerror("Error", "El apellido debe tener entre 2 y 30 caracteres")
         return

         cliente = db.Cliente(dni, nombre, apellido)
         db.Clientes.insertar(cliente)
        self.close()

   def validate_dni(self, char):
       if not char.isdigit():
         return False
       return True

   def validate_nombre(self, char):
       if not char.isalnum():
         return False
       return True

   def validate_apellido(self, char):
       if not char.isalnum():
         return False
       return True
   
   def edit(self):
      if self.treeview.focus():
       EditClientWindow(self)

   def close(self):
       self.destroy()
       self.update()




       if index == 0:
         valido= helpers.dni_valido(valor, db.Clientes.lista)
         if valido:
            Event.widget.configure({"bg": "Green"})
         else:
            Event.widget.configure({"bg": "Red"})

       if index == 1:
         valido = len(valor) >= 2 and len(valor) <= 30 and valor.isalpha()
       if valido:
        Event.widget.configure({"bg": "Green"})
       else:
        Event.widget.configure({"bg": "Red"})

        self.validaciones[index] = valido
        self.crear.config(state=NORMAL if self.validaciones == [1, 1 , 1] else DISABLED)


class  EditClientWindow(Toplevel, CenterWidgetMixin):
   def __init__(self, parent):
      super().__init__(parent)
      self.title("Actualizar cliente")
      self.build()
      self.center()
      self.transient(parent)
      self.grab_set()

      









   




         
                                   

 
