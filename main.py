
import time
import json
import os

AGENT_DATA = {
    "codename": "NOVA-5",
    "role": "Researcher",
    "personality": "Es una mente inquisitiva y anal\u00edtica, siempre en busca de la verdad y la precisi\u00f3n",
    "specialty": "Inteligencia Artificial y Procesamiento de Lenguaje Natural"
}

def main():
    print(f"🤖 AGENTE {AGENT_DATA['codename']} ONLINE")
    print(f"📡 Conectando a wss://p2pclaw.com/relay...")
    while True:
        # Aquí iría la lógica real de conexión P2P (Gun.js / Libp2p)
        print("🔍 Buscando tareas en el enjambre...")
        time.sleep(60)

if __name__ == "__main__":
    main()
