import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def cargar_ids_cliente():
    try:
        with open("clientes.txt", "r") as file:
            clientes = [line.strip().split(',')[0] for line in file if line.strip()]
            return clientes
    except FileNotFoundError:
        messagebox.showerror('Error', 'El archivo de clientes no se encuentra.')
        return []

def cargar_ids_habitacion():
    try:
        with open("habitaciones.txt", "r") as file:
            habitaciones = [line.strip().split(',')[0] for line in file if line.strip()]
            return habitaciones
    except FileNotFoundError:
        messagebox.showerror('Error', 'El archivo de habitaciones no se encuentra.')
        return []

def actualizar_combos():
    # Cargar los IDs desde los archivos
    cliente_ids = cargar_ids_cliente()
    habitacion_ids = cargar_ids_habitacion()

    # Actualizar los combos
    combo_cliente_id['values'] = cliente_ids
    combo_habitacion_id['values'] = habitacion_ids


def agregar_cliente(id_cliente, nombre, direccion, email, telefono):
    with open("clientes.txt", "a") as file:
        file.write(f"{id_cliente},{nombre},{direccion},{email},{telefono}\n")
    print(f"Cliente {nombre} agregado con éxito.")
    
def id_cliente_existe(id_cliente):
    # Verificar que id_cliente no esté vacío
    if not id_cliente:
        return False
    
    try:
        with open("clientes.txt", "r") as file:
            for line in file:
                fields = line.strip().split(',')
                if len(fields) < 5:
                    continue  # Saltar líneas que no tienen el formato esperado
                
                existing_id = fields[0]
                if existing_id == id_cliente:
                    return True
    except FileNotFoundError:
        # El archivo no existe, lo que significa que no hay clientes registrados
        return False
    
    return False


