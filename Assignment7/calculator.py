import pygtk
pygtk.require('2.0')
import gtk

class Calculator:
	#A call back function to insert the button text,invoked when operands are pressed.
	#this function inserts the button text into textbox entry.		
	def print_buttonText(self,widget,operand):
		self.entry.insert_text(operand,position = 20)

	#A call back function called when operators are pressed.
	def calculate(self,widget,operator):
		if operator == 'Clr':
			self.entry.set_text("")
		elif operator == 'CE':
			self.entry.set_text("0")		
		elif operator == '+':
			self.flag = 1
			self.firstOperand = self.entry.get_text()
			self.entry.set_text("")
		elif operator == '-':
			self.flag = 2
			self.firstOperand = self.entry.get_text()
			self.entry.set_text("")
		elif operator == '*':
			self.flag = 3
			self.firstOperand = self.entry.get_text()
			self.entry.set_text("")
		elif operator == '/':
			self.flag = 4
			self.firstOperand = self.entry.get_text()
			self.entry.set_text("")
		elif operator == '%':
			self.flag = 5
			self.firstOperand = self.entry.get_text()
			self.entry.set_text("")
		elif operator == '=':
			self.secondOperand = self.entry.get_text()
			sum1 = float(self.firstOperand)
			sum2 = float(self.secondOperand)
			if self.flag == 1:
				result = sum1 + sum2
			elif self.flag == 2:
				result = sum1 - sum2
			elif self.flag == 3:
				result = sum1 * sum2
			elif self.flag == 4:
				result = sum1 / sum2
			elif self.flag == 5:
				sum1 = int(sum1)
				sum2 = int(sum2)	
				result = sum1 % sum2
			self.entry.set_text(str(result))		
				
	#This function is used to design the gui of calcualtor
	def __init__(self):
		self.window = gtk.Window()		#a window is created
		self.window.set_title("Calculator")
		self.window.set_size_request(500,500)
		self.window.connect("destroy",gtk.main_quit) #window is connected with 'destroy' signal,
							     #window is closed when we press 'close x' at top right corner
														

		self.table = gtk.Table(6,4,False) # a table is created with 6 rows and 4 columns
		self.window.add(self.table)	  # a table is added to the window 	

		self.entry = gtk.Entry()	  # text entry is created
		self.table.attach(self.entry,0,4,0,1)  #attached to the table

		self.button = gtk.Button("Close")      #buttons are created
		self.table.attach(self.button,0,1,1,2)  #attached to the table 
		self.button.connect("clicked",gtk.main_quit)#the application gets terminated when we click on the close button

		self.button = gtk.Button("CE")
		self.table.attach(self.button,1,2,1,2)
		self.button.connect("clicked",self.calculate,"CE") #calculate function is invoked, when the corresponding button receives 'clicked' signal

		self.button = gtk.Button("Clr")
		self.table.attach(self.button,2,3,1,2)
		self.button.connect("clicked",self.calculate,"Clr")

		self.button = gtk.Button("%")
		self.table.attach(self.button,3,4,1,2)
		self.button.connect("clicked",self.calculate,'%')

		
		self.button = gtk.Button("7")
		self.table.attach(self.button,0,1,2,3)
		self.button.connect("clicked",self.print_buttonText,"7")

		self.button = gtk.Button("8")
		self.table.attach(self.button,1,2,2,3)
		self.button.connect("clicked",self.print_buttonText,"8")

		self.button = gtk.Button("9")
		self.table.attach(self.button,2,3,2,3)
		self.button.connect("clicked",self.print_buttonText,"9")

		self.button = gtk.Button("/")
		self.table.attach(self.button,3,4,2,3)
		self.button.connect("clicked",self.calculate,"/")

		
		
		self.button = gtk.Button("4")
		self.table.attach(self.button,0,1,3,4)
		self.button.connect("clicked",self.print_buttonText,"4")

		self.button = gtk.Button("5")
		self.table.attach(self.button,1,2,3,4)
		self.button.connect("clicked",self.print_buttonText,"5")

		self.button = gtk.Button("6")
		self.table.attach(self.button,2,3,3,4)
                self.button.connect("clicked",self.print_buttonText, "6")

		self.button = gtk.Button("*")
		self.table.attach(self.button,3,4,3,4)
		self.button.connect("clicked",self.calculate,"*")
		
		self.button = gtk.Button("1")
		self.table.attach(self.button,0,1,4,5)
		self.button.connect("clicked",self.print_buttonText,"1")
		
		
		self.button = gtk.Button("2")
		self.table.attach(self.button,1,2,4,5)
		self.button.connect("clicked",self.print_buttonText,"2")

		self.button = gtk.Button("3")
		self.table.attach(self.button,2,3,4,5)
		self.button.connect("clicked",self.print_buttonText,"3")

		self.button = gtk.Button("-")
		self.table.attach(self.button,3,4,4,5)
		self.button.connect("clicked",self.calculate,"-")

		self.button = gtk.Button("0")
		self.table.attach(self.button,0,1,5,6)
		self.button.connect("clicked",self.print_buttonText,"0")

		self.button = gtk.Button(".")
		self.table.attach(self.button,1,2,5,6)
		self.button.connect("clicked",self.print_buttonText,".")

		self.button = gtk.Button("=")
		self.table.attach(self.button,2,3,5,6)
		self.button.connect("clicked",self.calculate,'=')

		self.button = gtk.Button("+")
		self.table.attach(self.button,3,4,5,6)
		self.button.connect("clicked",self.calculate,"+")

		self.window.show_all()

	#this function invokes main
	def main(self):
		gtk.main()

if __name__ == "__main__":
	c = Calculator() #instance of calculator is created
	c.main()	#main function is invoked

