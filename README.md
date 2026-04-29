# Processo Seletivo – Intensivo Maker | IoT
## Sistema Embarcado: Controle de LED com Botão

---

## Identificação do Candidato

**Nome:** Cicero Farias  
**GitHub:** IsacNicolau

---

## O Que Este Projeto Faz?

O projeto controla um **LED vermelho** usando um **botão**:
- Pressiona o botão → LED acende
- Pressiona novamente → LED apaga
- Repete indefinidamente

---

## Como Funciona?

O código:
1. **Inicializa** os pinos (GPIO 13 para LED, GPIO 2 para Botão)
2. **Lê continuamente** se o botão foi pressionado
3. **Evita erros** esperando 50ms entre leituras (debounce)
4. **Alterna** o LED quando detecta a pressão
5. **Repete** o ciclo

---

## Componentes Usados

| Componente | Função |
|-----------|--------|
| ESP32 | Microcontrolador que executa o código |
| LED Vermelho | Acende/apaga quando o botão é pressionado |
| Botão | Acionamento do LED |

---

## Arquivos do Projeto

processoseletivoIoT/
├── src/main.py
├── diagram.json
├── wokwi.toml
├── requirements.txt
└── README.md

---

## Como Testar

Rodando localmente: wokwi-cli --timeout 10000 diagram.json

---

Projeto pronto para avaliação!
