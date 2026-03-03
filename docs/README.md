# 📂 Evidências da Implementação

## 🔧 Preparação do Ambiente

Antes de iniciar a Etapa 1, foi necessário configurar todo o ambiente de desenvolvimento e orquestração. As principais instalações e configurações realizadas foram:

- **Docker Desktop**  
  - Instalado para fornecer o ambiente de containers.  
  - Configurado para rodar localmente com suporte a Kubernetes.  

- **Kubernetes (K8s)**  
  - Ativado dentro do Docker Desktop.  
  - Criado namespace `aiops-banco` para organizar os recursos da aplicação.  
  - Instalado o **metrics-server** para coleta de métricas de CPU e memória.  

- **Git e GitHub**  
  - Repositório criado no GitHub para versionamento do projeto.  
  - Configuração do Git local para sincronizar com o repositório remoto.  
  - Estrutura organizada em pastas:  
    - `app/` → código-fonte da aplicação.  
    - `k8s/` → manifests Kubernetes.  
    - `docs/` → evidências e documentação.  

- **Ferramentas adicionais**  
  - **kubectl**: utilizado para gerenciar os recursos Kubernetes.  
  - **Prometheus e Grafana**: instalados posteriormente para observabilidade (Etapa 2).  

---

## 📌 Fluxo de Implementação

1. Preparação do ambiente (Docker, Kubernetes, Git).  
2. Empacotamento da aplicação em container e orquestração no Kubernetes (**Etapa 1**).  
3. Configuração de observabilidade com Prometheus e Grafana (**Etapa 2**).  
4. Testes de escalabilidade automática com HPA.  
5. Evidências documentadas na pasta `docs/`.

---

## 🔧 Evidências das Instalações

- **Docker Desktop em execução:**  
  ![docker](docker.PNG)

- **Kubernetes ativado no Docker Desktop e nó em execução:**  
  ![kubernetes](kubernetes.PNG)

- **Cluster ativo (nó em execução):**  
  ![cluster ativo](cluster_ativo.PNG)

- **Namespace criado (aiops-banco):**  
  ![namespace](namespace_ativo.PNG)

- **Metrics-server funcionando (CPU/Memória):**  
  ![metrics Server](metrics_server.PNG)

- **Git instalado e configurado localmente:**  
  ![git](git.PNG)

- **Repositório conectado ao GitHub:**  
  ![github](github.PNG)

  
## 1. Etapa 1 – Empacotamento e Orquestração
Este documento reúne as evidências coletadas durante a **Etapa 1** do protótipo, que consistiu em empacotar a aplicação `aiops-app` em containers e orquestrá-la em ambiente Kubernetes (Docker Desktop).

---

## 1. Pods em execução
- **Comando utilizado:**
  ```bash
  kubectl get pods -n aiops-banco
  ```
- **Descrição:**  
  Lista todos os pods ativos no namespace `aiops-banco`, confirmando que a aplicação e os componentes de observabilidade estão em execução.
- **Evidência:**  
 ![pods](pods.PNG)

---

## 2. Métricas coletadas
- **Comando utilizado:**
  ```bash
  kubectl top pods -n aiops-banco
  ```
- **Descrição:**  
  Exibe consumo de CPU e memória dos pods, validando que o **metrics-server** está funcionando corretamente.
- **Evidência:**  
  ![metrics](metricas.PNG)

---

## 3. HPA monitorando a aplicação
- **Comando utilizado:**
  ```bash
  kubectl get hpa -n aiops-banco --watch
  ```
- **Descrição:**  
  Mostra o comportamento do **Horizontal Pod Autoscaler (HPA)**, incluindo limites de CPU, número mínimo/máximo de pods e réplicas atuais.
- **Evidência:**  
 ![hpa](hpa.PNG)

---

## 4. Escalada automática
- **Descrição:**  
  Durante a execução de carga simulada (via BusyBox), o HPA detectou aumento de CPU e escalou a aplicação, criando novos pods automaticamente.
![escala_automatica](escala_automatica.PNG)

---


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

