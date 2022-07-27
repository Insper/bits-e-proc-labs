#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

import math
from myhdl import *

# from ula.ula_modules import adder


@block
def dff(q, d, clk, rst):
    @always_seq(clk.posedge, reset=rst)
    def seq():
        q.next = d

    return instances()


@block
def blinkLed(led, time_ms, clk, rst):
    ms = 50000
    cnt = Signal(intbv(0)[32:])
    l = Signal(bool(0))

    @always_seq(clk.posedge, reset=rst)
    def seq():
        if cnt < 25000000:
            cnt.next = cnt + 1
        else:
            cnt.next = 0
            l.next = not l

    @always_comb
    def comb():
        led.next = l

    return instances()


@block
def barLed(leds, time_ms, dir, vel, clk, rst):
    ms = 50000
    cnt = Signal(intbv(0)[32:])
    cntLed = Signal(intbv(0)[4:])
    led = Signal(intbv(0)[10:])
    delay = Signal(intbv(0)[32:])

    @always_seq(clk.posedge, reset=rst)
    def seq():
        if cnt < delay:
            # if cnt < time_ms * ms:
            cnt.next = cnt + 1
        else:
            cnt.next = 0
            if cntLed < 10:
                if dir:
                    cntLed.next = cntLed + 1
                else:
                    cntLed.next = cntLed - 1
                led[cntLed].next = 1
            else:
                led.next = 0
                if dir:
                    cntLed.next = 0
                else:
                    cntLed.next = 2**10 - 1

    @always_comb
    def comb():
        leds.next = led

        if vel:
            delay.next = 10000000
        else:
            delay.next = 5000000

    return instances()


@block
def barLed2(leds, time_ms, clk, rst):
    ms = 50000
    cnt = Signal(intbv(0)[32:])
    cntLed = Signal(intbv(0)[4:])
    led = Signal(intbv(0)[10:])

    @always_seq(clk.posedge, reset=rst)
    def seq():
        if cnt < time_ms * ms:
            cnt.next = cnt + 1
        else:
            cnt.next = 0
            if cntLed < 10:
                cntLed.next = cntLed + 1
            else:
                cntLed.next = 0

    @always_comb
    def comb():
        leds.next = intbv(1)[10:] << cntLed

    return instances()


@block
def doubleDabble(din, clk, rst):

    bcd = Signal(modbv(0)[12:])
    cnt = Signal(intbv(0)[8:])
    b = Signal(0)[12:0]

    @always(clk.posedge)
    def seq():
        print(bin(bcd[4:0], 4))
        print("%s" % bin(bcd[8:4], 4))
        print("%s" % (bin(bcd[12:8], 4)))
        print(cnt)
        print("-----")
        if cnt < 8:
            bcd.next = bcd << 1
            if bcd[8:4] < 5 and bcd[12:8] < 5:
                cnt.next = cnt + 1

            if bcd[8:4] >= 5:
                print("add L")
                bcd[8:4].next = bcd[8:4] + 3

            if bcd[12:8] >= 5:
                print("add H")
                bcd[12:8].next = bcd[12:8] + 3

        else:
            print("----------------------")
            print("%s %s" % (bin(bcd[12:8], 4), bin(bcd[8:4], 4)))
            bcd.next = din
            cnt.next = 0

    return instances()
