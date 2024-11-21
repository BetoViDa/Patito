class Interpreter:
    def __init__(self, compiled_code):
        parts = compiled_code.split("\n&\n")
        quadruples = [line.strip() for line in parts[0].strip().split("\n") if line.strip()]
        constants_table = [line.strip() for line in parts[1].strip().split("\n") if line.strip()]
        
        self.quadruples = [line.split(",") for line in quadruples]
        self.constants_table = self.parse_constants(constants_table)
        self.memory = self.initialize_memory()

    def parse_constants(self, constants_table):
        constants = {}
        for line in constants_table:
            comma_index = line.index(",")
            address = line[:comma_index].strip()
            value = line[comma_index + 1:].strip()
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1].replace("\\n", "\n")
            else:
                value = float(value) 
            constants[int(address)] = value
        return constants

    def initialize_memory(self):
        return {
            "global": [None] * 4000,
            "temp": [None] * 5000,
            "local": [None] * 5000,
        }

    def get_memory_segment(self, address):
        if 1000 <= address <= 4999:
            return "global"
        elif 5000 <= address <= 9999:
            return "temp"
        elif 10000 <= address <= 14999:
            return "local"
        raise ValueError(f"Direccion invalida: {address}")

    def get_base_address(self, segment):
        if segment == "global":
            return 1000
        elif segment == "temp":
            return 5000
        elif segment == "local":
            return 10000
        raise ValueError(f"Segmento de memoria invalido: {segment}")

    def get_value(self, address):
        if address is None or address == "":
            return None
        address = int(address)
        if address >= 15000:
            return self.constants_table[address]
        segment = self.get_memory_segment(address)
        base_address = self.get_base_address(segment)
        value = self.memory[segment][address - base_address]
        if value is None:
            raise ValueError(f"Variable en direccion {address} no inicializada")
        return value

    def set_value(self, address, value):
        address = int(address)
        segment = self.get_memory_segment(address)
        base_address = self.get_base_address(segment)
        self.memory[segment][address - base_address] = value

    def execute(self):
        instruction_pointer = 0
        print_buffer = []
        
        while instruction_pointer < len(self.quadruples):
            op, arg1, arg2, result = self.quadruples[instruction_pointer]
            try:
                op = int(op)
                if op == 0:  # Add
                    self.set_value(result, self.get_value(arg1) + self.get_value(arg2))
                elif op == 1:  # Sub
                    self.set_value(result, self.get_value(arg1) - self.get_value(arg2))
                elif op == 2:  # Mul
                    self.set_value(result, self.get_value(arg1) * self.get_value(arg2))
                elif op == 3:  # Div
                    self.set_value(result, self.get_value(arg1) / self.get_value(arg2))
                elif op == 4:  # Greater than
                    self.set_value(result, self.get_value(arg1) > self.get_value(arg2))
                elif op == 5:  # Less than
                    self.set_value(result, self.get_value(arg1) < self.get_value(arg2))
                elif op == 6:  # Not equal
                    self.set_value(result, self.get_value(arg1) != self.get_value(arg2))
                elif op == 7:  # Equal
                    self.set_value(result, self.get_value(arg1) == self.get_value(arg2))
                elif op == 8:  # Assign
                    self.set_value(result, self.get_value(arg1))
                elif op == 9:  # Print
                    value_to_print = self.get_value(result)
                    print_buffer.append(str(value_to_print))
                elif op == 10:  # GOTOF
                    if not self.get_value(arg1):
                        instruction_pointer = int(result) - 1
                elif op == 11:  # GOTOT
                    if self.get_value(arg1):
                        instruction_pointer = int(result) - 1
                elif op == 12:  # GOTO
                    instruction_pointer = int(result) - 1
                elif op == 13:  # END
                    return
                else:
                    raise ValueError(f"Operacion desconocida: {op}")
            except Exception as error:
                print(f"Error en instruccion {instruction_pointer}: {error}")
                return

            if (
                instruction_pointer < len(self.quadruples)  and
                int(self.quadruples[instruction_pointer + 1][0]) != 8
            ) or instruction_pointer == len(self.quadruples) :
                if print_buffer:
                    print("".join(print_buffer))
                    print_buffer = []

            instruction_pointer += 1
        
        if print_buffer:
            print("".join(print_buffer))
