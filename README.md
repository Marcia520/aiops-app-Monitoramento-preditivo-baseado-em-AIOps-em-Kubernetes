# aiops-app

Este repositório reúne o desenvolvimento do **Trabalho de Conclusão de Curso (TCC)** cujo objetivo geral é **propor, implementar e validar uma solução de monitoramento preditivo baseada em AIOps aplicada a ambientes Kubernetes no setor bancário**, com foco na:

- Antecipação de falhas operacionais  
- Redução do tempo de resposta a incidentes  
- Aumento da resiliência de serviços críticos  

---

## 🎯 Objetivo
Demonstrar como técnicas de **Machine Learning** (em especial o algoritmo **Isolation Forest**) podem ser integradas a ferramentas de observabilidade (**Prometheus** e **Grafana**) em ambientes **Kubernetes**, aplicadas ao contexto bancário, para identificar comportamentos anômalos e apoiar a tomada de decisão proativa.

---

## 🔹 Tecnologias utilizadas
- **Python** → aplicação principal  
- **Isolation Forest** → detecção de anomalias  
- **Prometheus** → coleta de métricas  
- **Grafana** → visualização  
- **Kubernetes** → orquestração e deploy  

---

## 📂 Estrutura do projeto
- `app/` → Código da aplicação e Dockerfile  
- `docs/` → Documentação, tabelas e resultados do TCC  
- `k8s/` → Manifests para deploy em Kubernetes  

---

## 📌 Contexto acadêmico
Este projeto foi desenvolvido como parte de um **Trabalho de Conclusão de Curso**, evidenciando a aplicação prática de conceitos de **AIOps, DevOps e Observabilidade** em ambientes críticos do setor bancário.  
A proposta busca contribuir para a evolução da confiabilidade operacional e para a redução de riscos em serviços financeiros essenciais, demonstrando a relevância da integração entre **inteligência artificial e operações de TI**.

---

# 🚀 Etapa 1 – Empacotamento e Orquestração da Aplicação

Este documento descreve o roteiro de validação da aplicação **aiops-app** empacotada em contêineres Docker e orquestrada via Kubernetes, incluindo o uso de **Horizontal Pod Autoscaler (HPA)** e probes de saúde.

---

## 📂 Estrutura de arquivos

Na pasta `k8s/` estão os manifestos Kubernetes:

- `aiops-app-deployment.yaml` → Deployment da aplicação  
- `aiops-service.yaml` → Service para expor a aplicação  
- `aiops-hpa.yaml` → Horizontal Pod Autoscaler  
- `aiops-servicemonitor.yaml` → ServiceMonitor para Prometheus  
- `metrics-server-deployment.yaml` → Metrics Server  

---

## 📌 Roteiro de Validação

### 1. Aplicar os manifestos
```bash
kubectl apply -f k8s/aiops-app-deployment.yaml
kubectl apply -f k8s/aiops-service.yaml
kubectl apply -f k8s/aiops-hpa.yaml
kubectl apply -f k8s/aiops-servicemonitor.yaml
kubectl apply -f k8s/metrics-server-deployment.yaml

### 2. Verificar pods
```bash
kubectl get pods -n aiops-banco

### Saída esperada:
```bash
NAME                                                     READY   STATUS             RESTARTS         AGE
aiops-app-575fd79f44-f7nwd                               1/1     Running            3 (30m ago)      33m
aiops-app-575fd79f44-rvf76                               1/1     Running            3 (31m ago)      33m
alertmanager-prometheus-kube-prometheus-alertmanager-0   2/2     Running            6 (115m ago)     2d20h
prometheus-grafana-644d5c5bdf-klgh4                      3/3     Running            3 (115m ago)     2d
prometheus-kube-prometheus-operator-8465b57d95-zbznf     1/1     Running            5 (113m ago)     2d20h
prometheus-kube-state-metrics-cc8c6b4df-grqc9            1/1     Running            4 (113m ago)     2d20h
prometheus-prometheus-kube-prometheus-prometheus-0       2/2     Running            6 (115m ago)     2d20h
prometheus-prometheus-node-exporter-lt6kc                0/1     CrashLoopBackOff   99 (4m56s ago)   2d20h

### 3. Validar métricas
```bash
kubectl top pods -n aiops-banco

### Saída esperada:
```bash
NAME                                                     CPU(cores)   MEMORY(bytes)
aiops-app-575fd79f44-f7nwd                               37m          76Mi
aiops-app-575fd79f44-rvf76                               34m          76Mi
alertmanager-prometheus-kube-prometheus-alertmanager-0   2m           52Mi
prometheus-grafana-644d5c5bdf-klgh4                      13m          416Mi
prometheus-kube-prometheus-operator-8465b57d95-zbznf     12m          42Mi
prometheus-kube-state-metrics-cc8c6b4df-grqc9            2m           49Mi
prometheus-prometheus-kube-prometheus-prometheus-0       19m          320Mi

### 4. Conferir status do HPA
```bash
kubectl get hpa -n aiops-banco --watch

### Saída esperada:
```bash
NAME        REFERENCE              TARGETS        MINPODS   MAXPODS   REPLICAS   AGE
aiops-hpa   Deployment/aiops-app   cpu: 34%/70%   2         5         2          2d20h

### 👉 Inicialmente pode aparecer <unknown>. Após alguns ciclos, deve mostrar valores reais de CPU.

### 5. Gerar carga para forçar escalada
```bash
kubectl exec -it <busybox-pod> -n aiops-banco -- sh
