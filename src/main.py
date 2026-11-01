# Este es el orquestador principal del programa
from core.fisicas import calcular_cg_dinamico
from ui.graficos import graficar_envolvente_cg

def main():
    print("--- Simulador de Peso y Balance (Dinámica de CG) ---")
    
    mtow = 5200.0  # lbs
    pesos_actuales = {'vacio': 3100.0, 'piloto_copiloto': 380.0, 'pax_traseros': 340.0, 'equipaje': 150.0, 'combustible': 864.0}
    brazos_datum = {'vacio': 101.5, 'piloto_copiloto': 91.0, 'pax_traseros': 128.5, 'equipaje': 155.0, 'combustible': 105.0}
    
    consumo_lbs_hr = 150.0
    tiempo_mision = 4.5

    limites_afm = {
        "cg": [95.0, 107.0, 107.0, 99.5, 95.0],
        "peso": [3500.0, 3500.0, 5200.0, 5200.0, 3500.0]
    }

    try:
        print("Calculando cinemática vectorial del combustible...")
        resultados = calcular_cg_dinamico(pesos_actuales, brazos_datum, consumo_lbs_hr, tiempo_mision, mtow)
        
        cg_despegue = resultados["cg_pulgadas"][0]
        cg_aterrizaje = resultados["cg_pulgadas"][-1]
        
        print("\n[RESULTADOS DEL VUELO]")
        print(f"CG al Despegue:   {cg_despegue:.2f} pulg. | Peso: {resultados['peso_total_lbs'][0]:.1f} lbs")
        print(f"CG al Aterrizaje: {cg_aterrizaje:.2f} pulg. | Peso: {resultados['peso_total_lbs'][-1]:.1f} lbs")
        
        print("\nGenerando matriz gráfica...")
        graficar_envolvente_cg(resultados, limites_afm)

    except ValueError as e:
        print(f"\n[!] EXCEPCIÓN PREVENTIVA ACTIVADA:\n    {e}")
    except Exception as e:
        print(f"\n[!] Fallo no controlado:\n    {e}")

if __name__ == "__main__":
    main()
    
