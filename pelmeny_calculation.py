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
