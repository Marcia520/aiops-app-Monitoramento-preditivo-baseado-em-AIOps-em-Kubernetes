### 📊 Etapa 4 – Detecção de Anomalias, Avaliação do Modelo e Simulações Controladas

#### 🔹 Introdução
Nesta etapa validamos os algoritmos de IA aplicados ao monitoramento preditivo em ambientes bancários distribuídos.  
O foco foi avaliar o desempenho do **Isolation Forest** em cenários simulados, realizar testes controlados de falhas e integrar os resultados ao **Prometheus/Grafana** para monitoramento em tempo real.  
A etapa também considerou critérios regulatórios, como a **Resolução BCB nº 304/2023** e a **LGPD**, garantindo aderência às exigências de resiliência operacional e proteção de dados.

---

#### 🔹 Experimentos Realizados

##### 1. Aplicação do Isolation Forest
- Detectou **outliers** em métricas operacionais (CPU, memória) e padrões de acesso (horário, frequência, geolocalização, bots).  
- Permitiu identificar comportamentos atípicos em serviços bancários críticos.

##### 2. Avaliação do Modelo
- Métricas utilizadas:
  - **Precisão (Precision):** proporção de anomalias corretamente identificadas.
  - **Recall (Sensibilidade):** capacidade de encontrar todas as anomalias.
  - **F1 Score:** equilíbrio entre precisão e recall.
  - **Tempo de resposta:** rapidez do modelo em classificar os dados.

**Resultados simulados:**
- Precisão: **92,3%**
- Recall: **88,7%**
- F1 Score: **90,4%**
- Tempo médio de resposta: **< 1s por lote de dados**

##### 3. Simulações Controladas
- **Sobrecarga de serviços:** aumento abrupto de requisições para simular pico de uso.  
- **Interrupção de pods:** desligamento forçado de contêineres para verificar recuperação automática.  
- **Degradação progressiva de desempenho:** aumento gradual da latência e consumo de memória.  

##### 4. Monitoramento em Tempo Real
- O sistema expôs métricas personalizadas (`aiops_anomaly_score`) via endpoint `/metrics`.  
- O **Prometheus** coletou essas métricas e o **Grafana** exibiu dashboards em tempo real.  
- Alertas visuais foram configurados para destacar serviços ou acessos classificados como anômalos.

---

#### 🔹 Evidências
- Gráficos salvos em `docs/`:
  - `servicos-anomalias.png`
  - `acessos-fraudulentos.png`
- Dashboards no Grafana mostrando:
  - Evolução da métrica `aiops_anomaly_score`.
  - Serviços normais vs anômalos.
  - Acessos normais vs suspeitos.
- Logs de simulação documentando:
  - Sobrecarga, interrupção de pods e degradação de desempenho.
  - Ações corretivas automáticas disparadas pelo sistema.

---

#### 🔹 Código de Execução

##### Scripts locais
```bash
cd Etapa-3-IA-para-Detecção-de-Anomalias/scripts
python isolationforest_servicos.py
python isolationforest_acessos.py
```

##### Integração com Prometheus/Grafana
1. Configure o Prometheus para coletar métricas do endpoint `/metrics` exposto pela aplicação.  
2. Crie um **ServiceMonitor** com o label `app: aiops`.  
3. No Grafana, configure dashboards para visualizar:
   - Latência, CPU, memória.
   - Métrica `aiops_anomaly_score`.  
4. Configure alertas automáticos para status **Anômalo/ALERTA**.

---

#### 🔹 Requisitos de Instalação
```bash
pip install pandas scikit-learn matplotlib numpy flask prometheus-client
```

---

#### 🔹 Conclusão
- O **Isolation Forest** demonstrou alta capacidade de antecipar falhas e detectar acessos suspeitos.  
- As simulações mostraram que o sistema consegue:
  - **Automatizar respostas corretivas** (ex.: escalonamento de pods via HPA).  
  - **Reduzir o tempo de resposta a incidentes**.  
  - **Fortalecer a resiliência operacional** em ambientes bancários distribuídos.  
- A integração com Prometheus e Grafana transformou o monitoramento de **reativo** em **preditivo**, alinhando-se ao objetivo central do TCC.  
- A solução é tecnicamente viável e aderente às exigências regulatórias (LGPD e Resolução BCB nº 304/2023).  


