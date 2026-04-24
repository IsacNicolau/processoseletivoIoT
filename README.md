# Projeto IoT – Controle de LED com Estados

## 👤 Identificação
Nome: Cicero Isac da Silva Farias  
GitHub: IsacNicolau  

---

## 1️⃣ Visão Geral
Este projeto implementa um sistema embarcado para controle de um LED com três modos de operação (desligado, ligado e piscando), utilizando um botão como interface de entrada do usuário.

A cada acionamento do botão, o sistema alterna entre os estados.

---

## 2️⃣ Arquitetura
O sistema foi desenvolvido utilizando uma máquina de estados, controlada por um loop principal contínuo.

Fluxo:
- O botão é monitorado continuamente
- Ao detectar um pressionamento (borda de descida), o estado é atualizado
- O comportamento do LED depende do estado atual

Estados:
- OFF: LED desligado
- ON: LED ligado continuamente
- BLINK: LED piscando com temporização controlada

---

## 3️⃣ Componentes
- Raspberry Pi Pico (simulado no Wokwi)
- LED (saída visual)
- Botão (entrada do usuário)

---

## 4️⃣ Decisões Técnicas
- Uso de máquina de estados para facilitar escalabilidade
- Implementação de debounce simples via software
- Separação da lógica em funções para melhor organização
- Uso de temporização não bloqueante no modo BLINK

---

## 5️⃣ Resultados
A simulação apresenta funcionamento correto, com alternância entre os três estados conforme interação com o botão.

O sistema executa sem erros na simulação e nas GitHub Actions.

---

## 6️⃣ Comentários
Como melhorias futuras, poderiam ser implementados:
- Debounce mais robusto (ex: filtro por tempo)
- Uso de interrupções ao invés de polling
- Expansão para múltiplos LEDs ou sensores