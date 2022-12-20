from knightshock.kinetics import SimulationPool
import numpy as np
from time import time

T = np.linspace(1000, 2000, 50)
P = np.array([1e6])
mixtures = {}
mixtures["mix A"] = "H2:0.07191781, NH3:0.07191781, O2:0.1797945, N2:0.6763699"
mechanisms = [r"../Mechanisms/Stagni.yaml", "../Mechanisms/Glarborg2022.yaml"]

t1 = time()
results = SimulationPool(mechanisms, mixtures, P, T).parallel()
t2 = time()
print("Parallel: {0:.3f} seconds".format(t2 - t1))
print()

t1 = time()
SimulationPool(mechanisms, mixtures, P, T).serial()
t2 = time()
print("Serial: {0:.3f} seconds".format(t2 - t1))

# for sim in results:
#     T, P, X = sim.TPX
#     mix = {i for i in mixtures if mixtures[i] == X}
#     print(f'{T=} K, {P=} Pa, {mix=}, {X=}, Mech = {sim.gas.source} IDT is {sim.ignition_delay_time("oh")} S')
