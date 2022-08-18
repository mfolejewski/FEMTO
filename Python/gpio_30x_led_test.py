import time

from machine import mem32, Timer

BANK0_base_address = 0x40014000
offset_GPIO25_CTRL = 0xcc

SIO_base_address = 0xd0000000
offset_GPIO_IN = 0x4
offset_GPIO_OUT = 0x10
offset_GPIO_OUT_SET = 0x14
offset_GPIO_OUT_CLR = 0x18
offset_GPIO_OUT_XOR = 0x1c
offset_GPIO_OE = 0x20
offset_GPIO_OE_SET = 0x24
offset_GPIO_OE_CLR = 0x28
offset_GPIO_OE_XOR = 0x2c

LED_MIN = 0
LED_MAX = 29
LED_MASK = 0x3fffffff

mem32[BANK0_base_address + offset_GPIO25_CTRL] = 5
for i in range(LED_MIN, LED_MAX + 1):
    mem32[BANK0_base_address + 4 + 8 * i] = 5

mem32[SIO_base_address + offset_GPIO_OE_SET] = LED_MASK
mem32[SIO_base_address + offset_GPIO_OUT_CLR] = LED_MASK

def blink_led(i):
    global SIO_base_address, offset_GPIO_OUT_XOR
    mem32[SIO_base_address + offset_GPIO_OUT_CLR] = LED_MASK
    mem32[SIO_base_address + offset_GPIO_OUT_SET] = i

cnt = LED_MIN

while True:
    cnt += 1
    if cnt > LED_MAX:
        cnt = LED_MIN
    blink_led((1 << cnt) & LED_MASK)
    time.sleep(0.1)
