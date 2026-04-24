import time

# Simulação de pinos (Wokwi normalmente usa machine ou similar dependendo da placa)
try:
    from machine import Pin
except ImportError:
    # fallback para simulação local
    class Pin:
        IN = 0
        OUT = 1
        PULL_UP = 2

        def __init__(self, pin, mode, pull=None):
            self.value_state = 1

        def value(self, v=None):
            if v is None:
                return self.value_state
            self.value_state = v


# Configuração dos pinos
led = Pin(2, Pin.OUT)
button = Pin(3, Pin.IN, Pin.PULL_UP)

# Estados
STATE_OFF = 0
STATE_ON = 1
STATE_BLINK = 2

state = STATE_OFF
last_button = 1


def set_led(value):
    led.value(value)


def button_pressed():
    global last_button
    current = button.value()
    pressed = last_button == 1 and current == 0
    last_button = current

    if pressed:
        time.sleep(0.05)  # debounce simples

    return pressed


def led_off():
    set_led(0)


def led_on():
    set_led(1)


blink_state = 0
last_blink_time = 0

def led_blink():
    global blink_state, last_blink_time
    now = time.time()

    if now - last_blink_time > 0.3:
        blink_state = not blink_state
        set_led(blink_state)
        last_blink_time = now


# Loop principal
while True:
    if button_pressed():
        state = (state + 1) % 3

    if state == STATE_OFF:
        led_off()
    elif state == STATE_ON:
        led_on()
    elif state == STATE_BLINK:
        led_blink()

    time.sleep(0.1)