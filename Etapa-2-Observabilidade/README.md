
# 📊 Etapa 2 – Observabilidade com Prometheus e Grafana

## ⚙️ Instalações e Configurações

Durante esta etapa, foram realizadas as seguintes instalações e configurações:

- **Prometheus Operator (via Helm)**
  ```bash
  helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
  helm repo update
  helm install prometheus prometheus-community/kube-prometheus-stack -n aiops-banco
  ```
  Instala Prometheus, Alertmanager e Grafana no namespace `aiops-banco`.  
  **Evidência:** `docs/prometheus-operator.png`

Aqui está, Márcia 🌟!  
Segue o trecho em formato **README.md**, já com os comandos de evidência para o **Metrics-server**. Assim você mantém o padrão de documentação com comandos + espaço para os prints.

---

```markdown
# 📊 Etapa 2 – Observabilidade com Prometheus e Grafana

## ⚙️ Instalações e Configurações

### 🔹 Prometheus Operator (via Helm)
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus prometheus-community/kube-prometheus-stack -n aiops-banco
```
Instala Prometheus, Alertmanager e Grafana no namespace `aiops-banco`.  
**Evidência:** `docs/prometheus-operator.png`

---

### 🔹 Metrics-server
Arquivo: `metrics-server-deployment.yaml`

```bash
kubectl apply -f metrics-server-deployment.yaml -n aiops-banco
```

#### 📌 Comandos de evidência

```bash
# Verificar se o pod do metrics-server está rodando
kubectl get pods -n kube-system | findstr metrics-server

# Verificar se o APIService está disponível
kubectl get apiservice | findstr metrics.k8s.io

# Testar coleta de métricas
kubectl top nodes
kubectl top pods -n aiops-banco
```

#### 📌 Saídas esperadas
- Pod `metrics-server-xxxxx` em estado **Running**.  
- APIService `v1beta1.metrics.k8s.io` com status **True**.  
- Listagem de nós e pods com consumo de CPU e memória.

#### 📌 Evidências
- `docs/metrics-server.png` → Pod rodando.  
- `docs/metrics-server-apiservice.png` → APIService ativo.  
- `docs/metrics-server-top-nodes.png` → Métricas de nós.  
- `docs/metrics-server-top-pods.png` → Métricas de pods.
```

---

Ótimo, Márcia 🌟!  
Aqui está o bloco em **README.md** para evidenciar o **Deployment da aplicação, Service, ServiceMonitor e HPA**, já com os comandos de verificação, saídas esperadas e espaços para os prints:

---

```markdown
### 🔹 Deployment da aplicação
Arquivo: `aiops-app-deployment.yaml`  
👉 Define os pods da aplicação e expõe a porta 8000.

```bash
# Aplicar o deployment
kubectl apply -f aiops-app-deployment.yaml -n aiops-banco

# Verificar se os pods da aplicação estão rodando
kubectl get pods -n aiops-banco | findstr aiops-app

# Verificar o deployment
kubectl get deployment aiops-app -n aiops-banco
```

**Saída esperada:**
- Pods `aiops-app-xxxxx` em estado **Running**.  
- Deployment `aiops-app` criado e disponível.  

**Evidência:** `docs/deployment.png`

---

### 🔹 Service da aplicação
Arquivo: `aiops-service.yaml`  
👉 Exposição interna da aplicação para que Prometheus consiga coletar métricas.

```bash
# Aplicar o service
kubectl apply -f aiops-service.yaml -n aiops-banco

# Verificar se o service foi criado
kubectl get svc -n aiops-banco | findstr aiops-service

# Testar acesso às métricas
kubectl port-forward svc/aiops-service 8000:8000 -n aiops-banco
curl http://localhost:8000/metrics | head -n 10
```

**Saída esperada:**
- Service `aiops-service` criado.  
- Endpoint `/metrics` acessível.  

**Evidência:** `docs/service.png`

---

### 🔹 ServiceMonitor
Arquivo: `aiops-servicemonitor.yaml`  
👉 Configura Prometheus para coletar métricas da aplicação.