- **Metrics-server**
  Arquivo: `metrics-server-deployment.yaml`  
  Responsável por fornecer métricas de CPU e memória ao Kubernetes, permitindo o funcionamento do HPA.
  ```bash
  kubectl apply -f metrics-server-deployment.yaml -n aiops-banco
  ```
  Verificação:
  ```bash
  kubectl get pods -n kube-system | grep metrics-server
  ```
  Saída esperada:
  ```
  metrics-server-7f8d9f9d8d-abcde   1/1   Running   0   2m
  ```

- **Deployment da aplicação**
  Arquivo: `aiops-app-deployment.yaml`  
  👉 Define os pods da aplicação e expõe a porta 8000.

- **Service da aplicação**
  Arquivo: `aiops-service.yaml`  
  👉 Exposição interna da aplicação para que Prometheus consiga coletar métricas.

- **ServiceMonitor**
  Arquivo: `aiops-servicemonitor.yaml`  
  👉 Configura Prometheus para coletar métricas da aplicação.

- **Horizontal Pod Autoscaler (HPA)**
  Arquivo: `aiops-hpa.yaml`  
  👉 Define regras de escalabilidade automática com base em métricas de CPU.

---

## 📌 Comandos, Saídas e Evidências

### 1. Exposição de métricas pela aplicação
- **Port-forward:**
  ```bash
  kubectl port-forward svc/aiops-service 8000:8000 -n aiops-banco
  ```
- **Acesso às métricas:**
  ```bash
  curl http://localhost:8000/metrics
  ```
- **Saída esperada:**
  ```
  # HELP aiops_anomaly_score Score de anomalia calculado pelo modelo
  # TYPE aiops_anomaly_score gauge
  aiops_anomaly_score 0.15
  ```
- **Evidência:** `docs/metrics.png`

---

### 2. Coleta de métricas pelo Prometheus
- **Query PromQL:**
  ```promql
  aiops_anomaly_score
  ```
- **Saída esperada:**
  ```
  aiops_anomaly_score{instance="aiops-app:8000",job="aiops-monitor"} 0.15
  ```
- **Evidência:** `docs/prometheus.png`

---

### 3. Visualização no Grafana
- **Queries configuradas:**
  ```promql
  # Consumo médio de CPU por pod
  rate(container_cpu_usage_seconds_total{namespace="aiops-banco"}[2m])

  # Score de anomalia
  aiops_anomaly_score
  ```
- **Saída esperada:**
  - Gráfico de CPU por pod.  
  - Gráfico do score de anomalia.  
  - Gráfico mostrando réplicas do HPA ao longo do tempo.
- **Evidência:** `docs/grafana.png`

---

### 4. Comportamento do HPA
- **Comando:**
  ```bash
  kubectl get hpa -n aiops-banco
  ```
- **Saída esperada:**
  ```
  NAME         REFERENCE               TARGETS   MINPODS   MAXPODS   REPLICAS   AGE
  aiops-hpa    Deployment/aiops-app    75%/80%   2         4         3          10m
  ```
- **Evidência:** `docs/hpa.png`

---

## 🌐 Acesso ao Prometheus e Grafana

### 🔎 Prometheus
- **Service:** `prometheus-kube-prometheus-prometheus`
- **Porta:** `9090`
- **Comando:**
  ```bash
  kubectl port-forward svc/prometheus-kube-prometheus-prometheus 9090:9090 -n aiops-banco
  ```
- **Link local:**  
  👉 http://localhost:9090

---

### 📊 Grafana
- **Service:** `prometheus-grafana`
- **Porta:** `80`
- **Comando:**
  ```bash
  kubectl port-forward svc/prometheus-grafana 3000:80 -n aiops-banco
  ```
- **Link local:**  
  👉 http://localhost:3000

---

### 🔑 Credenciais do Grafana
- Usuário: `admin`  
- Senha: gerada automaticamente pelo Helm Chart. Para descobrir:
  ```bash
  kubectl get secret prometheus-grafana -n aiops-banco -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
  ```

---
