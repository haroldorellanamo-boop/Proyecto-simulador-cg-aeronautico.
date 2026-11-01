# Aquí irán los gráficos de la envolvente de vuelo
import matplotlib.pyplot as plt

def graficar_envolvente_cg(resultados: dict, limites_envolvente: dict):
    pesos = resultados["peso_total_lbs"]
    cgs = resultados["cg_pulgadas"]
    
    env_cg = limites_envolvente["cg"]
    env_peso = limites_envolvente["peso"]

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(env_cg + [env_cg[0]], env_peso + [env_peso[0]], 'k--', linewidth=2, label='Límites Estructurales (AFM)')
    ax.fill(env_cg, env_peso, alpha=0.1, color='gray')

    trayectoria = ax.scatter(cgs, pesos, c=resultados["tiempo_hr"], cmap='viridis', s=40, zorder=5)
    ax.plot(cgs, pesos, 'b-', linewidth=1.5, alpha=0.6, label='Trayectoria del Vuelo')
    
    ax.plot(cgs[0], pesos[0], 'go', markersize=8, label='Despegue (Takeoff)')
    ax.plot(cgs[-1], pesos[-1], 'ro', markersize=8, label='Aterrizaje (Landing)')

    cbar = plt.colorbar(trayectoria)
    cbar.set_label('Tiempo de Vuelo [Horas]', fontweight='bold')
    
    ax.set_title('Desplazamiento Dinámico del Centro de Gravedad', fontsize=14, fontweight='bold')
    ax.set_xlabel('Estación del CG [Pulgadas desde Datum]', fontweight='bold')
    ax.set_ylabel('Peso Total [lbs]', fontweight='bold')
    ax.grid(True, linestyle=':', alpha=0.7)
    ax.legend(loc='lower left')

    plt.tight_layout()
    plt.show()
    