"""
Sistema Embarcado: Controle de LED com Botão
Projeto para Wokwi Simulation
"""

import time
from machine import Pin

# Definir pinos
LED = Pin(13, Pin.OUT)      # LED no pino 13
BUTTON = Pin(2, Pin.IN)     # Botão no pino 2

# Estado inicial
led_state = False

def toggle_led():
    """Alterna o estado do LED"""
    global led_state
    led_state = not led_state
    LED.value(led_state)
    state_text = "ACESO" if led_state else "APAGADO"
    print(f"LED {state_text}")

def main():
    """Função principal"""
    print("Sistema Embarcado: Controle de LED")
    print("Pressione o botão para alternar o LED...")
    
    last_button_state = 0
    debounce_time = 0
    
    while True:
        current_button_state = BUTTON.value()
        
        # Debounce simples
        if current_button_state != last_button_state:
            debounce_time = time.ticks_ms()
        
        if time.ticks_ms() - debounce_time > 50:
            if current_button_state == 1 and last_button_state == 0:
                toggle_led()
            last_button_state = current_button_state
        
        time.sleep(0.01)

if __name__ == "__main__":
    main()
