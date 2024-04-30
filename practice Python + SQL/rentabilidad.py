import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

with sqlite3.connect("Northwind.db") as conection_DB:
    # consulta para obtener los primeros 10 pronductos mas rentables
    query = '''
            SELECT ProductName, sum(Price * Quantity) as Revenue
            FROM OrderDetails od
            JOIN Products p ON p.ProductID = od.ProductID
            GROUP BY od.ProductID
            ORDER BY Revenue DESC
            LIMIT 10
            '''
    top_products = pd.read_sql_query(query, conection_DB)
    print(top_products)

    # hacer que el cuadro/ventana sea de 10 de with y 5 de heigth
    # y rotar los nombres de los productos 90°
    plt.figure(figsize=(10, 5))
    plt.xticks(rotation=45)

    # generar el grafico de barras
    sns.barplot(x="ProductName", y="Revenue", data=top_products, width=0.6)

    # agregar un tituloa a la ventana
    plt.title("Ventas por producto")
    # mostrar el grafico
    plt.show()

    query2 = '''
            SELECT FirstName || " " || LastName as Nombre, count(*) as total_ordenes
            FROM Orders o
            INNER JOIN Employees e ON e.EmployeeID = o.EmployeeID
            GROUP BY o.EmployeeID
            ORDER BY total_ordenes DESC
            '''
    top_employees = pd.read_sql_query(query2, conection_DB)
    print(top_employees)

    # hacer que el cuadro/ventana sea de 10 de with y 5 de heigth
    # y rotar los nombres de los productos 90°
    plt.figure(figsize=(10, 5))
    plt.xticks(rotation=45)

    # generar el grafico de barras
    sns.barplot(x="Nombre", y="total_ordenes", data=top_employees, width=0.6)

    # agregar un tituloa a la ventana
    plt.title("Ventas por empleado")
    # mostrar el grafico
    plt.show()
