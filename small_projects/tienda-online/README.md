# Proyecto de Tienda Virtual

Este proyecto es un sistema de gestión de tienda virtual que permite a los usuarios gestionar el inventario, visualizar productos, realizar compras y consultar el historial de compras. 

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
tienda-virtual
├── src
│   ├── main.py                  # Punto de entrada de la aplicación
│   ├── inventory                # Módulo de gestión de inventario
│   │   ├── __init__.py
│   │   └── inventory_manager.py  # Clase InventoryManager para gestionar el inventario
│   ├── products                 # Módulo de visualización de productos
│   │   ├── __init__.py
│   │   └── product_viewer.py    # Clase ProductViewer para visualizar productos
│   ├── purchases                # Módulo de gestión de compras
│   │   ├── __init__.py
│   │   └── purchase_manager.py   # Clase PurchaseManager para gestionar compras
│   ├── history                  # Módulo de consulta del historial de compras
│   │   ├── __init__.py
│   │   └── history_viewer.py     # Clase HistoryViewer para consultar historial de compras
│   └── menu                     # Módulo del menú interactivo
│       ├── __init__.py
│       └── interactive_menu.py    # Clase InteractiveMenu para gestionar el menú
├── requirements.txt             # Dependencias necesarias para el proyecto
└── README.md                    # Documentación del proyecto
```

## Instalación

1. Clona el repositorio en tu máquina local.
2. Navega al directorio del proyecto.
3. Instala las dependencias necesarias ejecutando:

```
pip install -r requirements.txt
```

## Uso

Para iniciar la aplicación, ejecuta el siguiente comando:

```
python src/main.py
```

Esto abrirá un menú interactivo donde podrás gestionar el inventario, visualizar productos, realizar compras y consultar el historial de compras.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.