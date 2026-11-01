# Aquí irán las ecuaciones del Centro de Gravedad
import numpy as np

def calcular_cg_dinamico(pesos: dict, brazos: dict, consumo_combustible_lbs_hr: float, tiempo_vuelo_hr: float, mtow: float) -> dict:
    # 1. Validación de entradas (Física y límites estructurales)
    if any(p < 0 for p in pesos.values()):
        raise ValueError("Error Físico: Se detectaron pesos negativos.")
    
    peso_cero_combustible = pesos['vacio'] + pesos['piloto_copiloto'] + pesos['pax_traseros'] + pesos['equipaje']
    peso_total_inicial = peso_cero_combustible + pesos['combustible']
    
    if peso_total_inicial > mtow:
        raise ValueError(f"Violación Estructural: El peso inicial ({peso_total_inicial} lbs) excede el MTOW ({mtow} lbs).")

    combustible_total_consumido = consumo_combustible_lbs_hr * tiempo_vuelo_hr
    if combustible_total_consumido > pesos['combustible']:
        raise ValueError("Error de Operación: El tiempo de vuelo excede la capacidad de combustible a bordo.")

    # 2. Computación Vectorizada (Eficiencia Algorítmica sin bucles)
    vector_tiempo = np.linspace(0, tiempo_vuelo_hr, 100)
    vector_combustible = pesos['combustible'] - (consumo_combustible_lbs_hr * vector_tiempo)
    vector_peso_total = peso_cero_combustible + vector_combustible
    
    momento_cero_combustible = (pesos['vacio'] * brazos['vacio'] +
                                pesos['piloto_copiloto'] * brazos['piloto_copiloto'] +
                                pesos['pax_traseros'] * brazos['pax_traseros'] +
                                pesos['equipaje'] * brazos['equipaje'])
                                
    vector_momento_combustible = vector_combustible * brazos['combustible']
    vector_momento_total = momento_cero_combustible + vector_momento_combustible
    vector_cg = vector_momento_total / vector_peso_total

    return {
        "tiempo_hr": vector_tiempo,
        "peso_total_lbs": vector_peso_total,
        "cg_pulgadas": vector_cg
    }