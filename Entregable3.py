import pandas as pd
import networkx as nx

# Leer el archivo base.txt
file_path = 'baseconocimientos.txt'
data = pd.read_csv(file_path)

# Crear el DataFrame con las conexiones y tiempos de viaje
df = pd.DataFrame({
    'Estaciones': data['Origen'],
    'Destinos': data['Destino'],
    'Tiempo_Viaje': data['Paradas'].apply(lambda x: len(x.split('-')) - 1)  # Asumimos que cada parada toma 1 minuto
})

# Crear un DataFrame para mostrar las rutas de transporte con tiempos de viaje
timedf = df.copy()
timedf['Tiempo_Viaje'] = timedf['Tiempo_Viaje'].astype(str) + ' minutos'


# Crear un grafo desde el DataFrame
G = nx.from_pandas_edgelist(df, source='Estaciones', target='Destinos', edge_attr='Tiempo_Viaje')


#Mensaje inicial
print("\nSistema de transporte masivo Transmilenio Bogotá \n")

# Definir el punto de inicio y el punto de destino
punto_inicio = input('Escriba su punto de origen: ') 
punto_destino = input('Escriba su punto de destino: ') 

# Usar el algoritmo de Dijkstra para encontrar la mejor ruta (menor tiempo de viaje)
mejor_ruta = nx.dijkstra_path(G, source=punto_inicio, target=punto_destino, weight='Tiempo_Viaje')
mejor_tiempo = nx.dijkstra_path_length(G, source=punto_inicio, target=punto_destino, weight='Tiempo_Viaje')

print(f"\nComenzando en la estación {punto_inicio}, la mejor ruta es: \n")
for i in range(len(mejor_ruta) - 1):
    estacion_a = mejor_ruta[i]
    proxima_estacion = mejor_ruta[i + 1]
    print(f"De la estación {estacion_a} ir hasta la estación {proxima_estacion}")

# Mostrar los resultados
print(f"\nEl tiempo total de viaje de {punto_inicio} hasta {punto_destino} es: {mejor_tiempo} minutos\n")