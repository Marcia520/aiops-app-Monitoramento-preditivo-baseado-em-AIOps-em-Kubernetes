### Monitoramento preditivo baseado em AIOps em Kubernetes

Projeto desenvolvido por **Marcia**, aplicando práticas de Engenharia de Software e DevOps para ambientes de monitoramento inteligente em Kubernetes.

Este repositório reúne o desenvolvimento do **Trabalho de Conclusão de Curso (TCC)** do **MBA Engenharia de Software - USP/ESALQ** cujo objetivo geral é **propor, implementar e validar uma solução de monitoramento preditivo baseada em AIOps aplicada a ambientes Kubernetes no setor bancário**, com foco em:

- Monitoramento preditivo
- Observabilidade completa
- Detecção de anomalias
- Automação de respostas
- Escalabilidade dinâmica
- Antecipação de falhas operacionais
- Redução do tempo de resposta a incidentes
- Aumento da resiliência de serviços críticos 

---

#### 🎯 Objetivo
Demonstrar como técnicas de **Machine Learning** (em especial o algoritmo **Isolation Forest**) podem ser integradas a ferramentas de observabilidade (**Prometheus** e **Grafana**) em ambientes **Kubernetes**, aplicadas ao contexto bancário, para identificar comportamentos anômalos e apoiar a tomada de decisão proativa.

##### 📑 Etapas

- [Etapa 1 – Empacotamento e Orquestração](./Etapa-1-Empacotamento-e-Orquestração/README.md)
- [Etapa 2 – Observabilidade com Prometheus e Grafana](./Etapa-2-Observabilidade/README.md)
- [Etapa 3 – IA para Detecção de Anomalias](./Etapa-3-IA-para-Detecção-de-Anomalias/README.md)
- [Etapa 4 – Avaliação e Simulações](./Etapa-4-Avaliação-e-Simulações/README.md)

---

#### 🔹 Tecnologias utilizadas

##### 📌 Linguagens e Frameworks
- **Python 3.10** → linguagem principal da aplicação  
- **Flask** → framework para API RESTful  
- **Scikit-learn** → biblioteca para aprendizado de máquina (Isolation Forest)  

##### 📌 Infraestrutura e Orquestração
- **Docker** → empacotamento da aplicação em contêineres  
- **Kubernetes** → orquestração e deploy  
- **Docker Desktop** → ambiente local para simular o cluster Kubernetes  
- **Helm** → instalação de Prometheus e Grafana via charts  

##### 📌 Observabilidade
- **Prometheus** → coleta de métricas  
- **Grafana** → visualização e dashboards  
- **PromQL** → consultas para análise de métricas  
- **ServiceMonitor** → integração Prometheus Operator para coleta estruturada  

##### 📌 Inteligência Artificial
- **Isolation Forest** → detecção de anomalias não supervisionada  
- **Random Forest** → modelo complementar discutido  
- **LSTM (Long Short-Term Memory)** → redes neurais para séries temporais (complementar)  

##### 📌 Engenharia de Software e DevOps
- **GitOps** → versionamento declarativo da infraestrutura  
- **TDD (Test-Driven Development)** → validação automatizada dos modelos  
- **DDD (Domain-Driven Design)** → organização dos microsserviços por domínios funcionais  
- **mTLS (mutual TLS)** → autenticação mútua e comunicação segura entre serviços
- **GitHub** como fonte única da verdade (GitOps). 
- **Ferramentas de CI/CD** para automação de deploys e testes.  

---

#### 📂 Estrutura do projeto

##### app/ → código-fonte da aplicação
- `app.py`
- `Dockerfile`
- `requirements.txt`

