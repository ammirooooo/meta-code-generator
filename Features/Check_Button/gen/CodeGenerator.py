import os
from gen.configuration import METHOD_LIB


class CodeGenerator:
    def __init__(self, output_address, asts_list):
        self.asts_list = asts_list
        if os.path.exists(output_address):
            os.remove(output_address)
        output = open(r"" + output_address, "a")
        self.output = output

    def print_file(self, address):
        with open(address) as fh:
            layout_lines = fh.readlines()
        for line in layout_lines:
            self.output.write(line)

    def generate_code(self):
        self.print_file('layout.txt')

        counter = 1
        for i in self.asts_list:
            inputAttributes = i

            attributes = {
                "text": "'check'",
                "variable": "checkButton" + str(counter),
                "onvalue": "1",
                "offvalue": "0",
                "height": "2",
                "width": "10",
            }

            for j in inputAttributes:
                if j[0] == "variable" or j[0] == "value" or j[0] == "gridy":
                    continue

                if j[0] == 'checked':
                    if j[1] == '"true"':
                        self.output.write("checkButton" + str(counter) + " = IntVar(value=1)\n")
                    else:
                        self.output.write("checkButton" + str(counter) + " = IntVar(value=0)\n")
                    attributes[j[0]] = j[1]
                elif j[0] == 'text':
                    attributes[j[0]] = "'" + j[1] + "'"
                else:
                    attributes[j[0]] = j[1]

            values = 'root'

            if 'checked' not in attributes.keys():
                self.output.write("checkButton" + str(counter) + " = IntVar(value=0)\n")
            else:
                del attributes['checked']

            for j in attributes:
                attribute = ", " + j + " = " + attributes[j]
                values += attribute

            self.output.write("Button" + str(counter) + " = Checkbutton" + "(" + values + ")" + "\n")

            self.output.write("Button" + str(counter) + ".pack()\n\n")

            counter += 1

        self.print_file('footer.txt')
