import asyncio
from copy import copy
import random


async def merge(A1, A2, start, middle, finish, event_in1, event_in2, event_out):
    A1, left, right = copy(A1), start, middle
    await event_in1.wait()
    await event_in2.wait()
    for i in range(start, finish):
        if right >= finish or left < middle and A1[left] < A1[right]:
            A2[i] = A1[left]
            left += 1
        else:
            A2[i] = A1[right]
            right += 1
    event_out.set()


async def mtasks(A):
    A, lenA = copy(A), len(A)
    tasks, evs = [], [asyncio.Event() for _ in range(lenA + 1)]
    for ev in evs:
        ev.set()
    step = 1
    while step < lenA:
        cur_ev, upd = 0, []
        for i in range(0, lenA, 2 * step):
            upd.append(asyncio.Event())
            tasks.append(asyncio.create_task(merge(
                A, A, i, min(i + step, lenA), min(i + 2 * step, lenA),
                evs[cur_ev], evs[cur_ev + 1], upd[-1]
            )))
            cur_ev += 2
        upd.append(upd[-1])
        evs = upd
        step *= 2
    return tasks, A


import sys
exec(sys.stdin.read())