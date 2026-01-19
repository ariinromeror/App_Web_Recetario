import sqlite3

def inicializar_recetario():
    conexion = sqlite3.connect('recetas_venezuela.db')
    cursor = conexion.cursor()

    cursor.execute('DROP TABLE IF EXISTS platos')
    
    cursor.execute('''
        CREATE TABLE platos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            categoria TEXT,
            ingredientes TEXT,
            instrucciones TEXT,
            imagen_url TEXT
        )
    ''')

    repertorio = [
        (
            "Arepa de Reina Pepiada", 
            "Clásicos", 
            "Harina de maíz, pollo esmechado, aguacate, mayonesa, cilantro.", 
            "Hacer la masa, asar la arepa. Mezclar pollo con aguacate y mayonesa para el relleno.",
            "https://www.recetasnestle.com.ve/sites/default/files/srh_recipes/5b4b8b0bb98418d6f77a4529a63ab570.jpg"
        ),
        (
            "Pabellón Criollo", 
            "Almuerzos", 
            "Arroz blanco, caraotas negras, carne esmechada, tajadas de plátano frito.", 
            "Cocinar cada elemento por separado. Servir de forma organizada en el plato.",
            "https://www.bekiacocina.com/images/cocina/0000/868-h.jpg"
        ),
        (
            "Cachapa con Queso", 
            "Especialidades", 
            "Maíz tierno molido, azúcar, una pizca de sal, queso de mano.", 
            "Cocinar la mezcla en un budare caliente hasta que dore. Rellenar con abundante queso.",
            "https://antojoscriollos.com/cdn/shop/products/Cachapa-wm.jpg?v=1700084053"
        )
    ]

    cursor.executemany('''
        INSERT INTO platos (nombre, categoria, ingredientes, instrucciones, imagen_url)
        VALUES (?, ?, ?, ?, ?)
    ''', repertorio)

    conexion.commit()
    conexion.close()
    print("✓ Base de datos actualizada con éxito.")

if __name__ == "__main__":
    inicializar_recetario()