##### Etapa-1-Empacotamento-Orquestracao/
- **docs/** → prints da instalação e configuração (Docker, Kubernetes, Git, GitHub)
- `README.md` → explicação da etapa

##### Etapa-2-Observabilidade/
- **k8s/** → manifests de Prometheus, Grafana, ServiceMonitor
- **docs/** → prints de métricas, dashboards, HPA
- `README.md` → explicação da etapa

##### Etapa-3-Anomalias-Automacao/
- **k8s/** → YAMLs de alertas e detecção de anomalias (`alertmanager-config.yaml`, `anomaly-detector.yaml`)
- **docs/** → prints dos dashboards de anomalias
- `README.md` → explicação da etapa

##### Etapa-4-Resultados-Conclusoes/
- **docs/** → prints finais, gráficos comparativos, conclusões
- `README.md` → resumo dos resultados e análise de resiliência 


#### 📌 Contexto acadêmico
Este projeto foi desenvolvido como parte de um **Trabalho de Conclusão de Curso**, evidenciando a aplicação prática de conceitos de **AIOps, DevOps e Observabilidade** em ambientes críticos do setor bancário.  
A proposta busca contribuir para a evolução da confiabilidade operacional e para a redução de riscos em serviços financeiros essenciais, demonstrando a relevância da integração entre **inteligência artificial e operações de TI**.

# 🔐 Monitoramento Preditivo baseado em AIOps em Kubernetes
### Autora: Márcia Aparecida Rodrigues de Sousa

Este repositório contém implementações práticas do meu TCC:  
**“Monitoramento preditivo com inteligência artificial em ambientes Kubernetes: uma abordagem aplicada ao setor bancário”**.  

O projeto integra **Kubernetes, Prometheus, Grafana e algoritmos de IA** (Isolation Forest, Random Forest, LSTM) para detecção de anomalias e automação de respostas operacionais.

---

## ▶️ Executar os Notebooks no Google Colab

Clique nos botões abaixo para abrir e executar diretamente no Colab:

### Etapa 1 – Configuração do Ambiente Kubernetes
*(manifests, HPA, probes, simulações de falhas)*  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Marcia520/aiops-app-Monitoramento-preditivo-baseado-em-AIOps-em-Kubernetes/blob/main/Etapa-1-Kubernetes/ambiente_kubernetes.ipynb)

---

### Etapa 2 – Observabilidade com Prometheus e Grafana
*(coleta de métricas, dashboards, análise em tempo real)*  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Marcia520/aiops-app-Monitoramento-preditivo-baseado-em-AIOps-em-Kubernetes/blob/main/Etapa-2-Observabilidade/prometheus_grafana.ipynb)

---

### Etapa 3 – IA para Detecção de Anomalias

#### Isolation Forest – Acessos
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Marcia520/aiops-app-Monitoramento-preditivo-baseado-em-AIOps-em-Kubernetes/blob/main/Etapa-3-IA-para-Detecção-de-Anomalias/notebooks/isolationforest_acessos.ipynb)

#### Isolation Forest – Serviços
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Marcia520/aiops-app-Monitoramento-preditivo-baseado-em-AIOps-em-Kubernetes/blob/main/Etapa-3-IA-para-Detecção-de-Anomalias/notebooks/isolationforest_servicos.ipynb)

#### Random Forest – Comparativo
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Marcia520/aiops-app-Monitoramento-preditivo-baseado-em-AIOps-em-Kubernetes/blob/main/Etapa-3-IA-para-Detecção-de-Anomalias/notebooks/randomforest_servicos.ipynb)

#### LSTM – Séries Temporais
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Marcia520/aiops-app-Monitoramento-preditivo-baseado-em-AIOps-em-Kubernetes/blob/main/Etapa-3-IA-para-Detecção-de-Anomalias/notebooks/lstm_servicos.ipynb)

---

## 📊 Estrutura do Projeto

- **datasets/** → scripts de geração de dados sintéticos (acessos e métricas operacionais)  
- **dashboards/** → arquivos JSON dos dashboards do Grafana  
- **Etapa-1-Kubernetes/** → manifests e notebook de configuração do ambiente  
- **Etapa-2-Observabilidade/** → configuração Prometheus/Grafana  
- **Etapa-3-IA-para-Detecção-de-Anomalias/** → notebooks de IA (Isolation Forest, Random Forest, LSTM)  

---

## 🚀 Como Executar Localmente

1. Clone este repositório:
   ```bash
   git clone https://github.com/Marcia520/aiops-app-Monitoramento-preditivo-baseado-em-AIOps-em-Kubernetes.git
   cd aiops-app-Monitoramento-preditivo-baseado-em-AIOps-em-Kubernetes