```bash
# Aplicar o ServiceMonitor
kubectl apply -f aiops-servicemonitor.yaml -n aiops-banco

# Verificar se o ServiceMonitor foi criado
kubectl get servicemonitor -n aiops-banco | findstr aiops-servicemonitor
```

**Saída esperada:**
- ServiceMonitor `aiops-servicemonitor` criado e listado.  

**Evidência:** `docs/servicemonitor.png`

---

### 🔹 Horizontal Pod Autoscaler (HPA)
Arquivo: `aiops-hpa.yaml`  
👉 Define regras de escalabilidade automática com base em métricas de CPU.

```bash
# Aplicar o HPA
kubectl apply -f aiops-hpa.yaml -n aiops-banco

# Verificar se o HPA está ativo
kubectl get hpa -n aiops-banco

# Simular carga para ver escalonamento
kubectl run -i --tty load-generator --image=busybox --restart=Never -n aiops-banco -- /bin/sh
# Dentro do pod:
while true; do wget -q -O- http://aiops-service:8000/; done
```

**Saída esperada:**
```
NAME         REFERENCE               TARGETS   MINPODS   MAXPODS   REPLICAS   AGE
aiops-hpa    Deployment/aiops-app    75%/80%   2         4         3          10m
```

**Evidência:** `docs/hpa-config.png`
```

---


## 📌 Comandos, Saídas e Evidências

### 1. Exposição de métricas pela aplicação
```bash
kubectl port-forward svc/aiops-service 8000:8000 -n aiops-banco
curl http://localhost:8000/metrics
```
**Saída esperada:**
```
# HELP aiops_anomaly_score Score de anomalia calculado pelo modelo
# TYPE aiops_anomaly_score gauge
aiops_anomaly_score 0.15
```
**Evidência:** `docs/metrics.png`

---

### 2. Coleta de métricas pelo Prometheus
**Query PromQL:**
```promql
aiops_anomaly_score
```
**Saída esperada:**
```
aiops_anomaly_score{instance="aiops-app:8000",job="aiops-monitor"} 0.15
```
**Evidência:** `docs/prometheus.png`

---

### 3. Visualização no Grafana
**Queries configuradas:**
```promql
# Consumo médio de CPU por pod
rate(container_cpu_usage_seconds_total{namespace="aiops-banco"}[2m])

# Score de anomalia
aiops_anomaly_score
```

**Saída esperada:**
- Gráfico de CPU por pod.  
- Gráfico do score de anomalia.  
- Gráfico mostrando réplicas do HPA ao longo do tempo.

**Evidências:**
- `docs/grafana-dashboard.png` → Dashboard consolidado com os quatro painéis.  
- `docs/grafana-cpu.png` → Painel de CPU por pod.  
- `docs/grafana-memoria.png` → Painel de memória por pod.  
- `docs/grafana-anomalia.png` → Painel de score de anomalia.  
- `docs/grafana-hpa.png` → Painel de réplicas do HPA.

---

### 4. Comportamento do HPA
```bash
kubectl get hpa -n aiops-banco
```
**Saída esperada:**
```
NAME         REFERENCE               TARGETS   MINPODS   MAXPODS   REPLICAS   AGE
aiops-hpa    Deployment/aiops-app    75%/80%   2         4         3          10m
```
**Evidência:** `docs/hpa.png`

---

## 🌐 Acesso ao Prometheus e Grafana

### 🔎 Prometheus
```bash
kubectl port-forward svc/prometheus-kube-prometheus-prometheus 9090:9090 -n aiops-banco
```
👉 http://localhost:9090  
**Evidência:** `docs/prometheus-access.png`

---

### 📊 Grafana
```bash
kubectl port-forward svc/prometheus-grafana 3000:80 -n aiops-banco
```
👉 http://localhost:3000  
**Evidência:** `docs/grafana-access.png`

---

### 🔑 Credenciais do Grafana
```bash
kubectl get secret prometheus-grafana -n aiops-banco -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
```
**Evidência:** `docs/grafana-credentials.png`

---

## ✅ Conclusão
As evidências acima comprovam que:
- As métricas foram expostas pela aplicação.  
- Prometheus coletou e armazenou corretamente.  
- Grafana consolidou em dashboards visuais.  
- O HPA reagiu às métricas conforme esperado.  

