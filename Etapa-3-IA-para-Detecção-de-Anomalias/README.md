### Etapa 3 – Aplicação de Algoritmos de IA para Detecção de Anomalias


#### 🔹 Introdução

Nesta etapa aplicamos **Inteligência Artificial orientada a Operações (AIOps)** para o monitoramento preditivo de ambientes bancários distribuídos em Kubernetes.  
O objetivo é detectar comportamentos atípicos em métricas operacionais e padrões de acesso, antecipando falhas, reduzindo o tempo de resposta a incidentes e fortalecendo a resiliência operacional.  
O algoritmo principal utilizado foi o **Isolation Forest**, complementado por discussões comparativas com **Random Forest** e **LSTM**, conforme fundamentação teórica do TCC.

---

#### 🔹 Fonte de Dados

Para validar os modelos, foram utilizados **dados sintéticos**, garantindo conformidade com a **LGPD** e reprodutibilidade científica.

- **Conjunto Operacional:** métricas de serviços críticos (autenticação, emissão de boletos, processamento de pagamentos, transações e transferências).  
  - Variáveis: uso de CPU, memória e latência.  
  - Processamento: normalização via *StandardScaler*.  

- **Conjunto de Acessos:** 5.000 registros simulados.  
  - Atributos: identificador do cliente, país de origem, tipo de dispositivo, quantidade de acessos e horário.  
  - Objetivo: detectar acessos fraudulentos (bots, horários incomuns, alta frequência, geolocalização divergente).  

---

#### 🔹 Algoritmos Aplicados

- **Isolation Forest (principal):** não supervisionado, eficaz em cenários sem dados rotulados.
  Embora o **Isolation Forest** tenha sido o algoritmo principal implementado nesta etapa, o estudo também discutiu modelos amplamente utilizados na literatura, como **Random Forest** e **Long Short-Term Memory (LSTM)**.   
- O **Random Forest** foi considerado como alternativa supervisionada, útil em cenários com dados rotulados e exigência de explicabilidade.  
- O **LSTM** foi discutido como modelo especializado em séries temporais, capaz de prever picos de carga e tendências operacionais.  
Esses modelos não foram implementados integralmente nesta etapa, mas sua análise comparativa reforça a fundamentação teórica e indica possíveis extensões futuras da abordagem proposta.  

---

#### 🔹 Implementação
- Scripts em Python (Flask, Scikit-learn, TensorFlow/Keras).  
- Métrica personalizada `aiops_anomaly_score` exposta via endpoint `/metrics`.  
- Integração com **Prometheus** e **Grafana** para coleta e visualização em tempo real.  
- Dashboards configurados para destacar serviços e acessos classificados como anômalos.  

---

#### 🔹 Bibliotecas Utilizadas
- **Scikit-learn** → biblioteca de aprendizado de máquina utilizada para implementar o algoritmo Isolation Forest.  
- **Pandas / NumPy** → manipulação e análise de dados.  
- **Matplotlib** → geração de gráficos e visualizações.  

---

#### 🔹 Experimentos Realizados

#### 1. Detecção de Anomalias em Serviços Bancários
- **Contexto:** análise de métricas operacionais (CPU, memória, latência) de serviços críticos como autenticação, boletos e transações.  
- **Objetivo:** identificar serviços com consumo anômalo de recursos.  
- **Script:** `scripts/isolationforest_servicos.py`  
- **Saída esperada:** tabela com serviços classificados como **Normais (1)** ou **Anômalos (-1)**, além de gráfico de dispersão.

**Resultado:**

| Serviço              | Uso de CPU | Uso de Memória | Latência (ms) | Status   |
|----------------------|------------|----------------|---------------|----------|
| Autenticação         | 23.4%      | 156MB          | 89            | Normal   |
| Processamento Pagto  | 45.6%      | 234MB          | 156           | Normal   |
| Transações           | 82.3%      | 467MB          | 345           | Anômalo  |
| Transferência Fundos | 76.8%      | 423MB          | 289           | Anômalo  |

![Anomalia Serviços](docs/anomalias-servicos.png)

---

#### 2. Detecção de Acessos Fraudulentos

- **Contexto:** simulação de 5.000 registros de acessos com atributos como país, cidade, dispositivo, quantidade de acessos e horário.  
- **Objetivo:** identificar acessos suspeitos (bots, horários incomuns, geolocalização atípica).  
- **Script:** `scripts/isolationforest_acessos.py`  
- **Saída esperada:** gráfico com acessos normais (azul) e suspeitos (vermelho), além de tabela com os primeiros registros classificados como **ALERTA**.

**Resultado:**

| Padrão de Acesso       | Quantidade | Percentual | Características                  |
|-------------------------|------------|------------|----------------------------------|
| Horário Incomum (0h–5h) | 85         | 34.0%      | Acessos em horário não comercial |
| Alta Frequência         | 67         | 26.8%      | Mais de 10 acessos/hora por IP   |
| Geolocalização Atípica  | 53         | 21.2%      | País diferente do cadastro       |
| Padrão de Bot           | 45         | 18.0%      | Comportamento automatizado       |

 ![Acessos Fraudulentos](docs/acessos-fraudulentos.png)

---

#### 🔹 Código de Execução

#### Serviços Bancários
```bash
cd Etapa-3-IA-para-Detecção-de-Anomalias/scripts
python isolationforest_servicos.py
```

#### Acessos Fraudulentos
```bash
cd Etapa-3-IA-para-Detecção-de-Anomalias/scripts
python isolationforest_acessos.py
```

---

#### 🔹 Saídas Esperadas
- **Serviços Bancários:** tabela com métricas e status (Normal/Anômalo) + gráfico de dispersão salvo em `docs/servicos-anomalias.png` 
- **Acessos Fraudulentos:** contagem de acessos normais e suspeitos + gráfico com pontos azuis (normais) e vermelhos (alerta) salvo em `docs/acessos-fraudulentos.png`.
  
---

#### 🔹 Notebooks
Para garantir a reprodutibilidade dos experimentos, foram criados notebooks interativos:  
- `notebooks/isolationforest_servicos.ipynb`  
- `notebooks/isolationforest_acessos.ipynb`  

#### Como rodar os notebooks:
1. Instale o Jupyter Notebook:
   ```bash
   pip install notebook
   ```
2. Entre na pasta notebooks:
   ```bash
   cd Etapa-3-IA-para-Detecção-de-Anomalias/notebooks
   ```
3. Inicie o Jupyter:
   ```bash
   python -m notebook
   ```
4. Abra os arquivos `.ipynb` e execute todas as células (**Kernel → Restart & Run All**) para visualizar os resultados.  
   - Os gráficos também são salvos automaticamente em `../docs/`.

---

#### 🔹 Requisitos de Instalação
Antes de executar os scripts ou notebooks, instale as dependências necessárias:

```bash
pip install pandas scikit-learn matplotlib numpy
```

---
#### 🔹 Conclusão
- A etapa consolidou a **metodologia**: definição dos dados, escolha dos algoritmos e integração com a arquitetura cloud native.  
- O *Isolation Forest* foi selecionado como modelo principal por equilibrar desempenho e eficiência computacional.  
- Essa base metodológica sustentou os testes práticos e resultados apresentados na Etapa 4.  

---




