# EJERCICIO 10 — SETS

# Tienes productos representados mediante tuplas:
# #
# # productos = (
# #     ("arroz", {"alimentacion", "basico", "granos"}),
# #     ("cafe", {"alimentacion", "bebida", "basico"}),
# #     ("aceite", {"alimentacion", "basico", "cocina"}),
# #     ("refresco", {"bebida", "azucar"}),
# # )
# #
# # Escribe una función que reciba el conjunto de etiquetas
# # buscadas y devuelva los productos que tengan TODAS esas
# # etiquetas.
# #
# # Ejemplo:
# #
# # etiquetas_buscadas = {"alimentacion", "basico"}
# #
# # Resultado:
# #
# # {"arroz", "cafe", "aceite"}
# #
# # Importante:
# # Un producto solo entra si contiene todas las etiquetas
# # solicitadas.
# #
# # Aquí debes combinar:
# # - tuplas
# # - sets
# # - iteración
# # - operaciones de conjuntos
# 

def filtrar_productos(productos,etiquetas_buscadas):
    lista =[ ]
    for producto in productos:
        if etiquetas_buscadas <= producto[1]:
            lista.append(producto[0])

    return set(lista)

productos = (
    # --- Alimentación básica ---
    ("arroz", {"alimentacion", "basico", "granos"}),
    ("cafe", {"alimentacion", "bebida", "basico"}),
    ("aceite", {"alimentacion", "basico", "cocina"}),
    ("refresco", {"bebida", "azucar"}),
    ("pan", {"alimentacion", "basico", "panaderia"}),
    ("leche", {"alimentacion", "basico", "lacteos"}),
    ("huevos", {"alimentacion", "basico", "proteinas"}),
    ("azucar", {"alimentacion", "basico", "endulzante"}),
    ("sal", {"alimentacion", "basico", "condimento"}),
    ("harina", {"alimentacion", "basico", "panaderia"}),
    ("pasta", {"alimentacion", "basico", "granos"}),
    ("legumbres", {"alimentacion", "basico", "granos", "proteinas"}),
    ("atun", {"alimentacion", "proteinas", "conserva"}),
    ("sardinas", {"alimentacion", "proteinas", "conserva"}),
    ("mantequilla", {"alimentacion", "lacteos", "cocina"}),
    ("yogur", {"alimentacion", "lacteos", "fresco"}),
    ("queso", {"alimentacion", "lacteos", "fresco"}),
    ("cereal", {"alimentacion", "desayuno", "granos"}),
    ("galletas", {"alimentacion", "snack", "azucar"}),
    ("chocolate", {"alimentacion", "snack", "azucar"}),

    # --- Bebidas ---
    ("agua", {"bebida", "basico", "saludable"}),
    ("zumo", {"bebida", "azucar", "fresco"}),
    ("te", {"bebida", "saludable", "basico"}),
    ("cerveza", {"bebida", "alcohol", "adulto"}),
    ("vino", {"bebida", "alcohol", "adulto"}),
    ("bebida_energetica", {"bebida", "azucar", "energia"}),

    # --- Frutas y verduras ---
    ("manzana", {"alimentacion", "fruta", "fresco", "saludable"}),
    ("platano", {"alimentacion", "fruta", "fresco", "saludable"}),
    ("naranja", {"alimentacion", "fruta", "fresco", "saludable"}),
    ("tomate", {"alimentacion", "verdura", "fresco", "saludable"}),
    ("cebolla", {"alimentacion", "verdura", "fresco", "basico"}),
    ("patata", {"alimentacion", "verdura", "basico", "granos"}),
    ("zanahoria", {"alimentacion", "verdura", "fresco", "saludable"}),
    ("lechuga", {"alimentacion", "verdura", "fresco", "saludable"}),
    ("pimiento", {"alimentacion", "verdura", "fresco", "saludable"}),

    # --- Carnes y pescados ---
    ("pollo", {"alimentacion", "carne", "proteinas", "fresco"}),
    ("ternera", {"alimentacion", "carne", "proteinas", "fresco"}),
    ("cerdo", {"alimentacion", "carne", "proteinas", "fresco"}),
    ("salmon", {"alimentacion", "pescado", "proteinas", "fresco"}),
    ("merluza", {"alimentacion", "pescado", "proteinas", "fresco"}),

    # --- Limpieza ---
    ("detergente", {"limpieza", "hogar", "quimico"}),
    ("lejia", {"limpieza", "hogar", "quimico"}),
    ("lavavajillas", {"limpieza", "hogar", "cocina", "quimico"}),
    ("suavizante", {"limpieza", "hogar", "quimico"}),
    ("friegasuelos", {"limpieza", "hogar", "quimico"}),
    ("estropajo", {"limpieza", "hogar", "cocina", "desechable"}),
    ("bolsas_basura", {"limpieza", "hogar", "desechable"}),

    # --- Higiene personal ---
    ("jabon", {"higiene", "personal", "basico"}),
    ("champu", {"higiene", "personal", "cabello"}),
    ("pasta_dientes", {"higiene", "personal", "bucal"}),
    ("cepillo_dientes", {"higiene", "personal", "bucal"}),
    ("desodorante", {"higiene", "personal", "cuidado"}),
    ("gel", {"higiene", "personal", "basico"}),
    ("papel_higienico", {"higiene", "personal", "basico", "desechable"}),
    ("panales", {"higiene", "bebe", "desechable"}),

    # --- Hogar y cocina ---
    ("servilletas", {"hogar", "cocina", "desechable"}),
    ("papel_cocina", {"hogar", "cocina", "desechable"}),
    ("film_transparente", {"hogar", "cocina", "desechable"}),
    ("aluminio", {"hogar", "cocina", "desechable"}),
    ("vajilla", {"hogar", "cocina", "reutilizable"}),
    ("cubiertos", {"hogar", "cocina", "reutilizable"}),
    ("sarten", {"hogar", "cocina", "reutilizable"}),
    ("olla", {"hogar", "cocina", "reutilizable"}),

    # --- Mascotas ---
    ("pienso_perro", {"mascotas", "perro", "alimentacion"}),
    ("pienso_gato", {"mascotas", "gato", "alimentacion"}),
    ("arena_gato", {"mascotas", "gato", "higiene"}),
    ("juguete_mascota", {"mascotas", "juguete"}),

    # --- Bebés ---
    ("leche_materna", {"bebe", "alimentacion", "lacteos"}),
    ("papilla", {"bebe", "alimentacion", "fresco"}),
    ("toallitas", {"bebe", "higiene", "desechable"}),
    ("biberon", {"bebe", "cocina", "reutilizable"}),

    # --- Otros ---
    ("pilas", {"electronica", "hogar", "desechable"}),
    ("bombillas", {"electronica", "hogar"}),
    ("encendedor", {"hogar", "peligroso"}),
    ("velas", {"hogar", "decoracion"}),
    ("cuaderno", {"papeleria", "estudio"}),
    ("boligrafo", {"papeleria", "estudio"}),
    ("libro", {"papeleria", "estudio", "ocio"}),
)

buscadas = {"alimentacion", "basico"}

encontrados = filtrar_productos(productos,buscadas)

print(encontrados)


