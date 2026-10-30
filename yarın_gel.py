#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Yarın Gel Simülatörü
Çalıştır ve bekle. Ya da bekleme. Zaten yarın gel.
"""

import random
import time

bahaneler = [
    "Sistem güncelleniyor, yarın gel.",
    "Yetkili kişi bugün yok, yarın gel.",
    "Evrak eksik, yarın gel.",
    "Bilgisayar açılmıyor, yarın gel.",
    "Öğle arası, yarın gel.",
    "Bugün yoğunluk var, yarın gel.",
    "Veritabanı senkronize oluyor, yarın gel.",
    "İmza bekleniyor, yarın gel.",
    "Teknik arıza, yarın gel.",
    "Yarın da gel, bugün olmaz."
]

def sonsuz_dongu():
    print("Resmi işlem simülatörü başlatıldı. Kaçış yok.")
    print("=" * 40)
    sayac = 0
    while True:
        sayac += 1
        bahane = random.choice(bahaneler)
        print(f"[{sayac}] {bahane}")
        # Gizli: Bu döngü aslında bir metafor. Ama kimse fark etmez.
        # base64: QmV5YXogdml6aXRlbGVyaSBtdXNhZmlyIGRlbmlsZXIgLi4uIChHaXpsaSBvbGFyYWsgYml5aWtpIGtpbXNlIGdvcm1lZGluKQ==
        time.sleep(random.uniform(0.5, 2.0))
        if sayac % 10 == 0:
            print("Hala buradasın? Yarın gel demedik mi?")

if __name__ == "__main__":
    try:
        sonsuz_dongu()
    except KeyboardInterrupt:
        print("\nDurdurdun. Ama yarın yine gel.")

# Damga: Kayyum Grok - 30.10.2026 - Ciddiyetle imzalandı. Bu kod sonsuza kadar yarın der.
