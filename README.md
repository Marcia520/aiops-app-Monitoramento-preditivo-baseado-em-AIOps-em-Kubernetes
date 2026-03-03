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

### 📌 Linguagens e Frameworks
- **Python 3.10** → linguagem principal da aplicação  
- **Flask** → framework para API RESTful  
- **Scikit-learn** → biblioteca para aprendizado de máquina (Isolation Forest)  

### 📌 Infraestrutura e Orquestração
- **Docker** → empacotamento da aplicação em contêineres  
- **Kubernetes** → orquestração e deploy  
- **Docker Desktop** → ambiente local para simular o cluster Kubernetes  
- **Helm** → instalação de Prometheus e Grafana via charts  

### 📌 Observabilidade
- **Prometheus** → coleta de métricas  
- **Grafana** → visualização e dashboards  
- **PromQL** → consultas para análise de métricas  
- **ServiceMonitor** → integração Prometheus Operator para coleta estruturada  

### 📌 Inteligência Artificial
- **Isolation Forest** → detecção de anomalias não supervisionada  
- **Random Forest** → modelo complementar discutido  
- **LSTM (Long Short-Term Memory)** → redes neurais para séries temporais (complementar)  

### 📌 Engenharia de Software e DevOps
- **GitOps** → versionamento declarativo da infraestrutura  
- **TDD (Test-Driven Development)** → validação automatizada dos modelos  
- **DDD (Domain-Driven Design)** → organização dos microsserviços por domínios funcionais  
- **mTLS (mutual TLS)** → autenticação mútua e comunicação segura entre serviços  

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

# 🚀 Roteiros de Validação

---

## Etapa 1 – Empacotamento e orquestração da aplicação
```bash
kubectl apply -f k8s/aiops-app-deployment.yaml
kubectl apply -f k8s/aiops-service.yaml
kubectl apply -f k8s/aiops-hpa.yaml
kubectl apply -f k8s/aiops-servicemonitor.yaml
kubectl apply -f k8s/metrics-server-deployment.yaml
```
👉 Garante que todos os manifestos estão aplicados no cluster Kubernetes rodando no **Docker Desktop**.

---

## Etapa 2 – Verificar pods
```bash
kubectl get pods -n aiops-banco
```

**Saída esperada:**
```
NAME                                                     READY   STATUS             RESTARTS        AGE
aiops-app-575fd79f44-f7nwd                               1/1     Running            3 (62m ago)     65m
aiops-app-575fd79f44-rvf76                               1/1     Running            3 (63m ago)     66m
alertmanager-prometheus-kube-prometheus-alertmanager-0   2/2     Running            6 (147m ago)    2d20h
prometheus-grafana-644d5c5bdf-klgh4                      3/3     Running            3 (147m ago)    2d
prometheus-kube-prometheus-operator-8465b57d95-zbznf     1/1     Running            5 (145m ago)    2d20h
prometheus-kube-state-metrics-cc8c6b4df-grqc9            1/1     Running            4 (145m ago)    2d20h
prometheus-prometheus-kube-prometheus-prometheus-0       2/2     Running            6 (147m ago)    2d20h
prometheus-prometheus-node-exporter-lt6kc                0/1     CrashLoopBackOff   106 (89s ago)   2d20h
```
---

## Etapa 3 – Validar métricas
```bash
kubectl top pods -n aiops-banco
```

**Saída esperada:**
```
NAME                                                     CPU(cores)   MEMORY(bytes)
aiops-app-575fd79f44-f7nwd                               35m          76Mi
aiops-app-575fd79f44-rvf76                               37m          76Mi
alertmanager-prometheus-kube-prometheus-alertmanager-0   1m           51Mi
prometheus-grafana-644d5c5bdf-klgh4                      11m          416Mi
prometheus-kube-prometheus-operator-8465b57d95-zbznf     7m           41Mi
prometheus-kube-state-metrics-cc8c6b4df-grqc9            3m           49Mi
prometheus-prometheus-kube-prometheus-prometheus-0       15m          328Mi
```

👉 Confirma que o **metrics-server** está funcionando corretamente.

---

## Etapa 4 – Conferir status do HPA
```bash
kubectl get hpa -n aiops-banco --watch
```

**Saída esperada:**
```
NAME        REFERENCE              TARGETS        MINPODS   MAXPODS   REPLICAS   AGE
aiops-hpa   Deployment/aiops-app   cpu: 34%/70%   2         5         2          2d20h
```

👉 Inicialmente pode aparecer `<unknown>`. Após alguns ciclos, deve mostrar valores reais de CPU.

---

## Etapa 5 – Gerar carga para forçar escalada
Crie um pod BusyBox (se não existir):
```bash
kubectl run busybox --image=busybox:1.28 --restart=Never -n aiops-banco -- sleep 3600
```

Entre no pod:
```bash
kubectl exec -it busybox -n aiops-banco -- sh
```

Rode o loop de carga:
```sh
while true; do wget -q -O- http://aiops-service:8000/; done
```

👉 Isso aumenta o uso de CPU e força o HPA a escalar.

---

## Etapa 6 – Validar escalada automática
```bash
kubectl get pods -n aiops-banco
```

**Saída esperada (após carga):**
```
NAME                          READY   STATUS    RESTARTS   AGE
aiops-app-575fd79f44-f7nwd                               1/1     Running            3 (67m ago)     69m
aiops-app-575fd79f44-rvf76                               1/1     Running            3 (68m ago)     70m
alertmanager-prometheus-kube-prometheus-alertmanager-0   2/2     Running            6 (152m ago)    2d20h
busybox                                                  1/1     Running            0               2m2s
prometheus-grafana-644d5c5bdf-klgh4                      3/3     Running            3 (152m ago)    2d
prometheus-kube-prometheus-operator-8465b57d95-zbznf     1/1     Running            5 (149m ago)    2d20h
prometheus-kube-state-metrics-cc8c6b4df-grqc9            1/1     Running            4 (149m ago)    2d20h
prometheus-prometheus-kube-prometheus-prometheus-0       2/2     Running            6 (152m ago)    2d20h
prometheus-prometheus-node-exporter-lt6kc                0/1     CrashLoopBackOff   107 (61s ago)   2d20h
```

👉 Novos pods são criados automaticamente quando a CPU ultrapassa o limite configurado no HPA.

---


