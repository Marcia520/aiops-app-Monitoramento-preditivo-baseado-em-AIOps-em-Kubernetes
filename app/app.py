from flask import Flask, Response
from prometheus_client import Gauge, generate_latest, CONTENT_TYPE_LATEST
from sklearn.ensemble import IsolationForest
import numpy as np

app = Flask(__name__)

# Métricas Prometheus
cpu_anomaly_score = Gauge('aiops_cpu_anomaly_score', 'Score de anomalia de CPU')
access_anomaly_score = Gauge('aiops_access_anomaly_score', 'Score de anomalia de acessos')

# Modelos Isolation Forest
dados_cpu = np.random.rand(100, 2)
modelo_cpu = IsolationForest(contamination=0.1).fit(dados_cpu)

dados_acesso = np.random.rand(5000, 2)
modelo_acesso = IsolationForest(contamination=0.05).fit(dados_acesso)

@app.route("/")
def home():
    return "AIOps App rodando no Kubernetes!"

@app.route("/metrics")
def metrics():
    # Simulação de novo dado CPU/memória
    novo_cpu = np.random.rand(1, 2)
    score_cpu = modelo_cpu.decision_function(novo_cpu)
    cpu_anomaly_score.set(score_cpu)

    # Simulação de novo dado de acesso
    novo_acesso = np.random.rand(1, 2)
    score_acesso = modelo_acesso.decision_function(novo_acesso)
    access_anomaly_score.set(score_acesso)

    # Retornar métricas no formato correto
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
