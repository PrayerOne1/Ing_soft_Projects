import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Reservaciones - Hotel")
#root.geometry("500x800")
root.configure(bg="#f0f0f0")  # Fondo de la ventana principal

# Estilo para los botones y otros widgets
style = ttk.Style()
style.configure("TButton", font=("Arial", 10), padding=6)
style.configure("TLabel", font=("Arial", 10), background="#f0f0f0", padding=5)
style.configure("TNotebook", padding=10)
style.configure("TEntry", padding=5)
style.configure("TCombobox", padding=5)

# Crear los tabs
notebook = ttk.Notebook(root)
notebook.pack(pady=20, expand=True)

# Frame Clientes
frame_clientes = ttk.Frame(notebook)
frame_reservaciones = ttk.Frame(notebook)
frame_habitaciones = ttk.Frame(notebook)

# Agregar los tabs
notebook.add(frame_clientes, text="Clientes")
notebook.add(frame_reservaciones, text="Reservaciones")
notebook.add(frame_habitaciones, text="Habitaciones")

# ---------------------- Sección Clientes ----------------------

# Etiquetas y campos de entrada para Clientes
ttk.Label(frame_clientes, text="Ingrese Id del Cliente:").grid(row=0, column=0, padx=10, pady=10)
entry_cliente_buscar = ttk.Entry(frame_clientes)
entry_cliente_buscar.grid(row=0, column=1, padx=10)

ttk.Button(frame_clientes, text="Buscar", command=None).grid(row=0, column=2, padx=10)

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

# Botones para la sección de Clientes
ttk.Button(frame_clientes, text="Nuevo", command=None).grid(row=4, column=0, padx=10, pady=10)
ttk.Button(frame_clientes, text="Salvar", command=None).grid(row=4, column=1, padx=10, pady=10)
ttk.Button(frame_clientes, text="Cancelar", command=None).grid(row=4, column=2, padx=10, pady=10)
ttk.Button(frame_clientes, text="Editar", command=None).grid(row=4, column=3, padx=10, pady=10)
ttk.Button(frame_clientes, text="Eliminar", command=None).grid(row=4, column=4, padx=10, pady=10)

# ---------------------- Sección Reservaciones ----------------------

# Etiquetas y campos de entrada para Reservaciones
ttk.Label(frame_reservaciones, text="Ingrese Reservación:").grid(row=0, column=0, padx=10, pady=10)
entry_reservacion_buscar = ttk.Entry(frame_reservaciones)
entry_reservacion_buscar.grid(row=0, column=1)

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

# Botones para la sección de Reservaciones
ttk.Button(frame_reservaciones, text="Nueva Reservación", command=None).grid(row=5, column=0, padx=10, pady=10)
ttk.Button(frame_reservaciones, text="Reservar", command=None).grid(row=5, column=1, padx=10, pady=10)
ttk.Button(frame_reservaciones, text="Cancelar Reservación", command=None).grid(row=5, column=2, padx=10, pady=10)
ttk.Button(frame_reservaciones, text="Editar", command=None).grid(row=5, column=3, padx=10, pady=10)

# ---------------------- Sección Habitaciones ----------------------

# Etiquetas y campos de entrada para Habitaciones
ttk.Label(frame_habitaciones, text="Ingrese Número de Habitación:").grid(row=0, column=0, padx=10, pady=10)
entry_habitacion_buscar = ttk.Entry(frame_habitaciones)
entry_habitacion_buscar.grid(row=0, column=1)

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

# Botones para la sección de Habitaciones
ttk.Button(frame_habitaciones, text="Nueva Habitación", command=None).grid(row=4, column=0, padx=10, pady=10)
ttk.Button(frame_habitaciones, text="Editar", command=None).grid(row=4, column=1, padx=10, pady=10)

# Iniciar el loop principal de tkinter
root.mainloop()
