#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Расчет количества оборудования для технологической линии производства пельменей
"""

import sys
import io
import argparse
from math import ceil

# Исправление кодировки для Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')


# I. Технологическая линия изготовления пельменей
def calculate_line_productivity(q_sut: float, t: float) -> float:
    """
    Расчет производительности технологической линии
    
    Args:
        q_sut: суточная выработка готовой продукции, т
        t: продолжительность рабочей смены, ч
    
    Returns:
        Производительность технологической линии, т/ч
    """
    return q_sut / (2 * t)


def calculate_pelmen_machines(p_tl: float, p_pa: float) -> int:
    """
    Расчет количества пельменных автоматов
    
    Args:
        p_tl: производительность технологической линии, т/ч
        p_pa: производительность пельменного автомата, т/ч
    
    Returns:
        Количество пельменных автоматов
    """
    return ceil(p_tl / p_pa)


# II. Технологическая линия подготовки теста
def calculate_dough_line_productivity(p_tl: float, a_t: float) -> float:
    """
    Расчет производительности линии подготовки теста
    
    Args:
        p_tl: производительность технологической линии, т/ч
        a_t: массовая доля теста в готовой продукции, %
    
    Returns:
        Производительность линии подготовки теста, т/ч
    """
    return p_tl * a_t / 100


def calculate_dough_machines(p_tl_dough: float, p_tm: float) -> int:
    """
    Расчет количества тестомесильных машин
    
    Args:
        p_tl_dough: производительность линии подготовки теста, т/ч
        p_tm: производительность тестомесильной машины, т/ч
    
    Returns:
        Количество тестомесильных машин
    """
    return ceil(p_tl_dough / p_tm)


# III. Технологическая линия подготовки фарша
def calculate_filling_share(a_m: float, a_ya: float, a_s: float, a_sp: float) -> float:
    """
    Расчет массовой доли фарша в готовой продукции
    
    Args:
        a_m: массовая доля мяса, %
        a_ya: массовая доля яиц, %
        a_s: массовая доля соли, %
        a_sp: массовая доля специй, %
    
    Returns:
        Массовая доля фарша, %
    """
    return a_m + a_ya + a_s + a_sp


def calculate_filling_line_productivity(p_tl: float, a_f: float) -> float:
    """
    Расчет производительности линии подготовки фарша
    
    Args:
        p_tl: производительность технологической линии, т/ч
        a_f: массовая доля фарша в готовой продукции, %
    
    Returns:
        Производительность линии подготовки фарша, т/ч
    """
    return p_tl * a_f / 100


def calculate_cutters(p_tl_filling: float, p_k: float) -> int:
    """
    Расчет количества куттеров
    
    Args:
        p_tl_filling: производительность линии подготовки фарша, т/ч
        p_k: производительность куттера, т/ч
    
    Returns:
        Количество куттеров
    """
    return ceil(p_tl_filling / p_k)


def parse_arguments():
    """Парсинг аргументов командной строки"""
    parser = argparse.ArgumentParser(
        description='Расчет оборудования для производства пельменей',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Примеры использования:
  # Интерактивный режим
  python pelmeny_calculation.py
  
  # С параметрами командной строки
  python pelmeny_calculation.py --q_sut 5 --t 8 --a_t 60 --a_m 30 --a_ya 5 --a_s 2 --a_sp 3 --p_pa 0.2 --p_tm 0.15 --p_k 0.1
        """
    )
    
    parser.add_argument('--q_sut', type=float, help='Суточная выработка готовой продукции (т)')
    parser.add_argument('--t', type=float, help='Продолжительность рабочей смены (ч)')
    parser.add_argument('--a_t', type=float, help='Массовая доля теста в готовой продукции (%%)')
    parser.add_argument('--a_m', type=float, help='Массовая доля мяса (%%)')
    parser.add_argument('--a_ya', type=float, help='Массовая доля яиц (%%)')
    parser.add_argument('--a_s', type=float, help='Массовая доля соли (%%)')
    parser.add_argument('--a_sp', type=float, help='Массовая доля специй (%%)')
    parser.add_argument('--p_pa', type=float, help='Производительность пельменного автомата (т/ч)')
    parser.add_argument('--p_tm', type=float, help='Производительность тестомесильной машины (т/ч)')
    parser.add_argument('--p_k', type=float, help='Производительность куттера (т/ч)')
    
    return parser.parse_args()


