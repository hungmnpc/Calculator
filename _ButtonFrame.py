import tkinter as tk
import constBase



class ButtonFrame:

	def __init__(self, root):
		self.digits = constBase.DIGITS
		self.operation = constBase.OPERATION
		self.rootFrame = root
		self.buttonFrame = self.createMainFrame()
		self.pack()


	def createMainFrame(self):
		frame = tk.Frame(self.rootFrame, height=constBase.BUTTONS_FRAME_HEIGHT)
		return frame

	def getFrame(self):
		return self.buttonFrame

	def pack(self):
		self.buttonFrame.pack(expand=True, fill="both", side=tk.BOTTOM)
