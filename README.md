# Curvometria Quântica 🌌

Um modelo teórico para estimar massas de partículas subatômicas usando geometria relativística.

## 📚 Fundamentação Teórica
Relaciona a massa de partículas com sua "curvatura espaço-temporal efetiva" através da equação:
```
θ = (m · c · R) / ħ
```

onde:
- `θ`: Curvatura angular adimensional
- `m`: Massa da partícula (kg)
- `R`: Raio característico (m)
- `c`: Velocidade da luz
- `ħ`: Constante de Planck reduzida

## 🛠️ Instalação
```bash
git clone https://github.com/seu-usuario/curvometria-quantica.git
cd curvometria-quantica
pip install -r requirements.txt
## 🚀 Como Usar
```python
# Executar análise completa
python src/curvometria.py

# Saída esperada:
# - Tabelas de validação e predição
# - Gráfico log(m) vs θ
```

## 📊 Resultados
### Validação com Partículas Conhecidas
| Partícula      | Classe      | R (fm) | θ (rad) | Massa (kg)    |
|----------------|-------------|--------|---------|---------------|
| Píon (π⁺)      | Méson       | 1.565  | 1.1     | 2.488e-28     |
| J/ψ            | Méson       | 28.15  | 448.7   | 5.610e-27     |

### Predições para Partículas Exóticas
| Partícula      | Classe      | R (fm) | Massa Prevista (kg) |
|----------------|-------------|--------|---------------------|
| Glueball G⁰    | Glueball    | 7.5    | 3.377e-26          |

### 2. `requirements.txt`
```
numpy==1.26.0
pandas==2.1.1
matplotlib==3.7.2
```
