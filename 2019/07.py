RAW_DATA = "3,8,1001,8,10,8,105,1,0,0,21,30,51,72,81,94,175,256,337,418,99999,3,9,101,5,9,9,4,9,99,3,9,1001,9,3,9,1002,9,2,9,1001,9,2,9,1002,9,5,9,4,9,99,3,9,1002,9,4,9,101,4,9,9,102,5,9,9,101,3,9,9,4,9,99,3,9,1002,9,4,9,4,9,99,3,9,102,3,9,9,1001,9,4,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,99"
DATA = [int(x) for x in RAW_DATA.split(",")]

import itertools


class Amp:

    params = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 99: 0}

    def __init__(self, phase):
        self.inputs = [phase]
        self.data = DATA.copy()
        self.pointer = 0
        self.done = False
        self._update_state()

    def _update_state(self):
        self.op = int(str(self.data[self.pointer])[-2:])
        param_modes = [int(x) for x in str(self.data[self.pointer])[:-2].zfill(Amp.params[self.op])][::-1]
        self.raw_params = self.data[self.pointer + 1 : self.pointer + 1 + len(param_modes)]
        params_tuples = [(x, y) for x, y in zip(param_modes, self.raw_params)]
        self.params = [
            int(param) if mode else int(self.data[param])
            for mode, param in params_tuples
        ]

    def run(self):
        while True:
            if self.op == 99:
                self.done = True
                return
            if self.op == 1:
                self.data[self.raw_params[2]] = self.params[0] + self.params[1]
            elif self.op == 2:
                self.data[self.raw_params[2]] = self.params[0] * self.params[1]
            elif self.op == 3:
                if self.inputs:
                    self.data[self.raw_params[0]] = self.inputs.pop(0)
                else:
                    return
            elif self.op == 4:
                self.output = self.params[0]
            elif self.op == 5 and self.params[0] != 0:
                self.pointer = self.params[1]
                self._update_state()
                continue
            elif self.op == 6 and self.params[0] == 0:
                self.pointer = self.params[1]
                self._update_state()
                continue
            elif self.op == 7:
                self.data[self.raw_params[2]] = (1 if self.params[0] < self.params[1] else 0)
            elif self.op == 8:
                self.data[self.raw_params[2]] = (1 if self.params[0] == self.params[1] else 0)

            self.pointer = self.pointer + Amp.params[self.op] + 1
            self._update_state()


def run_amps(phases):

    amps = [Amp(phases[i]) for i in range(5)]
    _input = 0

    while not all([amp.done for amp in amps]):
        for i in range(5):
            amps[i].inputs.append(_input)
            amps[i].run()
            _input = amps[i].output

    return amps[4].output


def find_max_thrust(phases):
    phases = itertools.permutations(phases)
    max_thrust = -1
    for phase in phases:
        if (current := run_amps(phase)) > max_thrust:
            max_thrust = current
    print(max_thrust, phase)


find_max_thrust([0, 1, 2, 3, 4])
find_max_thrust([5, 6, 7, 8, 9])
