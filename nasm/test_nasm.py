#!/usr/bin/env python3

from myhdl import bin
from bits import nasm_test
import os.path
import warnings

def bad_symbol():
    warnings.warn(UserWarning("Tome cuidado para não estar usando o símbolo '#' no lugar de '$' ou '%'."))
    return 1

def test_add():
    ram = {0: 2, 1: 42}
    tst = {2: 44}
    assert nasm_test("add.nasm", ram, tst)
    assert bad_symbol() == 1

    ram = {0: 0, 1: 0}
    tst = {2: 0}
    assert nasm_test("add.nasm", ram, tst)
    assert bad_symbol() == 1

    ram = {0: 2, 1: 1}
    tst = {2: 3}
    assert nasm_test("add.nasm", ram, tst)
    assert bad_symbol() == 1


def test_mov():
    ram = {0: 33, 1: 44}
    tst = {0: 44, 1: 33, 3: 1}
    assert nasm_test("mov.nasm", ram, tst)
    assert bad_symbol() == 1


def test_sub():
    ram = {0: 2, 1: 4}
    tst = {2: 2}
    assert nasm_test("sub.nasm", ram, tst)
    assert bad_symbol() == 1

    
def test_max():
    ram = {0: 35, 1: 7}
    tst = {2: 35}
    assert nasm_test("max.nasm", ram, tst)
    assert bad_symbol() == 1

    ram = {0: 7, 1: 63}
    tst = {2: 63}
    assert nasm_test("max.nasm", ram, tst)
    assert bad_symbol() == 1
    
    
def test_abs():
    ram = {1: -1}
    tst = {0: 1}
    assert nasm_test("abs.nasm", ram, tst)
    assert bad_symbol() == 1

    ram = {1: 35}
    tst = {0: 35}
    assert nasm_test("abs.nasm", ram, tst)
    assert bad_symbol() == 1

    
def test_mult():
    ram = {0: 2, 1: 2}
    tst = {3: 4}
    assert nasm_test("mult.nasm", ram, tst)
    assert bad_symbol() == 1

    ram = {0: 32, 1: 16}
    tst = {3: 512}
    assert nasm_test("mult.nasm", ram, tst, 10000)
    assert bad_symbol() == 1
