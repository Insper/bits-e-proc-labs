#!/usr/bin/env python3

#!/usr/bin/env python3

from myhdl import bin
from bits import vm_test
import os.path

SP = 0
STACK = 256
TEMP = {0: 5, 1: 6, 2: 7, 3:8, 4:9, 5:10, 6:11, 7:12}

def init_ram():
    ram = {0: 256}
    return ram

def test_1a_add():
    ram = init_ram()
    tst = {256: 123+23}
    assert vm_test("1a-add.vm", ram, tst)

def test_1b_calc():
    ram = init_ram()
    tst = {256: (14+2)-(123-1)}
    assert vm_test("1b-calc.vm", ram, tst)

def test_1c_div_zero():
    ram = init_ram()
    a = 0; b =10
    ram[TEMP[0]] = a
    ram[TEMP[1]] = b
    tst = {SP: STACK, TEMP[3]: a/b}
    assert vm_test("1c-div.vm", ram, tst)

def test_1c_div_noRest():
    ram = init_ram()
    a = 15; b =5
    ram[TEMP[0]] = a
    ram[TEMP[1]] = b
    tst = {SP: STACK, TEMP[3]: a/b}
    assert vm_test("1c-div.vm", ram, tst)

def test_1c_div_rest():
    ram = init_ram()
    a = 15; b =7
    ram[TEMP[0]] = a
    ram[TEMP[1]] = b
    tst = {SP: STACK, TEMP[3]: a//b}
    assert vm_test("1c-div.vm", ram, tst)

def test_1c_loop():
    ram = init_ram()
    cnt = 0
    for i in range(55):
        cnt = cnt + 1

    tst = {SP: STACK, TEMP[3]: cnt}
    assert vm_test("1c-loop.vm", ram, tst)

def test_2a_calculadora():
    ram = init_ram()

    val = (14+2)*(8-1)
    tst = {SP: STACK, TEMP[1]: val}
    assert vm_test("2a-calculadora", ram, tst, 50000)

def test_2b_calculadora():
    ram = init_ram()

    val = 15//5
    tst = {SP: STACK, TEMP[1]: val}
    assert vm_test("2b-calculadora", ram, tst, 50000)
