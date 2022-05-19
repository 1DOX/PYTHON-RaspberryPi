import sys
from PySide2 import QtCore, QtWidgets, QtGui, QtXml, QtUiTools

class MainWindow(QtWidgets.QDialog):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Calculator")
		self.setup_ui()
		
	def setup_ui(self):
		main_layout = QtWidgets.QVBoxLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
		layout_clear_equal = QtWidgets.QHBoxLayout()
		layout_operation = QtWidgets.QHBoxLayout()
		layout_number = QtWidgets.QGridLayout()
		layout_equation_solution = QtWidgets.QFormLayout()
		
		### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
		label_equation = QtWidgets.QLabel("Input: ")
		label_solution = QtWidgets.QLabel("Result: ")
		self.equation = QtWidgets.QLineEdit("")
		self.solution = QtWidgets.QLineEdit("")
		
		### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
		layout_equation_solution.addRow(label_equation, self.equation)
		layout_equation_solution.addRow(label_solution, self.solution)
		
		### =, clear, backspace 버튼 생성
		button_equal = QtWidgets.QPushButton("=")
		button_clear = QtWidgets.QPushButton("C")
		button_backspace = QtWidgets.QPushButton("←")

        ### =, clear, backspace 버튼 클릭 시 시그널 설정
		button_equal.clicked.connect(self.button_equal_clicked)
		button_clear.clicked.connect(self.button_clear_clicked)
		button_backspace.clicked.connect(self.button_backspace_clicked)

        ### =, clear, backspace 버튼을 layout_clear_equal 레이아웃에 추가
		layout_clear_equal.addWidget(button_clear)
		layout_clear_equal.addWidget(button_backspace)
		layout_clear_equal.addWidget(button_equal)

        ### 사칙연상 버튼 생성
		button_plus = QtWidgets.QPushButton("+")
		button_minus = QtWidgets.QPushButton("-")
		button_product = QtWidgets.QPushButton("x")
		button_division = QtWidgets.QPushButton("/")
        
        ### 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
		button_plus.clicked.connect(lambda : self.button_operation_clicked('+'))
		button_minus.clicked.connect(lambda : self.button_operation_clicked('-'))
		button_product.clicked.connect(lambda : self.button_operation_clicked('*'))
		button_division.clicked.connect(lambda : self.button_operation_clicked('/'))

        ### 사칙연산 버튼을 layout_operation 레이아웃에 추가
		layout_operation.addWidget(button_plus)
		layout_operation.addWidget(button_minus)
		layout_operation.addWidget(button_product)
		layout_operation.addWidget(button_division)

        ### 숫자 버튼 생성하고, layout_number 레이아웃에 추가
        ### 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
		number_button_dict = {}
		for number in range(10):
			number_button_dict[number] = QtWidgets.QPushButton(str(number))
			#number_button_dict[number].clicked.connect(lambda : self.number_button_clicked(number))
			if number > 0:
				x, y = divmod(number-1, 3)
				layout_number.addWidget(number_button_dict[number], x, y)
			elif number == 0:
				layout_number.addWidget(number_button_dict[number], 3, 1)
		
		number_button_dict[0].clicked.connect(lambda : self.number_button_clicked(0))
		number_button_dict[1].clicked.connect(lambda : self.number_button_clicked(1))
		number_button_dict[2].clicked.connect(lambda : self.number_button_clicked(2))
		number_button_dict[3].clicked.connect(lambda : self.number_button_clicked(3))
		number_button_dict[4].clicked.connect(lambda : self.number_button_clicked(4))
		number_button_dict[5].clicked.connect(lambda : self.number_button_clicked(5))
		number_button_dict[6].clicked.connect(lambda : self.number_button_clicked(6))
		number_button_dict[7].clicked.connect(lambda : self.number_button_clicked(7))
		number_button_dict[8].clicked.connect(lambda : self.number_button_clicked(8))
		number_button_dict[9].clicked.connect(lambda : self.number_button_clicked(9))
			
        ### 소숫점 버튼과 00 버튼을 입력하고 시그널 설정
		button_dot = QtWidgets.QPushButton(".")
		button_dot.clicked.connect(lambda : self.number_button_clicked('.'))
		layout_number.addWidget(button_dot, 3, 2)

		button_double_zero = QtWidgets.QPushButton("00")
		button_double_zero.clicked.connect(lambda : self.number_button_clicked('00'))
		layout_number.addWidget(button_double_zero, 3, 0)

        ### 각 레이아웃을 main_layout 레이아웃에 추가
		main_layout.addLayout(layout_equation_solution)
		main_layout.addLayout(layout_clear_equal)
		main_layout.addLayout(layout_operation)
		main_layout.addLayout(layout_number)

		self.setLayout(main_layout)
		self.show()
		
		
	#################
    ### functions ###
    #################
	def number_button_clicked(self, num):
		equation = self.equation.text()
		equation += str(num)
		self.equation.setText(equation)

	def button_operation_clicked(self, operation):
		equation = self.equation.text()
		equation += operation
		self.equation.setText(equation)

	def button_equal_clicked(self):
		equation = self.equation.text()
		solution = eval(equation)
		self.solution.setText(str(solution))

	def button_clear_clicked(self):
		self.equation.setText("")
		self.solution.setText("")

	def button_backspace_clicked(self):
		equation = self.equation.text()
		equation = equation[:-1]
		self.equation.setText(equation)
        
if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	main = MainWindow()
	sys.exit(app.exec_())