def main():
    """Основная функция программы"""
    
    args = parse_arguments()
    
    print("=" * 70)
    print("РАСЧЕТ ОБОРУДОВАНИЯ ДЛЯ ПРОИЗВОДСТВА ПЕЛЬМЕНЕЙ")
    print("=" * 70)
    print()
    
    # Проверяем, заданы ли все параметры через командную строку
    all_params_provided = all([
        args.q_sut is not None, args.t is not None, args.a_t is not None,
        args.a_m is not None, args.a_ya is not None, args.a_s is not None,
        args.a_sp is not None, args.p_pa is not None, args.p_tm is not None,
        args.p_k is not None
    ])
    
    if all_params_provided:
        # Используем параметры из командной строки
        q_sut = args.q_sut
        t = args.t
        a_t = args.a_t
        a_m = args.a_m
        a_ya = args.a_ya
        a_s = args.a_s
        a_sp = args.a_sp
        p_pa = args.p_pa
        p_tm = args.p_tm
        p_k = args.p_k
        
        print("ИСХОДНЫЕ ДАННЫЕ (из командной строки):")
        print("-" * 70)
        print(f"Суточная выработка готовой продукции: {q_sut} т")
        print(f"Продолжительность рабочей смены: {t} ч")
        print(f"Массовая доля теста: {a_t} %")
        print(f"Массовая доля мяса: {a_m} %")
        print(f"Массовая доля яиц: {a_ya} %")
        print(f"Массовая доля соли: {a_s} %")
        print(f"Массовая доля специй: {a_sp} %")
        print(f"Производительность пельменного автомата: {p_pa} т/ч")
        print(f"Производительность тестомесильной машины: {p_tm} т/ч")
        print(f"Производительность куттера: {p_k} т/ч")
    else:
        # Интерактивный ввод
        print("ВВОД ИСХОДНЫХ ДАННЫХ:")
        print("-" * 70)
        
        q_sut = args.q_sut if args.q_sut else float(input("Суточная выработка готовой продукции (т): "))
        t = args.t if args.t else float(input("Продолжительность рабочей смены (ч): "))
        a_t = args.a_t if args.a_t else float(input("Массовая доля теста в готовой продукции (%): "))
        
        print("\nКомпоненты фарша:")
        a_m = args.a_m if args.a_m else float(input("  Массовая доля мяса (%): "))
        a_ya = args.a_ya if args.a_ya else float(input("  Массовая доля яиц (%): "))
        a_s = args.a_s if args.a_s else float(input("  Массовая доля соли (%): "))
        a_sp = args.a_sp if args.a_sp else float(input("  Массовая доля специй (%): "))
        
        print("\nПроизводительность оборудования:")
        p_pa = args.p_pa if args.p_pa else float(input("  Производительность пельменного автомата (т/ч): "))
        p_tm = args.p_tm if args.p_tm else float(input("  Производительность тестомесильной машины (т/ч): "))
        p_k = args.p_k if args.p_k else float(input("  Производительность куттера (т/ч): "))
    
    # Расчеты
    print()
    print("=" * 70)
    print("РЕЗУЛЬТАТЫ РАСЧЕТОВ:")
    print("=" * 70)
    print()
    
    # I. Технологическая линия изготовления пельменей
    p_tl = calculate_line_productivity(q_sut, t)
    n_pa = calculate_pelmen_machines(p_tl, p_pa)
    
    print("I. ТЕХНОЛОГИЧЕСКАЯ ЛИНИЯ ИЗГОТОВЛЕНИЯ ПЕЛЬМЕНЕЙ:")
    print(f"   Производительность линии: {p_tl:.3f} т/ч")
    print(f"   Количество пельменных автоматов: {n_pa} шт.")
    print()
    
    # II. Технологическая линия подготовки теста
    p_tl_dough = calculate_dough_line_productivity(p_tl, a_t)
    n_tm = calculate_dough_machines(p_tl_dough, p_tm)
    
    print("II. ТЕХНОЛОГИЧЕСКАЯ ЛИНИЯ ПОДГОТОВКИ ТЕСТА:")
    print(f"    Производительность линии: {p_tl_dough:.3f} т/ч")
    print(f"    Количество тестомесильных машин: {n_tm} шт.")
    print()
    
    # III. Технологическая линия подготовки фарша
    a_f = calculate_filling_share(a_m, a_ya, a_s, a_sp)
    p_tl_filling = calculate_filling_line_productivity(p_tl, a_f)
    n_k = calculate_cutters(p_tl_filling, p_k)
    
    print("III. ТЕХНОЛОГИЧЕСКАЯ ЛИНИЯ ПОДГОТОВКИ ФАРША:")
    print(f"     Массовая доля фарша: {a_f:.2f} %")
    print(f"     Производительность линии: {p_tl_filling:.3f} т/ч")
    print(f"     Количество куттеров: {n_k} шт.")
    print()
    
    # Итоговая сводка
    print("=" * 70)
    print("ИТОГОВАЯ СВОДКА:")
    print("=" * 70)
    print(f"Пельменных автоматов:     {n_pa} шт.")
    print(f"Тестомесильных машин:     {n_tm} шт.")
    print(f"Куттеров:                 {n_k} шт.")
    print("=" * 70)


if __name__ == "__main__":
    main()

