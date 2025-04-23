import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# === 1. Constantes Fundamentais ===
hbar = 1.055e-34  # J·s
c = 2.998e8       # m/s
fm_to_m = 1e-15

# === 2. Funções ===
def estimar_theta(m_kg, R_m):
    return m_kg * c * R_m / hbar

def prever_massa(theta, R_m):
    return hbar * theta / (c * R_m)

def painel_validação(df):
    df['R (m)'] = df['R (fm)'] * fm_to_m
    df['θ_real'] = estimar_theta(df['m_exp (kg)'], df['R (m)'])
    df['m_curvo (kg)'] = prever_massa(df['θ_real'], df['R (m)'])
    df['Erro (%)'] = 100 * (df['m_curvo (kg)'] / df['m_exp (kg)'] - 1)
    return df

def painel_predicao(df_novas, theta_por_classe):
    df_novas['R (m)'] = df_novas['R (fm)'] * fm_to_m
    df_novas['θ estimado'] = df_novas['Classe'].map(theta_por_classe)
    df_novas['m_curvo (kg)'] = prever_massa(df_novas['θ estimado'], df_novas['R (m)'])
    return df_novas

def plot_theta_vs_massa(df):
    plt.figure(figsize=(8, 5))
    plt.plot(df['θ_real'], df['m_exp (kg)'], 'o-k', linewidth=1.5)
    plt.yscale('log')
    for i, row in df.iterrows():
        plt.text(row['θ_real']*1.02, row['m_exp (kg)'], row['Partícula'], fontsize=9)
    plt.xlabel('θ (rad)')
    plt.ylabel('Massa experimental (kg) [log]')
    plt.title('Curvometria: Massa vs Curvatura Angular')
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

# === 3. Dados de Partículas Conhecidas ===
dados_reais = {
    'Partícula': ['Píon (π⁺)', 'Káon (K⁺)', 'Méson φ', 'Próton', 'Nêutron', 'J/ψ', 'Ômega⁻', 'D⁰', 'B⁺'],
    'Classe': ['Méson', 'Méson', 'Méson', 'Bárion', 'Bárion', 'Méson', 'Bárion', 'Méson', 'Méson'],
    'm_exp (kg)': [2.488e-28, 8.88e-28, 1.019e-27, 1.6726e-27, 1.675e-27, 5.610e-27, 1.672e-27, 3.330e-27, 5.280e-27],
    'R (fm)': [1.565, 4.5, 5.2, 8.4, 8.45, 28.15, 8.5, 6.0, 7.0]
}
df_conhecidas = pd.DataFrame(dados_reais)
df_conhecidas = painel_validação(df_conhecidas)

# === 4. Estimar θ médio por classe ===
theta_medios = df_conhecidas.groupby('Classe')['θ_real'].mean().to_dict()

# === 5. Novas partículas para predição ===
novas_particulas = {
    'Partícula': ['Teta⁺⁺', 'Híperon Ξ⁰', 'Glueball G⁰', 'Tetraquark X', 'Z⁺ Exótico'],
    'Classe': ['Bárion', 'Bárion', 'Glueball', 'Tetraquark', 'Méson'],
    'R (fm)': [10.0, 9.0, 7.5, 8.0, 6.5]
}
df_novas = pd.DataFrame(novas_particulas)

# Adiciona θ médios estendidos
theta_medios.update({'Glueball': 80.0, 'Tetraquark': 90.0})  # suposições teóricas

df_preditas = painel_predicao(df_novas, theta_medios)

# === 6. Resultados ===
print("\n--- MASSAS CONHECIDAS (VALIDAÇÃO) ---")
print(df_conhecidas[['Partícula', 'Classe', 'R (fm)', 'θ_real', 'm_exp (kg)', 'm_curvo (kg)', 'Erro (%)']])

print("\n--- PREDIÇÕES CURVOMÉTRICAS ---")
print(df_preditas[['Partícula', 'Classe', 'R (fm)', 'θ estimado', 'm_curvo (kg)']])

# === 7. Gráfico log(m) vs θ ===
plot_theta_vs_massa(df_conhecidas)
