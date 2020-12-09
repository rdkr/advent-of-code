class Machine:
    def __init__(self, ops, args):
        self.ops = ops
        self.args = args

        self.visited = [False] * len(self.ops)
        self.acca = 0
        self.pos = 0

    def run(self):
        try:
            self.runner()
        except RuntimeError:
            print(self.acca)

    def runner(self):
        while True:
            if self.visited[self.pos]:
                raise RuntimeError
            self.visited[self.pos] = True
            getattr(self, self.ops[self.pos])(self.args[self.pos])

    def acc(self, arg):
        self.acca = self.acca + arg
        self.pos = self.pos + 1

    def jmp(self, arg):
        self.pos = self.pos + arg

    def nop(self, arg):
        self.pos = self.pos + 1


class RewindMachine(Machine):
    def run(self):
        original_ops = self.ops.copy()
        last_changed = len(original_ops)

        while True:

            try:
                self.runner()
            except RuntimeError:
                last_changed = last_changed - 1

                new_ops = original_ops.copy()
                for i in range(last_changed, 0, -1):
                    if self.ops[i] == "jmp":
                        new_ops[i] = "nop"
                        break
                    elif self.ops[i] == "nop":
                        new_ops[i] = "jmp"
                        break
                    else:
                        last_changed = last_changed - 1

                self.ops = new_ops
                self.visited = [False] * len(self.ops)
                self.acca = 0
                self.pos = 0

            except IndexError:
                return print(self.acca)


def get_input(ops=[], args=[]):
    if not ops and not args:
        with open("08.txt") as _input:
            for instruction in _input:
                op, arg = instruction.rstrip().split(" ")
                ops.append(op)
                args.append(int(arg))
    return ops, args


machine = Machine(*get_input())
machine.run()

machine = RewindMachine(*get_input())
machine.run()
