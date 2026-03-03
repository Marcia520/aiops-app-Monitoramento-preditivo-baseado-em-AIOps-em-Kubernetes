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
  ![docker](docker.png)

- **Kubernetes ativado ativado no Docker Desktop e nó em execução:**  
  ![kubernetes](kubernetes.png)

  **Cluster ativo (nó em execução):**  
  ![cluster_ativo](cluster_ativo.png)

  - **Namespace criado (aiops-banco):**  
  ![namespace](/namespace.png)

- **Metrics-server funcionando (CPU/Memória):**  
  ![metrics_server](metrics_server.png)

- **Git instalado e configurado localmente:**  
  ![git](git.png)

  **Repositório conectado ao GitHub:**  
  ![github](github.png)

  
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

