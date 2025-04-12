import matplotlib.pyplot as plt
import numpy as np
from math import exp
import pandas as pd
import time
import seaborn as sb
import multiprocessing as mp


def f(v, s, a, rho, xy):
    return [a * xy[1], (s * xy[0] + v * xy[1]) * exp(-xy[0] - rho * xy[1])]
    #return [a * xy[1], exp(-xy[0] - rho * xy[1]) * xy[0] + v * xy[1]]


def calculate_frame(I, k, h, space_a, space_rho, xy0, v, s):
    la = len(space_a)
    lr = len(space_rho)
    local_df = np.zeros((la, lr))  # локальный двумерный массив для каждого процесса

    for i in range(I * k, (I + 1) * k):
        for j in range(lr):
            a = space_a[i]
            rho = space_rho[j]
            values = []
            p = xy0

            for _ in range(1000):
                values.append((round(p[0], 3), round(p[1], 3)))
                p = f(v, s, a, rho, p)

            values = values[800:]  # оставляем последние 200 значений
            uniq = len(set(values))
            # ограничиваем уникальные значения
            local_df[lr - 1 - j, i] = 20 if uniq > 20 else uniq

    print(f"Frame {I} finished")
    return local_df  # возвращаем локальный массив


def convert_parallel(start_frame, finish_frame, k, h, space_a, space_rho, xy0, v, s):
    num_processes = mp.cpu_count()
    pool = mp.Pool(processes=num_processes)
    results = pool.starmap(calculate_frame,
                           [(i, k, h, space_a, space_rho, xy0, v, s) for i in range(start_frame, finish_frame + 1)])
    pool.close()
    pool.join()

    # Объединяем результаты из всех процессов
    df = np.sum(results, axis=0)
    return df


if __name__ == '__main__':
    v = 0.5
    s = 0.5
    maxa = 120
    maxr = 120
    k = 10
    h = 200  # должно быть кратно k
    xy0 = (3, 3)

    space_a = np.linspace(1, maxa, h)
    space_rho = np.linspace(1, maxr, h)
    la = len(space_a)
    lr = len(space_rho)

    start_time = time.time()
    mp.freeze_support()

    # Изменяем количество кадров в зависимости от k
    df = convert_parallel(0, h // k - 1, k, h, space_a, space_rho, xy0, v, s)

    print("Time taken:", time.time() - start_time)

    h_ = int(h / 10)

    df = pd.DataFrame(df)
    df.to_csv("dmm7.csv", index=None)

