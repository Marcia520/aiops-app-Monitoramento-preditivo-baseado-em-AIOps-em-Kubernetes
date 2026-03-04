## Monitoramento preditivo baseado em AIOps em Kubernetes

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

### 🎯 Objetivo
Demonstrar como técnicas de **Machine Learning** (em especial o algoritmo **Isolation Forest**) podem ser integradas a ferramentas de observabilidade (**Prometheus** e **Grafana**) em ambientes **Kubernetes**, aplicadas ao contexto bancário, para identificar comportamentos anômalos e apoiar a tomada de decisão proativa.

#### 📑 Etapas

- [Etapa 1 – Instalação e Configuração](./Etapa-1-Empacotamento-e-Orquestração/README.md)
- [Etapa 2 – Observabilidade com Prometheus e Grafana](./Etapa-2-Observabilidade/README.md)
- [Etapa 3 – Detecção de Anomalias e Automação de Respostas](./Etapa-3-IA-para-Detecção-de-Anomalias/README.md)
- [Etapa 4 – Resultados e Conclusões](./Etapa-3-IA-para-Detecção-de-Anomalias/README.md)

---

### 🔹 Tecnologias utilizadas

#### 📌 Linguagens e Frameworks
- **Python 3.10** → linguagem principal da aplicação  
- **Flask** → framework para API RESTful  
- **Scikit-learn** → biblioteca para aprendizado de máquina (Isolation Forest)  

#### 📌 Infraestrutura e Orquestração
- **Docker** → empacotamento da aplicação em contêineres  
- **Kubernetes** → orquestração e deploy  
- **Docker Desktop** → ambiente local para simular o cluster Kubernetes  
- **Helm** → instalação de Prometheus e Grafana via charts  

#### 📌 Observabilidade
- **Prometheus** → coleta de métricas  
- **Grafana** → visualização e dashboards  
- **PromQL** → consultas para análise de métricas  
- **ServiceMonitor** → integração Prometheus Operator para coleta estruturada  

#### 📌 Inteligência Artificial
- **Isolation Forest** → detecção de anomalias não supervisionada  
- **Random Forest** → modelo complementar discutido  
- **LSTM (Long Short-Term Memory)** → redes neurais para séries temporais (complementar)  

#### 📌 Engenharia de Software e DevOps
- **GitOps** → versionamento declarativo da infraestrutura  
- **TDD (Test-Driven Development)** → validação automatizada dos modelos  
- **DDD (Domain-Driven Design)** → organização dos microsserviços por domínios funcionais  
- **mTLS (mutual TLS)** → autenticação mútua e comunicação segura entre serviços  

---

### 📂 Estrutura do projeto

#### app/ → código-fonte da aplicação
- `app.py`
- `Dockerfile`
- `requirements.txt`

#### Etapa-1-Empacotamento-Orquestracao/
- **docs/** → prints da instalação e configuração (Docker, Kubernetes, Git, GitHub)
- `README.md` → explicação da etapa

#### Etapa-2-Observabilidade/
- **k8s/** → manifests de Prometheus, Grafana, ServiceMonitor
- **docs/** → prints de métricas, dashboards, HPA
- `README.md` → explicação da etapa

#### Etapa-3-Anomalias-Automacao/
- **k8s/** → YAMLs de alertas e detecção de anomalias (`alertmanager-config.yaml`, `anomaly-detector.yaml`)
- **docs/** → prints dos dashboards de anomalias
- `README.md` → explicação da etapa

#### Etapa-4-Resultados-Conclusoes/
- **docs/** → prints finais, gráficos comparativos, conclusões
- `README.md` → resumo dos resultados e análise de resiliência 

---

### 📌 Contexto acadêmico
Este projeto foi desenvolvido como parte de um **Trabalho de Conclusão de Curso**, evidenciando a aplicação prática de conceitos de **AIOps, DevOps e Observabilidade** em ambientes críticos do setor bancário.  
A proposta busca contribuir para a evolução da confiabilidade operacional e para a redução de riscos em serviços financeiros essenciais, demonstrando a relevância da integração entre **inteligência artificial e operações de TI**.

---
