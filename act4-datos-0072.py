import pandas as pd
import matplotlib.pyplot as plt

## catherine rascon NC = 0072

# 1. Crear diccionario con datos de categorías de electrodomésticos
categorias_electro = {
    'id_categoria': [901, 902, 903, 904, 905, 906],
    'nombre_categoria': ['Refrigeracion', 'Lavado', 'Cocina', 'Climatizacion', 'Entretenimiento', 'Cuidado personal'],
    'descripcion': ['Refrigeradores y congeladores', 'Lavadoras y secadoras', 'Estufas y hornos', 'Aires acondicionados', 'TVs y Audio', 'Secadoras de pelo'],
    'cantidad_productos': [15, 10, 20, 8, 25, 12],
    'margen_ganancia_promedio': [15, 12, 18, 20, 10, 25],
    'producto_mas_vendido': ['Refrigerador 200L', 'Lavadora 15kg', 'Estufa 6Q', 'Minisplit 1T', 'Smart TV 50"', 'Secadora profesional'],
    'proveedor_principal': ['Mabe', 'Whirlpool', 'Iem', 'Carrier', 'Samsung', 'Philips'],
    'garantia_estandar_meses': [12, 12, 12, 12, 12, 6],
    'requiere_instalacion': [True, True, True, True, False, False],
    'estado_categoria': ['Activa', 'Activa', 'Activa', 'Activa', 'Activa', 'Activa']
}

print("Análisis Exploratorio de Datos, EDA")
print("Exploratory Data Analysis por catherine rascon NC = 0072")
print("5. Crear el diccionario con 10 listas y 6 elementos")

# 2. Convertir diccionario en DataFrame
df = pd.DataFrame(categorias_electro)

print("\n--- TABLA ORIGINAL DE CATEGORÍAS ---")
print(df)

# 3. Exportar los datos a CSV
print("-+-+-+ Convertir el DataFrame en archivo CSV -+-+-+")
df.to_csv(
    'categorias_electrodomesticos_0072.csv',
    index=False,
    encoding='utf-8-sig'
)

print("\nArchivo CSV creado correctamente")
print("+-+-+-+- 8. Leer los datos desde el archivo CSV +-+-+-+-")
print("categorias_electrodomesticos_0072.csv")

# 4. Leer el archivo CSV
df = pd.read_csv('categorias_electrodomesticos_0072.csv')

print("\n--- DATOS LEÍDOS DESDE CSV ---")
print(df)

print("+-+-+-+-+ 9. Análisis Exploratorio de Datos (EDA) +-+-+-+-+")

# 5. Primeros y últimos registros
print("+-+-+- PRIMEROS REGISTROS (Head):+-+-+-")
print(df.head(3))  # Muestra los primeros 3

print("+-+-+- ÚLTIMOS REGISTROS (Tail):+-+-+-")
print(df.tail(2))  # Muestra los últimos 2

# 6. Dimensiones y estructura
print("+-+-+- 6. Dimensiones y estructura +-+-+-")
print(df)

print("\n3. DIMENSIONES (Filas, Columnas):", df.shape)
print("\n4. NOMBRES DE COLUMNAS:\n", df.columns)
print("\n5. TIPOS DE DATOS:\n", df.dtypes)

# 7. Estadísticas y limpieza
print("+-+-+- 7. ESTADÍSTICAS DESCRIPTIVAS: +-+-+-")
print(df.describe())

print("\n8. VALORES FALTANTES (Nulls):")
print(df.isnull().sum())

print("\n9. REGISTROS DUPLICADOS:")
print(df.duplicated().sum())

print("\n10. VALORES ÚNICOS POR COLUMNA:")
print(df.nunique())

print("Categorías únicas:", df['nombre_categoria'].unique())

# 8. Análisis específico
print(df)
print("------------------------------------------")

print("+-+-+-+- CATEGORÍAS DE ELECTRODOMÉSTICOS: +-+-+-+-")
print(df['nombre_categoria'].value_counts())

print("\n12. PROMEDIO DEL MARGEN DE GANANCIA: ",
      df['margen_ganancia_promedio'].mean(), "%")

