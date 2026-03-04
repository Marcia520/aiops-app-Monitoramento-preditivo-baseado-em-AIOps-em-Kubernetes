import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# 1. Gerar dados simulados
def gerar_dados_bancarios(n=5000):
    np.random.seed(42)
    paises = ['Brasil', 'Estados Unidos', 'Canadá', 'Alemanha', 'França']
    cidades_br = ['São Paulo', 'Rio de Janeiro', 'Brasília', 'Curitiba']
    regioes_br = ['Sudeste', 'Sul', 'Centro-Oeste', 'Nordeste', 'Norte']
    dispositivos = ['celular', 'computador', 'tablet']

    dados = pd.DataFrame({
        'cliente_id': np.random.randint(100000, 999999, n),
        'hora': np.random.randint(0, 24, n),
        'qtd_acessos': np.random.poisson(3, n),
        'pais': np.random.choice(paises, n),
        'cidade': np.random.choice(cidades_br, n),
        'regiao': np.random.choice(regioes_br, n),
        'dispositivo': np.random.choice(dispositivos, n),
        'cliente': np.random.choice([0, 1], n),
        'bot': np.random.choice([0, 1], n)
    })

    dados = pd.get_dummies(dados, columns=['pais', 'cidade', 'regiao', 'dispositivo'], drop_first=True)
    return dados

# 2. Detectar fraudes
def detectar_fraudes(dados):
    modelo = IsolationForest(contamination=0.05, random_state=42)
    modelo.fit(dados.drop(columns=['cliente_id']))
    dados['anomaly'] = modelo.predict(dados.drop(columns=['cliente_id']))
    dados['alerta_fraude'] = dados['anomaly'].apply(lambda x: 'ALERTA' if x == -1 else 'Normal')
    return dados

# 3. Executar pipeline
dados_simulados = gerar_dados_bancarios()
resultado = detectar_fraudes(dados_simulados)

print("Acessos suspeitos detectados:")
print(resultado[resultado['alerta_fraude'] == 'ALERTA'][['cliente_id','hora','qtd_acessos','cliente','bot','alerta_fraude']].head(10))

# 4. Gráfico de acessos
plt.figure(figsize=(10, 6))
cores = resultado['alerta_fraude'].map({'Normal': 'blue', 'ALERTA': 'red'})
tamanhos = resultado['bot'].map({0: 40, 1: 80})
plt.scatter(resultado['hora'], resultado['qtd_acessos'], c=cores, s=tamanhos, alpha=0.6)
plt.xlabel('Hora do Acesso')
plt.ylabel('Quantidade de Acessos')
plt.title('Detecção de Acessos Fraudulentos com Isolation Forest')
plt.grid(True)
plt.tight_layout()
plt.savefig("docs/acessos-fraudulentos.png")  # salva o gráfico
plt.show()
