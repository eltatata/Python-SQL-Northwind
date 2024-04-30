import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


with sqlite3.connect("Northwind.db") as conection_DB:
    query_employees = '''
        SELECT FirstName || " " || LastName as Nombre, sum(Quantity) as cantidadVendida 
        FROM Orders o, OrderDetails od, Employees e
        WHERE o.OrderID = od.OrderID AND o.EmployeeID = e.EmployeeID
        GROUP BY o.EmployeeID
        '''

    # obtener el resultado de la consulta a la base de datos y pasarlo a data frame
    employee_sales = pd.read_sql_query(query_employees, conection_DB)
    print(employee_sales)
    
    # calcular el promedio de ventas
    average = round(employee_sales["cantidadVendida"].mean())
    # print(average)

    # hacer que el cuadro/ventana sea de 10 de with y 5 de heigth
    # y rotar los nombres de los productos 45°
    plt.figure(figsize=(10, 5))
    plt.xticks(rotation=45)
    
    # generar el grafico de barras
    sns.barplot(x="Nombre", y="cantidadVendida", data=employee_sales, width=0.6)
    
    # agregar un tituloa a la ventana
    plt.title("Ventas de los empleados")
    
    # Agregar una línea para el promedio
    plt.axhline(average, color='r', linestyle='--', label='Promedio Ventas')

    # ajustar automáticamente los márgenes y espaciado de los subplots y los elementos del gráfico 
    # para que se ajusten de manera óptima dentro de la figura
    plt.tight_layout()
    
    # Mostrar la leyenda
    plt.legend()
    
    # mostrar el grafico
    plt.show()