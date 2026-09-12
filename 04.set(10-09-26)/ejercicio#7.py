# EJERCICIO 7 — SETS

# Tienes tres conjuntos:
# #
# # usuarios_registrados
# # usuarios_activos
# # usuarios_bloqueados
# #
# # Obtén un set con los usuarios que:
# #
# # - Están registrados.
# # - Están activos.
# # - NO están bloqueados.
# #
# # Ejemplo conceptual:
# #
# # registrados ∩ activos - bloqueados
# #
# # No utilices listas para realizar la operación.


# 

usuarios_registrados = {
    "ana_garcia", "luis_martinez", "carlos_ruiz", "sofia_lopez", "pedro_sanchez",
    "elena_torres", "miguel_ramirez", "laura_fernandez", "javier_moreno", "marta_jimenez",
    "david_ortiz", "cristina_navarro", "pablo_dominguez", "sara_vazquez", "alberto_romero",
    "nuria_gutierrez", "sergio_castillo", "paula_serrano", "andres_blanco", "irene_molina",
    "raul_herrera", "beatriz_medina", "victor_castro", "alicia_rubio", "ivan_suarez",
    "rocio_ortega", "adrian_delgado", "silvia_marin", "oscar_iglesias", "claudia_santos",
    "gonzalo_reyes", "lucia_cortes", "hugo_garrido", "natalia_sanz", "ruben_benitez",
    "patricia_lorenzo", "alvaro_mendez", "miriam_estevez", "fernando_carrasco", "noelia_prieto",
    "jorge_llorente", "veronica_gallardo", "santiago_rojas", "tatiana_ferrer", "emilio_cuesta",
    "raquel_pardo", "nicolas_aguilar", "estefania_bermejo", "tomas_rodrigo", "valeria_solano",
    "gabriel_pena", "monica_duarte", "borja_escobar", "amparo_zaragoza", "hector_villalba"
}

usuarios_activos = {
    "ana_garcia", "luis_martinez", "carlos_ruiz", "sofia_lopez", "pedro_sanchez",
    "elena_torres", "miguel_ramirez", "laura_fernandez", "javier_moreno", "marta_jimenez",
    "david_ortiz", "cristina_navarro", "pablo_dominguez", "sara_vazquez", "alberto_romero",
    "nuria_gutierrez", "sergio_castillo", "paula_serrano", "andres_blanco", "irene_molina",
    "raul_herrera", "beatriz_medina", "victor_castro", "alicia_rubio", "ivan_suarez",
    "rocio_ortega", "adrian_delgado", "silvia_marin", "oscar_iglesias", "claudia_santos",
    "gonzalo_reyes", "lucia_cortes"
}

usuarios_bloqueados = {
    "hugo_garrido", "natalia_sanz", "ruben_benitez", "patricia_lorenzo", "alvaro_mendez",
    "miriam_estevez", "fernando_carrasco", "noelia_prieto", "jorge_llorente", "veronica_gallardo"
}

usuarios_filtrados = (usuarios_registrados & usuarios_activos) - usuarios_bloqueados

print(usuarios_filtrados)
