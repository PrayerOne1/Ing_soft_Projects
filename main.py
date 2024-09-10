#  Libraries that we'll need and the use
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# Function to create users
def create_user(df: pd.DataFrame, filename: str) -> None:
    global data
    edit_btn.config(state="disabled")
    delete_btn.config(state="disabled")
    search_btn.config(state="disabled")

    #  Get the entries
    id_Entry = entry_id_cliente.get()
    nombre_entry = entry_nombre_cliente.get()
    direccion_entry = entry_direccion_cliente.get()
    telefono_entry = entry_telefono_cliente.get()
    email_entry = entry_email_cliente.get()

    if id_Entry and nombre_entry and direccion_entry and telefono_entry and email_entry:
        # Update the DataFrame
        data = {"ID": [id_Entry],
                "Nombre": [nombre_entry],
                "Direccion": [direccion_entry],
                "Telefono": [telefono_entry],
                "Email": [email_entry]}

        new_df = pd.DataFrame(data)
        table = pa.Table.from_pandas(new_df)
        pq.write_table(table, filename)

        messagebox.showinfo('Datos ingresados con éxito', 'Los datos fueron ingresados de manera exitosa')

        # Clean entries
        entry_nombre_cliente.delete(0, 'end')
        entry_id_cliente.delete(0, 'end')
        entry_direccion_cliente.delete(0, 'end')
        entry_telefono_cliente.delete(0, 'end')
        entry_email_cliente.delete(0, 'end')

        #  Just a little debug here
        print(data)
    else:
        messagebox.showerror('Error', 'Llene correctamente los datos seleccionados')

# Function to create new room
def create_room(df: pd.DataFrame, filename: str) -> None:
    global data
    hab_btn.config(state="disabled")
    edit_hab.config(state="disabled")

    # Get entries
    id_hab = entry_habitacion_id.get()
    room_entry = entry_numero_habitacion.get()
    status_entry = combo_estado_habitacion.get()

    if id_hab and room_entry and status_entry:
        # Upsate the  DataFrame
        data = {"ID habitacion": [id_hab],
                "Numero habitacion": [room_entry],
                "Estado": [status_entry]}

        new_df = pd.DataFrame(data)
        table = pa.Table.from_pandas(new_df)
        pq.write_table(table, filename)

        messagebox.showinfo('Datos ingresados con éxito', 'Los datos fueron ingresados de manera exitosa')

        # Clean entries
        entry_habitacion_id.delete(0, 'end')
        entry_numero_habitacion.delete(0, 'end')
        combo_estado_habitacion.set('') 

        #  Just a little debug here
        print(data)
    else:
        messagebox.showerror('Error', 'Llene correctamente los datos seleccionados')

# Create the main window
root = tk.Tk()
root.title("Sistema de Reservaciones - Hotel")
root.configure(bg="#f0f0f0")

# Style for the buttons and other widgets
style = ttk.Style()
style.configure("TButton", font=("Arial", 10), padding=6)
style.configure("TLabel", font=("Arial", 10), background="#f0f0f0", padding=5)
style.configure("TNotebook", padding=10)
style.configure("TEntry", padding=5)
style.configure("TCombobox", padding=5)

# Create the tabs
notebook = ttk.Notebook(root)
notebook.pack(pady=20, expand=True)

# Frame for each section
frame_clientes = ttk.Frame(notebook)
frame_reservaciones = ttk.Frame(notebook)
frame_habitaciones = ttk.Frame(notebook)

# Add tabs
notebook.add(frame_clientes, text="Clientes")
notebook.add(frame_reservaciones, text="Reservaciones")
notebook.add(frame_habitaciones, text="Habitaciones")

# ---------------------- Clients Section -----------------------------

# Tags and fields for the clients secition
ttk.Label(frame_clientes, text="Ingrese Id del Cliente:").grid(row=0, column=0, padx=10, pady=10)
entry_cliente_buscar = ttk.Entry(frame_clientes)
entry_cliente_buscar.grid(row=0, column=1, padx=10)

search_btn = ttk.Button(frame_clientes, text="Buscar", command=None)
search_btn.grid(row=0, column=2, padx=10)

ttk.Label(frame_clientes, text="ID:").grid(row=1, column=0, padx=10, pady=10)
entry_id_cliente = ttk.Entry(frame_clientes)
entry_id_cliente.grid(row=1, column=1)

ttk.Label(frame_clientes, text="Nombre:").grid(row=2, column=0, padx=10, pady=10)
entry_nombre_cliente = ttk.Entry(frame_clientes)
entry_nombre_cliente.grid(row=2, column=1)

ttk.Label(frame_clientes, text="Dirección:").grid(row=3, column=0, padx=10, pady=10)
entry_direccion_cliente = ttk.Entry(frame_clientes)
entry_direccion_cliente.grid(row=3, column=1)

ttk.Label(frame_clientes, text="Email:").grid(row=2, column=2, padx=10, pady=10)
entry_email_cliente = ttk.Entry(frame_clientes)
entry_email_cliente.grid(row=2, column=3)

ttk.Label(frame_clientes, text="Teléfono:").grid(row=3, column=2, padx=10, pady=10)
entry_telefono_cliente = ttk.Entry(frame_clientes)
entry_telefono_cliente.grid(row=3, column=3)

