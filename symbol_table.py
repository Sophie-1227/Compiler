class Variable:
    def __init__(self, memory_offset):
        self.memory_offset = memory_offset
        self.initialized = False

    def __repr__(self):
        return f"{'Uni' if not self.initialized else 'I'}nitialized variable at {self.memory_offset}"

class Iterator:
    def __init__(self, memory_offset, limit_address):
        self.memory_offset = memory_offset
        self.limit_address = limit_address

    def __repr__(self):
        return f"iterator at {self.memory_offset}"

class SymbolTable(dict):
    def __init__(self):
        self.table = {}

    def put(self, name, value):
        self.table[name] = value

    def get(self, name):
        if name in self.table:
            return self.table[name]
        else:
            return None