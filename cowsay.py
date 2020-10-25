from typing import AnyStr, Iterable, Tuple

class Character:
	"""
	Defines parameters to compose a cowsay character.

	Replicates the original cowsay program by default.
	"""

	def __init__(self):
		self.horizontal_border = "-"

		self.left_single_border = "<"
		self.right_single_border = ">"

		self.top_left_border = "/"
		self.left_border = "|"
		self.bottom_left_border = "\\"

		self.top_right_border = "\\"
		self.right_border = "|"
		self.bottom_right_border = "/"

		self.speech_bubble_line = "\\"
		self.speech_bubble_line_left_padding = 8
		self.speech_bubble_line_right_padding = 2

		self.character = R"""
^__^
(oo)\_______
(__)\       )\/\
	||----w |
	||     ||"""[1:]

		self.tab_size = 4

	def say(self, message: AnyStr) -> None:
		"""
		Print a message using the character.
		"""

		message = message.replace("\t", " " * self.tab_size).strip()
		lines = message.split("\n")
		count = len(lines)

		if count == 1:
			self._say_singleline(message)
		elif count == 2:
			self._say_two_lines(lines[0], lines[1])
		else:
			self._say_lines(lines)

		self._print_character()

	def _padding(self, line_count: int) -> Tuple[int, int]:
		if line_count == 1:
			return (len(self.left_single_border), len(self.right_single_border))

		if line_count == 2:
			return (
				len(max(self.top_left_border, self.bottom_left_border)),
				len(max(self.top_right_border, self.bottom_right_border)))

		return (
			len(max(
				(self.left_border,
				self.top_left_border,
				self.bottom_left_border),
				key = len)),
			len(max(
				(self.right_border,
				self.top_right_border,
				self.bottom_right_border),
				key = len)))

	def _make_horizontal_border(
		self,
		message_width: int,
		line_count: int
	) -> str:
		pad = self._padding(line_count)

		return (
			" " * pad[0] +
			self.horizontal_border * (message_width + 2) +
			" " * pad[1])

	def _print_character(self) -> None:
		lines = self.character.split("\n")

		padding = " " * self.speech_bubble_line_left_padding
		print(
			padding,
			self.speech_bubble_line,
			" " * (1 + self.speech_bubble_line_right_padding),
			lines[0],
			sep = "")

		padding += " "
		print(
			padding,
			self.speech_bubble_line,
			" " * self.speech_bubble_line_right_padding,
			lines[1],
			sep = "")

		padding += " " * (
			len(self.speech_bubble_line) +
			self.speech_bubble_line_right_padding)

		for i in range(2, len(lines)):
			print(padding, lines[i], sep = "")

	def _say_singleline(self, message: AnyStr) -> None:
		border = self._make_horizontal_border(len(message), 1)

		print(border)
		print(self.left_single_border, message, self.right_single_border)
		print(border)

	def _say_two_lines(self, line1: AnyStr, line2: AnyStr) -> None:
		width = max(len(line1), len(line2))
		border = self._make_horizontal_border(width, 2)

		print(border)
		print(
			self.top_left_border,
			line1.ljust(width),
			self.top_right_border)
		print(
			self.bottom_left_border,
			line2.ljust(width),
			self.bottom_right_border)
		print(border)

	def _say_lines(self, lines: Iterable[AnyStr]) -> None:
		width = len(max(lines, key = len))
		border = self._make_horizontal_border(width, len(lines))

		print(border)
		print(
			self.top_left_border,
			lines[0].ljust(width),
			self.top_right_border)

		for l in lines[1:-1]:
			print(self.left_border, l.ljust(width), self.right_border)

		print(
			self.bottom_left_border,
			lines[-1].ljust(width),
			self.bottom_right_border)
		print(border)