print("13. MARGEN DE GANANCIA MÁXIMO: ",
      df['margen_ganancia_promedio'].max(), "%")

print("14. MARGEN DE GANANCIA MÍNIMO: ",
      df['margen_ganancia_promedio'].min(), "%")

print("\nPROMEDIO DE PRODUCTOS POR CATEGORÍA:",
      df['cantidad_productos'].mean())

print("TOTAL DE PRODUCTOS:",
      df['cantidad_productos'].sum())

# 9. Ordenamiento, filtrado y agrupación
print("9. Ordenamiento, filtrado y agrupación")

print("-+-+-+-+- CATEGORÍAS ORDENADAS POR MARGEN DE GANANCIA (Mayor a menor):-+-+-+-+-")
print(df.sort_values(by='margen_ganancia_promedio', ascending=False))

print("+-+-+-+- CATEGORÍAS CON MARGEN DE GANANCIA MAYOR A 15%:+-+-+-+-")
filtro = df[df['margen_ganancia_promedio'] > 15]
print(filtro)

print("\n17. RESUMEN POR INSTALACIÓN:")
resumen = df.groupby('requiere_instalacion').agg(
    categorias=('id_categoria', 'count'),
    productos_totales=('cantidad_productos', 'sum'),
    margen_promedio=('margen_ganancia_promedio', 'mean'),
    margen_maximo=('margen_ganancia_promedio', 'max')
)
print(resumen)

# 18. Gráfica de barras: Productos por categoría
print("18. Gráfica de barras: Productos por categoría")

plt.figure(figsize=(8, 5))
plt.bar(df['nombre_categoria'], df['cantidad_productos'], color='skyblue')
plt.title('Cantidad de productos por categoría catherine 0072')
plt.xlabel('Categoría')
plt.ylabel('Cantidad de productos')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 19. Gráfica de barras: Margen de ganancia por categoría
print("19. Gráfica de barras: Margen de ganancia por categoría")

plt.figure(figsize=(8, 5))
plt.bar(df['nombre_categoria'], df['margen_ganancia_promedio'], color='lightgreen')
plt.title('Margen de ganancia por categoría EDA por catherine 0072')
plt.xlabel('Categoría')
plt.ylabel('Margen de ganancia (%)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 20. Histograma: Distribución de garantías
print("20. Histograma: Distribución de garantías")

plt.figure(figsize=(8, 5))
plt.hist(df['garantia_estandar_meses'], bins=5, color='orange', edgecolor='black')
plt.title('Distribución de garantías de categorías EDA por catherine 0072')
plt.xlabel('Garantía en meses')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 21. Gráfica de dispersión: Cantidad de productos vs margen de ganancia
print("21. Gráfica de dispersión: Cantidad de productos vs margen de ganancia")

plt.figure(figsize=(8, 5))
plt.scatter(df['cantidad_productos'], df['margen_ganancia_promedio'], color='red', s=100)
plt.title('Relación entre cantidad de productos y margen de ganancia EDA por catherine 0072')
plt.xlabel('Cantidad de productos')
plt.ylabel('Margen de ganancia (%)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 22. Diagrama de caja: Distribución de márgenes de ganancia
print("22. Diagrama de caja: Distribución de márgenes de ganancia")

plt.figure(figsize=(7, 5))
plt.boxplot(
    df['margen_ganancia_promedio'],
    patch_artist=True,
    boxprops=dict(facecolor='lightblue')
)
plt.title('Distribución de márgenes de ganancia (Boxplot) EDA por catherine 0072')
plt.ylabel('Margen de ganancia (%)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 23. Matriz de correlación
print("23. Matriz de correlación")

correlacion = df.corr(numeric_only=True)

print("\n--- MATRIZ DE CORRELACIÓN ---")
print(correlacion)

plt.figure(figsize=(9, 6))
plt.imshow(correlacion, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(correlacion.columns)), correlacion.columns, rotation=45)
plt.yticks(range(len(correlacion.columns)), correlacion.columns)
plt.title('Matriz de correlación de variables numéricas EDA por catherine 0072')
plt.tight_layout()
plt.show()

print("catherine huerta rascon NC = 0072")