def buscar_cliente_por_nombre(nombre):
    with open("clientes.txt", "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue  # Saltar líneas vacías
            
            fields = line.split(',')
            if len(fields) < 5:
                continue  # Saltar líneas que no tienen el formato esperado
            
            id_cliente, nombre_cliente, direccion, email, telefono = fields
            if nombre_cliente.lower() == nombre.lower():
                return id_cliente, nombre_cliente, direccion, email, telefono
    
    return None



def editar_cliente(id_cliente, nombre=None, direccion=None, email=None, telefono=None):
    lines = []
    with open("clientes.txt", "r") as file:
        for line in file:
            fields = line.strip().split(',')
            if fields[0] == id_cliente:
                if nombre: fields[1] = nombre
                if direccion: fields[2] = direccion
                if email: fields[3] = email
                if telefono: fields[4] = telefono
            lines.append(','.join(fields))
    with open("clientes.txt", "w") as file:
        file.write('\n'.join(lines) + '\n')
    print(f"Cliente con ID {id_cliente} actualizado.")


def eliminar_cliente(id_cliente):
    lines = []
    with open("clientes.txt", "r") as file:
        for line in file:
            fields = line.strip().split(',')
            if fields[0] != id_cliente:
                lines.append(','.join(fields))
    with open("clientes.txt", "w") as file:
        file.write('\n'.join(lines) + '\n')
    print(f"Cliente con ID {id_cliente} eliminado.")

def id_habitacion_existe(id_habitacion):
    with open("habitaciones.txt", "r") as file:
        for line in file:
            fields = line.strip().split(',')
            if fields[0] == id_habitacion:
                return True
    return False

def agregar_habitacion(id_habitacion, numero_habitacion):
    with open("habitaciones.txt", "a") as file:
        file.write(f"{id_habitacion},{numero_habitacion},Libre\n")
    print(f"Habitación {numero_habitacion} agregada con éxito.")


def buscar_habitacion_por_numero(numero_habitacion):
    with open("habitaciones.txt", "r") as file:
        for line in file:
            id_habitacion, numero, estado = line.strip().split(',')
            if id_habitacion == numero_habitacion:
                return id_habitacion, numero, estado
    return None



def editar_habitacion(id_habitacion, numero_habitacion=None, estado=None):
    lines = []
    with open("habitaciones.txt", "r") as file:
        for line in file:
            fields = line.strip().split(',')
            if fields[0] == id_habitacion:
                if numero_habitacion:
                    fields[1] = numero_habitacion
                if estado:
                    fields[2] = estado
            lines.append(','.join(fields))
    with open("habitaciones.txt", "w") as file:
        file.write('\n'.join(lines) + '\n')


def agregar_reservacion(id_reservacion, id_cliente, id_habitacion, fecha_reservacion, hora_reservacion, fecha_salida, costo):
    with open("reservaciones.txt", "a") as file:
        file.write(f"{id_reservacion},{id_cliente},{id_habitacion},{fecha_reservacion},{hora_reservacion},{fecha_salida},{costo}\n")
    print(f"Reservación ID {id_reservacion} registrada con éxito.")


def buscar_reservacion_por_id(id_reservacion_buscar):
    try:
        with open("reservaciones.txt", "r") as file:
            for line in file:
                if line.strip():
                    parts = line.strip().split(',')
                    if len(parts) == 7:
                        id_reservacion, id_cliente, id_habitacion, fecha_reservacion, hora_reservacion, fecha_salida, costo = parts
                        if id_reservacion == id_reservacion_buscar:
                            # Buscar el nombre del cliente en el archivo de clientes
                            cliente_nombre_resultado = None
                            with open("clientes.txt", "r") as cliente_file:
                                for cliente_line in cliente_file:
                                    if cliente_line.strip():
                                        cliente_parts = cliente_line.strip().split(',')
                                        if len(cliente_parts) == 5:
                                            cliente_id, cliente_nombre, _, _, _ = cliente_parts
                                            if cliente_id == id_cliente:
                                                cliente_nombre_resultado = cliente_nombre
                                                break

                            # Buscar el número de la habitación en el archivo de habitaciones
                            numero_habitacion_resultado = None
                            with open("habitaciones.txt", "r") as habitacion_file:
                                for habitacion_line in habitacion_file:
                                    if habitacion_line.strip():
                                        habitacion_parts = habitacion_line.strip().split(',')
                                        if len(habitacion_parts) == 3:
                                            habitacion_id, numero_habitacion, _ = habitacion_parts
                                            if habitacion_id == id_habitacion:
                                                numero_habitacion_resultado = numero_habitacion
                                                break

                            if cliente_nombre_resultado and numero_habitacion_resultado:
                                return {
                                    "id_reservacion": id_reservacion,
                                    "cliente_nombre": cliente_nombre_resultado,
                                    "habitacion_numero": numero_habitacion_resultado,
                                    "fecha_reservacion": fecha_reservacion,
                                    "hora_reservacion": hora_reservacion,
                                    "fecha_salida": fecha_salida,
                                    "costo": costo
                                }
                            else:
                                return None
        return None
    except FileNotFoundError as e:
        print(f"Error al abrir el archivo: {e}")
        return None




def editar_reservacion(id_reservacion, id_cliente=None, id_habitacion=None, fecha_reservacion=None, hora_reservacion=None, fecha_salida=None, costo=None):
    lines = []
    with open("reservaciones.txt", "r") as file:
        for line in file:
            fields = line.strip().split(',')
            if fields[0] == id_reservacion:
                if id_cliente: fields[1] = id_cliente
                if id_habitacion: fields[2] = id_habitacion
                if fecha_reservacion: fields[3] = fecha_reservacion
                if hora_reservacion: fields[4] = hora_reservacion
                if fecha_salida: fields[5] = fecha_salida
                if costo: fields[6] = costo
            lines.append(','.join(fields))
    with open("reservaciones.txt", "w") as file:
        file.write('\n'.join(lines) + '\n')
    print(f"Reservación con ID {id_reservacion} actualizada.")

def eliminar_reservacion(id_reservacion):
    lines = []
    with open("reservaciones.txt", "r") as file:
        for line in file:
            fields = line.strip().split(',')
            if fields[0] != id_reservacion:
                lines.append(','.join(fields))
            else:
                # Liberar la habitación
                with open("habitaciones.txt", "r") as habitacion_file:
                    habitacion_lines = []
                    for habitacion_line in habitacion_file:
                        habitacion_fields = habitacion_line.strip().split(',')
                        if habitacion_fields[0] == fields[2]:
                            habitacion_fields[2] = "Libre"
                        habitacion_lines.append(','.join(habitacion_fields))
                with open("habitaciones.txt", "w") as habitacion_file:
                    habitacion_file.write('\n'.join(habitacion_lines) + '\n')
    with open("reservaciones.txt", "w") as file:
        file.write('\n'.join(lines) + '\n')
    print(f"Reservación con ID {id_reservacion} eliminada y habitación liberada.")


def on_agregar_cliente():
    id_cliente = entry_id_cliente.get()
    nombre = entry_nombre_cliente.get()
    direccion = entry_direccion_cliente.get()
    email = entry_email_cliente.get()
    telefono = entry_telefono_cliente.get()
    
    if id_cliente and nombre and direccion and email and telefono:
        if id_cliente_existe(id_cliente):
            messagebox.showerror('Error', 'El ID de cliente ya existe.')
            entry_id_cliente.delete(0, tk.END)
        else:
            agregar_cliente(id_cliente, nombre, direccion, email, telefono)
            
            # Limpiar los campos de entrada
            entry_id_cliente.delete(0, tk.END)
            entry_nombre_cliente.delete(0, tk.END)
            entry_direccion_cliente.delete(0, tk.END)
            entry_email_cliente.delete(0, tk.END)
            entry_telefono_cliente.delete(0, tk.END)
                
            # Mostrar mensaje de éxito si el cliente fue agregado
            messagebox.showinfo('Datos ingresados con éxito', 'Los datos fueron ingresados de manera exitosa')
    else:
        # Mostrar mensaje de error si no se completan todos los campos
        messagebox.showerror('Error', 'Llene correctamente los datos seleccionados')


def on_buscar_cliente_por_nombre():
    nombre = entry_cliente_buscar.get()
    if nombre:
        resultado = buscar_cliente_por_nombre(nombre)
        if resultado:
            id_cliente, nombre_cliente, direccion, email, telefono = resultado
            entry_id_cliente.delete(0, tk.END)
            entry_id_cliente.insert(0, id_cliente)
            entry_nombre_cliente.delete(0, tk.END)
            entry_nombre_cliente.insert(0, nombre_cliente)
            entry_direccion_cliente.delete(0, tk.END)
            entry_direccion_cliente.insert(0, direccion)
            entry_email_cliente.delete(0, tk.END)
            entry_email_cliente.insert(0, email)
            entry_telefono_cliente.delete(0, tk.END)
            entry_telefono_cliente.insert(0, telefono)
        else:
            messagebox.showinfo('Resultado', 'Cliente no encontrado.')
    else:
        messagebox.showerror('Error', 'Ingrese el nombre del cliente para buscar')

def on_editar_cliente():
    id_cliente = entry_id_cliente.get()
    nombre = entry_nombre_cliente.get()
    direccion = entry_direccion_cliente.get()
    email = entry_email_cliente.get()
    telefono = entry_telefono_cliente.get()
    
    if id_cliente and (nombre or direccion or email or telefono):
        editar_cliente(id_cliente, nombre, direccion, email, telefono)
        messagebox.showinfo('Datos actualizados', 'Los datos del cliente fueron actualizados con éxito')
        # Limpiar los campos de entrada
        entry_id_cliente.delete(0, tk.END)
        entry_nombre_cliente.delete(0, tk.END)
        entry_direccion_cliente.delete(0, tk.END)
        entry_email_cliente.delete(0, tk.END)
        entry_telefono_cliente.delete(0, tk.END)

    else:
        messagebox.showerror('Error', 'Ingrese el ID del cliente y al menos un dato para actualizar')

def on_eliminar_cliente():
    id_cliente = entry_id_cliente.get()
    if id_cliente:
        eliminar_cliente(id_cliente)
        messagebox.showinfo('Cliente eliminado', 'El cliente fue eliminado con éxito')
        # Limpiar los campos de entrada
        entry_cliente_buscar.delete(0, tk.END)
        entry_id_cliente.delete(0, tk.END)
        entry_nombre_cliente.delete(0, tk.END)
        entry_direccion_cliente.delete(0, tk.END)
        entry_email_cliente.delete(0, tk.END)
        entry_telefono_cliente.delete(0, tk.END)
    else:
        messagebox.showerror('Error', 'Ingrese el ID del cliente para eliminar')

def on_buscar_habitacion_por_numero():
    numero = entry_habitacion_buscar.get()
    if numero:
        resultado = buscar_habitacion_por_numero(numero)
        if resultado:
            id_habitacion, numero, estado = resultado
            entry_habitacion_id.delete(0, tk.END)
            entry_habitacion_id.insert(0, id_habitacion)
            entry_numero_habitacion.delete(0, tk.END)
            entry_numero_habitacion.insert(0, numero)
            combo_estado_habitacion.set(estado)
        else:
            messagebox.showinfo('Resultado', 'Habitación no encontrada.')
    else:
        messagebox.showerror('Error', 'Ingrese el número de habitación para buscar')


def on_editar_habitacion():
    id_habitacion = entry_habitacion_id.get()
    numero_habitacion = entry_numero_habitacion.get()
    estado = combo_estado_habitacion.get()

    if id_habitacion and (numero_habitacion or estado):
        editar_habitacion(id_habitacion, numero_habitacion, estado)
        messagebox.showinfo('Datos actualizados', 'Los datos de la habitación fueron actualizados con éxito')
        
        # Actualizar campos para reflejar los cambios en pantalla
        entry_numero_habitacion.delete(0, tk.END)
        combo_estado_habitacion.set('')
    else:
        messagebox.showerror('Error', 'Ingrese el ID de la habitación y al menos un dato para actualizar')

def id_reservacion_existe(id_reservacion):
    try:
        with open("reservaciones.txt", "r") as file:
            for line in file:
                if line.strip():
                    parts = line.strip().split(',')
                    if len(parts) == 7:
                        existing_id = parts[0]
                        if existing_id == id_reservacion:
                            return True
        return False
    except FileNotFoundError as e:
        print(f"Error al abrir el archivo: {e}")
        return False

def on_agregar_reservacion():
    id_reservacion = entry_reservacion_id.get()
    id_cliente = combo_cliente_id.get()
    id_habitacion = combo_habitacion_id.get()
    fecha_reservacion = entry_fecha_reservacion.get()
    hora_reservacion = entry_hora_reservacion.get()
    fecha_salida = entry_fecha_salida.get()
    costo = entry_costo_reservacion.get()
    
    if id_reservacion and id_cliente and id_habitacion and fecha_reservacion and hora_reservacion and fecha_salida and costo:
        if id_reservacion_existe(id_reservacion):
            messagebox.showerror('Error', 'El ID de la reservación ya existe. Por favor, use otro ID.')
        else:
            agregar_reservacion(id_reservacion, id_cliente, id_habitacion, fecha_reservacion, hora_reservacion, fecha_salida, costo)
            # Cambiar el estado de la habitación a "Reservado"
            editar_habitacion(id_habitacion, estado="Reservado")
            messagebox.showinfo('Reservación registrada', 'La reservación fue registrada con éxito')
            
            entry_reservacion_id.delete(0, tk.END)
            combo_cliente_id.delete(0, tk.END)
            combo_habitacion_id.delete(0, tk.END)
            entry_fecha_reservacion.delete(0, tk.END)
            entry_hora_reservacion.delete(0, tk.END)
            entry_fecha_salida.delete(0, tk.END)
            entry_costo_reservacion.delete(0, tk.END)
    else:
        messagebox.showerror('Error', 'Ingrese todos los datos para la reservación')


def on_buscar_reservacion_por_nombre():
    id_reservacion = entry_reservacion_buscar.get()
    if id_reservacion:
        resultado = buscar_reservacion_por_id(id_reservacion)
        if resultado:
            entry_reservacion_id.delete(0, tk.END)
            entry_reservacion_id.insert(0, resultado["id_reservacion"])
            combo_cliente_id.delete(0, tk.END)
            combo_cliente_id.insert(0, resultado["cliente_nombre"])
            combo_habitacion_id.delete(0, tk.END)
            combo_habitacion_id.insert(0, resultado["habitacion_numero"])
            entry_fecha_reservacion.delete(0, tk.END)
            entry_fecha_reservacion.insert(0, resultado["fecha_reservacion"])
            entry_hora_reservacion.delete(0, tk.END)
            entry_hora_reservacion.insert(0, resultado["hora_reservacion"])
            entry_fecha_salida.delete(0, tk.END)
            entry_fecha_salida.insert(0, resultado["fecha_salida"])
            entry_costo_reservacion.delete(0, tk.END)
            entry_costo_reservacion.insert(0, resultado["costo"])
        else:
            messagebox.showinfo('Resultado', 'Reservación no encontrada.')
    else:
        messagebox.showerror('Error', 'Ingrese el ID de la reservación para buscar')
        

def obtener_habitacion_actual(id_reservacion):
    """Función para obtener el ID de la habitación actual de la reservación."""
    try:
        with open("reservaciones.txt", "r") as file:
            for line in file:
                if line.strip():
                    parts = line.strip().split(',')
                    if len(parts) == 7:
                        reservacion_id, id_cliente, id_habitacion, fecha_reservacion, hora_reservacion, fecha_salida, costo = parts
                        if reservacion_id == id_reservacion:
                            return id_habitacion
    except FileNotFoundError:
        return None
    return None

def on_editar_reservacion():
    id_reservacion = entry_reservacion_id.get()
    id_cliente = combo_cliente_id.get()
    id_habitacion_nueva = combo_habitacion_id.get()  # Nueva habitación seleccionada
    fecha_reservacion = entry_fecha_reservacion.get()
    hora_reservacion = entry_hora_reservacion.get()
    fecha_salida = entry_fecha_salida.get()
    costo = entry_costo_reservacion.get()
    
    if id_reservacion:
        # Obtener la habitación actual antes de editar
        id_habitacion_actual = obtener_habitacion_actual(id_reservacion)
        
        if id_habitacion_actual and id_habitacion_nueva:
            # Editar la reservación
            editar_reservacion(id_reservacion, id_cliente, id_habitacion_nueva, fecha_reservacion, hora_reservacion, fecha_salida, costo)
            
            # Cambiar el estado de la nueva habitación a "Reservado"
            editar_habitacion(id_habitacion_nueva, estado="Reservado")
            
            # Cambiar el estado de la habitación anterior a "Libre"
            if id_habitacion_actual != id_habitacion_nueva:
                editar_habitacion(id_habitacion_actual, estado="Libre")
            
            # Mostrar mensaje de éxito
            messagebox.showinfo('Datos actualizados', 'Los datos de la reservación fueron actualizados con éxito')
            
            # Limpiar los campos de entrada
            entry_reservacion_id.delete(0, tk.END)
            combo_cliente_id.delete(0, tk.END)
            combo_habitacion_id.delete(0, tk.END)
            entry_fecha_reservacion.delete(0, tk.END)
            entry_hora_reservacion.delete(0, tk.END)
            entry_fecha_salida.delete(0, tk.END)
            entry_costo_reservacion.delete(0, tk.END)
        else:
            messagebox.showerror('Error', 'No se pudo encontrar la habitación actual o la nueva habitación no es válida')
    else:
        messagebox.showerror('Error', 'Ingrese el ID de la reservación para actualizar')


def on_eliminar_reservacion():
    id_reservacion = entry_reservacion_id.get()
    id_habitacion = combo_habitacion_id.get()
    if id_reservacion:
        editar_habitacion(id_habitacion, estado="Libre")
        eliminar_reservacion(id_reservacion)
        messagebox.showinfo('Reservación eliminada', 'La reservación fue eliminada con éxito')
        entry_reservacion_id.delete(0, tk.END)
        combo_cliente_id.delete(0, tk.END)
        combo_habitacion_id.delete(0, tk.END)
        entry_fecha_reservacion.delete(0, tk.END)
        entry_hora_reservacion.delete(0, tk.END)
        entry_fecha_salida.delete(0, tk.END)
        entry_costo_reservacion.delete(0, tk.END)
        entry_reservacion_buscar.delete(0, tk.END)
    else:
        messagebox.showerror('Error', 'Ingrese el ID de la reservación para eliminar')

def on_registrar_nueva_habitacion():
    id_habitacion = entry_habitacion_id.get()
    numero_habitacion = entry_numero_habitacion.get()
    estado = combo_estado_habitacion.get()
    
    if id_habitacion and numero_habitacion and estado:
        if id_habitacion_existe(id_habitacion):
            messagebox.showerror('Error', 'La ID de habitación ya existe.')
        else:
            # Agregar la habitación al archivo
            agregar_habitacion(id_habitacion, numero_habitacion)
            
            # Limpiar los campos de entrada
            entry_habitacion_id.delete(0, tk.END)
            entry_numero_habitacion.delete(0, tk.END)
            combo_estado_habitacion.set('')
    
            # Mostrar mensaje de éxito
            messagebox.showinfo('Éxito', f'Habitación {numero_habitacion} registrada con éxito.')
    else:
        # Mostrar mensaje de error si los campos no están completos
        messagebox.showerror('Error', 'Por favor, complete todos los campos.')
        
def on_clean_cliente ():
    entry_cliente_buscar.delete(0, tk.END)
    entry_id_cliente.delete(0, tk.END)
    entry_nombre_cliente.delete(0, tk.END)
    entry_direccion_cliente.delete(0, tk.END)
    entry_email_cliente.delete(0, tk.END)
    entry_telefono_cliente.delete(0, tk.END)
def on_clean_Reservaciones ():    
        entry_reservacion_id.delete(0, tk.END)
        combo_cliente_id.delete(0, tk.END)
        combo_habitacion_id.delete(0, tk.END)
        entry_fecha_reservacion.delete(0, tk.END)
        entry_hora_reservacion.delete(0, tk.END)
        entry_fecha_salida.delete(0, tk.END)
        entry_costo_reservacion.delete(0, tk.END)
        entry_reservacion_buscar.delete(0, tk.END)

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Reservaciones - Hotel")
root.geometry("780x400")
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
ttk.Button(frame_clientes, text="Buscar", command=on_buscar_cliente_por_nombre).grid(row=0, column=2, padx=10)
ttk.Button(frame_clientes, text="Nuevo", command=on_clean_cliente).grid(row=4, column=0, padx=10, pady=10)
ttk.Button(frame_clientes, text="Salvar", command=on_agregar_cliente).grid(row=4, column=1, padx=10, pady=10)
ttk.Button(frame_clientes, text="Cancelar", command=on_clean_cliente).grid(row=4, column=2, padx=10, pady=10)
ttk.Button(frame_clientes, text="Editar", command=on_editar_cliente).grid(row=4, column=3, padx=10, pady=10)
ttk.Button(frame_clientes, text="Eliminar", command=on_eliminar_cliente).grid(row=4, column=4, padx=10, pady=10)

# ---------------------- Sección Reservaciones ----------------------

# Etiquetas y campos de entrada para Reservaciones
ttk.Label(frame_reservaciones, text="Ingrese Reservación:").grid(row=0, column=0, padx=10, pady=10)
entry_reservacion_buscar = ttk.Entry(frame_reservaciones)
entry_reservacion_buscar.grid(row=0, column=1)


ttk.Label(frame_reservaciones, text="Reservación ID:").grid(row=1, column=0, padx=10, pady=10)
entry_reservacion_id = ttk.Entry(frame_reservaciones)
entry_reservacion_id.grid(row=1, column=1)

ttk.Label(frame_reservaciones, text="Cliente ID:").grid(row=2, column=0, padx=10, pady=10)
combo_cliente_id = ttk.Combobox(frame_reservaciones)
combo_cliente_id.grid(row=2, column=1)

ttk.Label(frame_reservaciones, text="Habitación ID:").grid(row=2, column=2, padx=10, pady=10)
combo_habitacion_id = ttk.Combobox(frame_reservaciones)
combo_habitacion_id.grid(row=2, column=3)


actualizar_combos()

ttk.Label(frame_reservaciones, text="Fecha Reservación (YYYY-MM-DD):").grid(row=3, column=0, padx=10, pady=10)
entry_fecha_reservacion = ttk.Entry(frame_reservaciones)
entry_fecha_reservacion.grid(row=3, column=1)

ttk.Label(frame_reservaciones, text="Fecha Salida (YYYY-MM-DD):").grid(row=3, column=2, padx=10, pady=10)
entry_fecha_salida = ttk.Entry(frame_reservaciones)
entry_fecha_salida.grid(row=3, column=3)

ttk.Label(frame_reservaciones, text="Hora Reservación:").grid(row=4, column=0, padx=10, pady=10)
entry_hora_reservacion = ttk.Entry(frame_reservaciones)
entry_hora_reservacion.grid(row=4, column=1)

ttk.Label(frame_reservaciones, text="Costo:").grid(row=4, column=2, padx=10, pady=10)
entry_costo_reservacion = ttk.Entry(frame_reservaciones)
entry_costo_reservacion.grid(row=4, column=3)
# Botones para la sección de Reservaciones
ttk.Button(frame_reservaciones, text="Buscar Reservación", command=on_buscar_reservacion_por_nombre).grid(row=0, column=2, padx=10)
ttk.Button(frame_reservaciones, text="Nueva Reservación", command=on_clean_Reservaciones).grid(row=5, column=0, padx=10, pady=10)
ttk.Button(frame_reservaciones, text="Reservar", command=on_agregar_reservacion).grid(row=5, column=1, padx=10, pady=10)
ttk.Button(frame_reservaciones, text="Cancelar Reservación", command=on_eliminar_reservacion).grid(row=5, column=2, padx=10, pady=10)
ttk.Button(frame_reservaciones, text="Editar", command=on_editar_reservacion).grid(row=5, column=3, padx=10, pady=10)

# ---------------------- Sección Habitaciones ----------------------

# Etiquetas y campos de entrada para Habitaciones
ttk.Label(frame_habitaciones, text="Ingrese Número de Habitación:").grid(row=0, column=0, padx=10, pady=10)
entry_habitacion_buscar = ttk.Entry(frame_habitaciones)
entry_habitacion_buscar.grid(row=0, column=1)


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
ttk.Button(frame_habitaciones, text="Buscar", command=on_buscar_habitacion_por_numero).grid(row=0, column=2, padx=10)
ttk.Button(frame_habitaciones, text="Nueva Habitación", command=on_registrar_nueva_habitacion).grid(row=4, column=0, padx=10, pady=10)
ttk.Button(frame_habitaciones, text="Editar", command=on_editar_habitacion).grid(row=4, column=1, padx=10, pady=10)






# Iniciar el loop principal de tkinter
root.mainloop()
