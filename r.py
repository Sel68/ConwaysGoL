import cellpylib as cpl
import numpy as np


cell_automaton = np.random.choice([0,1], size=200)
cell_automaton = cell_automaton.reshape((1, 200))
cpl.plot(cell_automaton)

cell_automaton = cpl.evolve(cell_automaton, timesteps=100, apply_rule=lambda n, c, t: cpl.nks_rule(n,90))

cpl.plot(cell_automaton)