# Buttons for the clients section
new_btn = ttk.Button(frame_clientes, text="Nuevo", command=lambda: create_user(pd.DataFrame(), "clientes.parquet"))
new_btn.grid(row=4, column=0, padx=10, pady=10)
save_btn = ttk.Button(frame_clientes, text="Salvar", command=None)
save_btn.grid(row=4, column=1, padx=10, pady=10)
cancel_btn = ttk.Button(frame_clientes, text="Cancelar", command=None)
cancel_btn.grid(row=4, column=2, padx=10, pady=10)
edit_btn = ttk.Button(frame_clientes, text="Editar", command=None)
edit_btn.grid(row=4, column=3, padx=10, pady=10)
delete_btn = ttk.Button(frame_clientes, text="Eliminar", command=None)
delete_btn.grid(row=4, column=4, padx=10, pady=10)

# ---------------------- Reservation section ----------------------------

# Tags and fields for the reservations section
ttk.Label(frame_reservaciones, text="Ingrese Reservación:").grid(row=0, column=0, padx=10, pady=10)
entry_reservacion_buscar = ttk.Entry(frame_reservaciones)
entry_reservacion_buscar.grid(row=0, column=1, padx=10)

ttk.Button(frame_reservaciones, text="Buscar Reservación", command=None).grid(row=0, column=2, padx=10)

ttk.Label(frame_reservaciones, text="Reservación ID:").grid(row=1, column=0, padx=10, pady=10)
entry_reservacion_id = ttk.Entry(frame_reservaciones)
entry_reservacion_id.grid(row=1, column=1)

ttk.Label(frame_reservaciones, text="Cliente ID:").grid(row=2, column=0, padx=10, pady=10)
combo_cliente_id = ttk.Combobox(frame_reservaciones)
combo_cliente_id.grid(row=2, column=1)

ttk.Label(frame_reservaciones, text="Habitación ID:").grid(row=2, column=2, padx=10, pady=10)
combo_habitacion_id = ttk.Combobox(frame_reservaciones)
combo_habitacion_id.grid(row=2, column=3)

ttk.Label(frame_reservaciones, text="Fecha Reservación:").grid(row=3, column=0, padx=10, pady=10)
entry_fecha_reservacion = ttk.Entry(frame_reservaciones)
entry_fecha_reservacion.grid(row=3, column=1)

ttk.Label(frame_reservaciones, text="Fecha Salida:").grid(row=3, column=2, padx=10, pady=10)
entry_fecha_salida = ttk.Entry(frame_reservaciones)
entry_fecha_salida.grid(row=3, column=3)

ttk.Label(frame_reservaciones, text="Hora Reservación:").grid(row=4, column=0, padx=10, pady=10)
entry_hora_reservacion = ttk.Entry(frame_reservaciones)
entry_hora_reservacion.grid(row=4, column=1)

ttk.Label(frame_reservaciones, text="Costo:").grid(row=4, column=2, padx=10, pady=10)
entry_costo_reservacion = ttk.Entry(frame_reservaciones)
entry_costo_reservacion.grid(row=4, column=3)

# Buttons for reservation section
ttk.Button(frame_reservaciones, text="Nueva Reservación", command=None).grid(row=5, column=0, padx=10, pady=10)
ttk.Button(frame_reservaciones, text="Reservar", command=None).grid(row=5, column=1, padx=10, pady=10)
ttk.Button(frame_reservaciones, text="Cancelar Reservación", command=None).grid(row=5, column=2, padx=10, pady=10)
ttk.Button(frame_reservaciones, text="Editar", command=None).grid(row=5, column=3, padx=10, pady=10)

# ---------------------- Room section -----------------------------

# Tags and fields for the room section
ttk.Label(frame_habitaciones, text="Ingrese Número de Habitación:").grid(row=0, column=0, padx=10, pady=10)
entry_habitacion_buscar = ttk.Entry(frame_habitaciones)
entry_habitacion_buscar.grid(row=0, column=1, padx=10)

ttk.Button(frame_habitaciones, text="Buscar", command=None).grid(row=0, column=2, padx=10)

ttk.Label(frame_habitaciones, text="Habitación ID:").grid(row=1, column=0, padx=10, pady=10)
entry_habitacion_id = ttk.Entry(frame_habitaciones)
entry_habitacion_id.grid(row=1, column=1)

ttk.Label(frame_habitaciones, text="Número:").grid(row=2, column=0, padx=10, pady=10)
entry_numero_habitacion = ttk.Entry(frame_habitaciones)
entry_numero_habitacion.grid(row=2, column=1)

ttk.Label(frame_habitaciones, text="Estado:").grid(row=3, column=0, padx=10, pady=10)
combo_estado_habitacion = ttk.Combobox(frame_habitaciones, values=["Libre", "Reservado", "Cancelado"])
combo_estado_habitacion.grid(row=3, column=1)

# Buttons for the room section
hab_btn = ttk.Button(frame_habitaciones, text="Nueva Habitación", command=lambda: create_room(pd.DataFrame(), "habitaciones.parquet"))
hab_btn.grid(row=4, column=0, padx=10, pady=10)
edit_hab = ttk.Button(frame_habitaciones, text="Editar", command=None)
edit_hab.grid(row=4, column=1, padx=10, pady=10)

# Start the main loop
root.mainloop()
