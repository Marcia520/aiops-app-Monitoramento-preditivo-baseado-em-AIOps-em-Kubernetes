# 📊 Etapa 3 – Aplicação de Algoritmos de IA para Detecção de Anomalias

## 🔹 Isolation Forest
O algoritmo principal escolhido foi o **Isolation Forest**, por ser não supervisionado e adequado a cenários sem dados rotulados.

### 📌 Código de execução (Python)
```python
from sklearn.ensemble import IsolationForest
import pandas as pd

# Carregar métricas simuladas
df = pd.read_csv("metrics.csv")

# Treinar modelo
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(df[["cpu_usage", "memory_usage"]])

# Score de anomalia
df["anomaly_score"] = model.decision_function(df[["cpu_usage", "memory_usage"]])
df["anomaly"] = model.predict(df[["cpu_usage", "memory_usage"]])
```

### 📌 Saída esperada
```
cpu_usage  memory_usage  anomaly_score  anomaly
0.45       0.30          0.12           1
0.95       0.80         -0.25          -1   <-- anomalia detectada
```

### 📌 Evidências
- `docs/isolationforest-code.png` → código rodando.  
- `docs/isolationforest-output.png` → gráfico com pontos normais e anômalos.  
- `docs/anomaly-cpu.png` → anomalias detectadas em métricas de CPU.  
- `docs/anomaly-memory.png` → anomalias em consumo de memória.  
- `docs/anomaly-access.png` → padrões de acesso fora do esperado.  
- `docs/anomaly-logs.png` → logs mostrando alertas de anomalia.

---

## 🔹 Modelos Comparativos

### Random Forest (supervisionado)
- Bom para classificação com dados rotulados.  
- Usado como referência teórica para prever comportamento de serviços.  

**Evidência:** `docs/randomforest.png`

---

### LSTM (redes neurais recorrentes)
- Especializado em séries temporais.  
- Capaz de prever picos de carga e tendências operacionais.  

**Evidência:** `docs/lstm.png`

---

## ✅ Conclusão
- O **Isolation Forest** foi aplicado com sucesso para detectar anomalias em métricas operacionais e padrões de acesso.  
- Modelos comparativos (Random Forest e LSTM) foram discutidos para contextualizar a escolha e indicar extensões futuras.  
- As evidências comprovam a execução prática, geração de scores e identificação de comportamentos atípicos, fortalecendo a resiliência operacional.
```
