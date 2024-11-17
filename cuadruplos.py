class Cuadruplo:
    def __init__(self, op, arg1, arg2, res):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2
        self.res = res

    def __str__(self):
        return f"\t{self.op}\t|\t{self.arg1}\t|\t{self.arg2}\t|\t{self.res}"

    def __strsf__(self):
        return f"{self.op},{self.arg1},{self.arg2},{self.res}"


class Cuadruplotabla:
    def __init__(self):
        self.Cuadruplo = []
        self.global_count = 0
        self.temp_count = 0
        self.label_count = 0
        self.operators_pile = []
        self.operatings_pile = []
        self.type_pile = []
        self.jump_pile = []

    def nuevo_temp(self):
        temp = f"t{self.temp_count}"
        self.temp_count += 1
        return temp

    def nuevo_label(self):
        label = f"L{self.label_count}"
        self.label_count += 1
        return label

    def add_Cuadruplo(self, op, arg1, arg2, res):
        cuadruplo = Cuadruplo(op, arg1, arg2, res)
        self.Cuadruplo.append(cuadruplo)
        self.global_count += 1

    def add_assign_Cuadruplo(self, op, arg1, res):
        cuadruplo = Cuadruplo(op, arg1, "", res)
        self.Cuadruplo.append(cuadruplo)
        self.global_count += 1
        
    def add_end_Cuadruplo(self):
        self.add_Cuadruplo(12,"","","")

    def push_operator(self, operator):
        self.operators_pile.append(operator)

    def pop_operator(self):
        return self.operators_pile.pop()

    def peek_operator(self):
        return self.operators_pile[-1] if self.operators_pile else None

    def push_operating(self, operating):
        self.operatings_pile.append(operating)

    def pop_operating(self):
        return self.operatings_pile.pop()

    def peek_operating(self):
        return self.operatings_pile[-1] if self.operatings_pile else None

    def push_type(self, type_):
        self.type_pile.append(type_)

    def pop_type(self):
        return self.type_pile.pop()

    def peek_type(self):
        return self.type_pile[-1] if self.type_pile else None

    # Optional methods
    def get_type_pile(self):
        return self.type_pile

    def get_current_count(self):
        return self.global_count

    def push_jump(self, jump):
        self.jump_pile.append(jump)

    def pop_jump(self):
        return self.jump_pile.pop()

    def peek_jump(self):
        return self.jump_pile[-1] if self.jump_pile else None

    def add_by_pass_jump(self, label):
        self.add_Cuadruplo(12, "", "", label)

    def add_conditional_jump(self, condition, label):
        self.add_Cuadruplo(10, condition, "", label)

    def add_cycle_jump(self, condition, label):
        self.add_Cuadruplo(11, condition, "", label)

    def add_print_Cuadruplo(self, arg):
        self.add_Cuadruplo(9, "", "", arg)

    def get_Cuadruplo_by_index(self, index):
        return self.Cuadruplo[index]

    def edit_Cuadruplo_by_label(self, label, nuevo_res):
        index = next((i for i, quad in enumerate(self.Cuadruplo) if quad.res == label), None)
        if index is not None:
            self.Cuadruplo[index].res = nuevo_res

    def print_Cuadruplo_tabla(self):
        print("Tabla de Cuádruplos:")
        print("\t---------------------------------------------------------------------------------")
        print("\t|\ti\t|\tOp\t|\tArg1\t|\tArg2\t|\tRes\t|")
        print("\t---------------------------------------------------------------------------------")
        for index, quad in enumerate(self.Cuadruplo):
            print(f"\t|\t{index}:\t|{quad}\t|")
            print("\t---------------------------------------------------------------------------------")
