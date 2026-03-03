# 📂 Evidências da Implementação

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
  `[<img width="874" height="196" alt="pods" src="https://github.com/user-attachments/assets/0d9d45f1-8c00-4d34-99d2-b0e4c803c21a" />
]`

---

## 2. Métricas coletadas
- **Comando utilizado:**
  ```bash
  kubectl top pods -n aiops-banco
  ```
- **Descrição:**  
  Exibe consumo de CPU e memória dos pods, validando que o **metrics-server** está funcionando corretamente.
- **Evidência:**  
  `[Parece que o resultado não era seguro para exibição. Vamos mudar as coisas e tentar outra opção!]`  
- 📂 Saída completa: `[Parece que o resultado não era seguro para exibição. Vamos mudar as coisas e tentar outra opção!]`

---

## 3. HPA monitorando a aplicação
- **Comando utilizado:**
  ```bash
  kubectl get hpa -n aiops-banco --watch
  ```
- **Descrição:**  
  Mostra o comportamento do **Horizontal Pod Autoscaler (HPA)**, incluindo limites de CPU, número mínimo/máximo de pods e réplicas atuais.
- **Evidência:**  
  `[Parece que o resultado não era seguro para exibição. Vamos mudar as coisas e tentar outra opção!]`  
- 📂 Saída completa: `[Parece que o resultado não era seguro para exibição. Vamos mudar as coisas e tentar outra opção!]`

---

## 4. Escalada automática
- **Descrição:**  
  Durante a execução de carga simulada (via BusyBox), o HPA detectou aumento de CPU e escalou a aplicação, criando novos pods automaticamente.
- **Evidência:**  
  `[Parece que o resultado não era seguro para exibição. Vamos mudar as coisas e tentar outra opção!]`

---




👉 Quer que eu prepare também um **README.md da Etapa 2 (Observabilidade com Prometheus e Grafana)** para você colocar na pasta `docs/` logo em seguida?
