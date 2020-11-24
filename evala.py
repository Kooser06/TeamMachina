#!/usr/bin/env pypy
# -*- coding: utf-8 -*-

pvs = (100, 100, 100, 100, 325, 425, 500, 100000)
ost = [
    (0, 0,   0,   0,   0,   0,   0,  0,  0, 0,
     0, 0,   0,   0,   0,   0,   0,  0,  0, 0,
     0, 0,   0,   0,   0,   0,   0,  0,  0, 0,
     0, 5,   15,  20,  5,   20,  5,  10, 5, 0,
     0, 5,   20,  10, -10,  10,  5, -5,  0, 0,
     0, 10,  25,  5,   10,  0,  -5,  0,  0, 0,
     0, 10, -5,   10,  5,  -5,   0,  0,  0, 0,
     0, 5,   20, -15,  20,  0,   0,  0,  0, 0,
     0, 0,   0,   0,   0,   0,   0,  0,  0, 0,
     0, 0,   0,   0,   0,   0,   0,  0,  0, 0,
     0, 0,   0,   0,   0,   0,   0,  0,  0, 0,
     0, 0,   0,   0,   0,   0,   0,  0,  0, 0),
    (0,  0,   0,   0,   0,   0,   0,   0,   0,  0,
     0,  0,   0,   0,   0,   0,   0,   0,   0,  0,
     0, -10, -5,   5,  -5,   10,  15,  10, -5,  0,
     0, -10, -5,   5,   10,  10,  10,  5,  -10, 0,
     0,  5,   10,  15,  15,  5,   15, -5,  -5,  0,
     0,  10, -5,  -5,   35,  40, -5,   20,  5,  0,
     0,  15,  10,  10,  40,  35,  15, -5,  -5,  0,
     0,  25, -5,   25,  10,  10,  25, -10, -5,  0,
     0, -10, -5,  -10, -15, -5,  -5,  -5,   0,  0,
     0, -25,  0,  -15, -20,  5,   5,  -10, -25, 0,
     0,  0,   0,   0,   0,   0,   0,   0,   0,  0,
     0,  0,   0,   0,   0,   0,   0,   0,   0,  0),
    (0,  0,   0,   0,   0,  0,   0,   0,   0,  0,
     0,  0,   0,   0,   0,  0,   0,   0,   0,  0,
     0,  0,  -15,  0,  -20, 0,  -10,  0,  -30, 0,
     0, -20,  0,  -15,  0,  5,   0,  -15,  0,  0,
     0,  0,  -10,  0,   25, 0,   15,  0,  -10, 0,
     0,  10,  0,   10,  0,  40,  0,  -10,  0,  0,
     0,  0,   5,   0,   40, 0,   10,  0,   5,  0,
     0,  10,  0,   15,  0,  20,  0,  -5,   0,  0,
     0,  0,   20,  0,   15, 0,  -5,   0,  -15, 0,
     0, -20,  0,   0,   0,  5,   0,  -10,  0,  0,
     0,  0,   0,   0,   0,  0,   0,   0,   0,  0,
     0,  0,   0,   0,   0,  0,   0,   0,   0,  0),
    (0,  0,   0,   0,   0,   0,   0,   0,   0,  0,
     0,  0,   0,   0,   0,   0,   0,   0,   0,  0,
     0,  20,  0,  -5,  -5,   5,  -10,  0,   20, 0,
     0,  5,  -15,  5,   10,  10, -5,  -10,  10, 0,
     0,  15, -5,   10,  15,  15,  5,   10,  5,  0,
     0,  5,   10,  15,  25,  25,  15, -10, -10, 0,
     0,  10, -5,   15,  35,  35,  15, -5,   5,  0,
     0,  10, -5,  -5,   20, -5,  -10, -10, -5,  0,
     0, -30, -25, -10, -10, -5,  -5,  -20, -30, 0,
     0,  0,  -25, -20,  20, -5,  -15, -25,  0,  0,
     0,  0,   0,   0,   0,   0,   0,   0,   0,  0,
     0,  0,   0,   0,   0,   0,   0,   0,   0,  0)
], [
    (0, 0, 0,  0,   0,  0,   0,   0,  0, 0,
     0, 0, 0,  0,   0,  0,   0,   0,  0, 0,
     0, 0, 0, -5,   0,  0,   0,   0,  0, 0,
     0, 0, 0,  20, -5,  0,   0,   0,  0, 0,
     0, 0, 0,  25, -5, -5,   0,   0,  0, 0,
     0, 0, 0,  25,  5, -10, -5,   0,  0, 0,
     0, 0, 0,  30, -5,  20,  15,  15, 0, 0,
     0, 0, 0,  35, -5,  30,  10,  25, 0, 0,
     0, 0, 0,  40, -5,  15, -5,   10, 0, 0,
     0, 0, 0,  40, -5,  15, -5,  -10, 0, 0,
     0, 0, 0,  0,   0,  0,   0,   0,  0, 0,
     0, 0, 0,  0,   0,  0,   0,   0,  0, 0),
    (0,  0,   0,   0,   0,   0,   0,   0,   0,  0,
     0,  0,   0,   0,   0,   0,   0,   0,   0,  0,
     0, -25, -10,  5,   5,  -20, -15,  0,  -25, 0,
     0,  0,  -5,  -5,  -5,  -15, -10, -5,  -10, 0,
     0, -5,  -10,  25,  10,  10,  25, -5,   25, 0,
     0, -5,  -5,   15,  35,  40,  10,  10,  15, 0,
     0,  5,   20, -5,   40,  35, -5,  -5,   10, 0,
     0, -5,  -5,   15,  5,   15,  15,  10,  5,  0,
     0, -10,  5,   10,  10,  10,  5,  -5,  -10, 0,
     0, -5,   10,  15,  10, -5,   5,  -5,  -10, 0,
     0,  0,   0,   0,   0,   0,   0,   0,   0,  0,
     0,  0,   0,   0,   0,   0,   0,   0,   0,  0),
    (0,  0,   0,   0,   0,   0,   0,   0,   0,  0,
     0,  0,   0,   0,   0,   0,   0,   0,   0,  0,
     0, -10,  0,   10,  0,   5,   0,  -10,  0,  0,
     0,  0,   10,  0,  -5,   0,   10,  0,  -15, 0,
     0,  0,   0,   15,  0,  -5,   0,  -5,   0,  0,
     0,  0,   20,  0,   40,  0,  -10,  0,  -10, 0,
     0, -10,  0,  -10,  0,   40,  0,  -5,   0,  0,
     0,  0,  -5,   0,  -15,  0,  -5,   0,  -5,  0,
     0, -20,  0,  -10,  0,  -10,  0,  -15,  0,  0,
     0,  0,  -30,  0,  -15,  0,  -20,  0,  -25, 0,
     0,  0,   0,   0,   0,   0,   0,   0,   0,  0,
     0,  0,   0,   0,   0,   0,   0,   0,   0,  0),
], [
    (0, 0,  0,   0,  0,   0,   0,   0,  0,  0,
     0, 0,  0,   0,  0,   0,   0,   0,  0,  0,
     0, 0,  0,   0,  0,   0,   0,   0,  0,  0,
     0, 0,  0,   0,  0,   0,   0,   0,  0,  0,
     0, 0,  0,   0,  0,   20, -15,  20, 5,  0,
     0, 0,  0,   0, -5,   5,   10, -5,  10, 0,
     0, 0,  0,  -5,  0,   10,  5,   25, 10, 0,
     0, 0, -5,   5,  10, -10,  10,  20, 5,  0,
     0, 5,  10,  5,  20,  5,   20,  15, 5,  0,
     0, 0,  0,   0,  0,   0,   0,   0,  0,  0,
     0, 0,  0,   0,  0,   0,   0,   0,  0,  0,
     0, 0,  0,   0,  0,   0,   0,   0,  0,  0),
    (0,  0,   0,   0,   0,   0,   0,   0,   0,  0,
     0,  0,   0,   0,   0,   0,   0,   0,   0,  0,
     0, -25, -10,  5,   5,  -20, -15,  0,  -25, 0,
     0,  0,  -5,  -5,  -5,  -15, -10, -5,  -10, 0,
     0, -5,  -10,  25,  10,  10,  25, -5,   25, 0,
     0, -5,  -5,   15,  35,  40,  10,  10,  15, 0,
     0,  5,   20, -5,   40,  35, -5,  -5,   10, 0,
     0, -5,  -5,   15,  5,   15,  15,  10,  5,  0,
     0, -10,  5,   10,  10,  10,  5,  -5,  -10, 0,
     0, -5,   10,  15,  10, -5,   5,  -5,  -10, 0,
     0,  0,   0,   0,   0,   0,   0,   0,   0,  0,
     0,  0,   0,   0,   0,   0,   0,   0,   0,  0),
    (0,  0,   0,   0,  0,   0,   0,   0,   0,  0,
     0,  0,   0,   0,  0,   0,   0,   0,   0,  0,
     0,  0,  -10,  0,  5,   0,   0,   0,  -20, 0,
     0, -15,  0,  -5,  0,   15,  0,   20,  0,  0,
     0,  0,  -5,   0,  20,  0,   15,  0,   10, 0,
     0,  5,   0,   10, 0,   40,  0,   5,   0,  0,
     0,  0,  -10,  0,  40,  0,   10,  0,   10, 0,
     0, -10,  0,   15, 0,   25,  0,  -10,  0,  0,
     0,  0,  -15,  0,  5,   0,  -15,  0,  -20, 0,
     0, -30,  0,  -10, 0,  -20,  0,  -15,  0,  0,
     0,  0,   0,   0,  0,   0,   0,   0,   0,  0,
     0,  0,   0,   0,  0,   0,   0,   0,   0,  0),
], [
    (0, 0,  0,   0,   0,   0,  0,  0, 0, 0,
     0, 0,  0,   0,   0,   0,  0,  0, 0, 0,
     0, 0, -10, -5,   15, -5,  40, 0, 0, 0,
     0, 0,  10, -5,   15, -5,  40, 0, 0, 0,
     0, 0,  25,  10,  30, -5,  35, 0, 0, 0,
     0, 0,  15,  15,  20, -5,  30, 0, 0, 0,
     0, 0,  0,  -5,  -10   5,  25, 0, 0, 0,
     0, 0,  0,   0,  -5,  -5,  25, 0, 0, 0,
     0, 0,  0,   0,   0,  -5,  20, 0, 0, 0,
     0, 0,  0,   0,   0,   0, -5,  0, 0, 0,
     0, 0,  0,   0,   0,   0,  0,  0, 0, 0,
     0, 0,  0,   0,   0,   0,  0,  0, 0, 0),
    (0,  0,   0,   0,   0,   0,   0,   0,   0,  0,
     0,  0,   0,   0,   0,   0,   0,   0,   0,  0,
     0, -10, -5,   5,  -5,   10,  15,  10, -5,  0,
     0, -10, -5,   5,   10,  10,  10,  5,  -10, 0,
     0,  5,   10,  15,  15,  5,   15, -5,  -5,  0,
     0,  10, -5,  -5,   35,  40, -5,   20,  5,  0,
     0,  15,  10,  10,  40,  35,  15, -5,  -5,  0,
     0,  25, -5,   25,  10,  10,  25, -10, -5,  0,
     0, -10, -5,  -10, -15, -5,  -5,  -5,   0,  0,
     0, -25,  0,  -15, -20,  5,   5,  -10, -25, 0,
     0,  0,   0,   0,   0,   0,   0,   0,   0,  0,
     0,  0,   0,   0,   0,   0,   0,   0,   0,  0),
]
