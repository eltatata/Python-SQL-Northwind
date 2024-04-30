import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


with sqlite3.connect("Northwind.db") as conection_DB:
    query = '''
        SELECT 	FirstName || " " || LastName as Nombre, 
                ProductName, max(Quantity) as cantidad, 
                round(Price * max(Quantity)) as total_vendido  
        FROM Employees e
        JOIN Orders o ON  e.EmployeeID = o.EmployeeID 
        JOIN OrderDetails od ON o.OrderID = od.OrderID 
        JOIN Products p ON od.ProductID = p.ProductID
        GROUP BY o.EmployeeID
        ORDER BY Quantity DESC
        '''

    # obtener el resultado de la consulta a la base de datos y pasarlo a data frame
    query_res = pd.read_sql_query(query, conection_DB)
    print(query_res)

    # Configurar el tamaño de la figura
    # y rotar los nombres de los productos 45°
    plt.figure(figsize=(10, 6))
    plt.xticks(rotation=45)

    # Generar el gráfico de barras utilizando Seaborn
    ax = sns.barplot(x=query_res['Nombre'],
                     y=query_res['total_vendido'], width=0.6)

    # Etiquetas de los ejes y título del gráfico
    plt.xlabel('Empleado')
    plt.ylabel('Total Recaudado')
    plt.title('Total Recaudado, Cantidad por Producto y Empleado')

    # # Agregar etiquetas a cada barra
    for i, v in enumerate(query_res['total_vendido']):
        ax.text(i, v, str(v), ha='center', va='bottom')

    # agregar los labels a la legend y mostrarlos
    labels = [f"{nombre} ({cantidad})" for nombre, cantidad in zip(query_res['ProductName'], query_res['cantidad'])]
    plt.legend(handles=ax.containers[0], labels=labels, title='Cantidad vendida')

    # Ajustar los márgenes del gráfico para evitar el desplazamiento de las barras
    plt.tight_layout()

    # Mostrar el gráfico
    plt.show()
