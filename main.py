#!/usr/bin/env python3

from typing import List
import sys
from cowsay import Character

def main(args: List[str]) -> int:
	message = args[1] if len(args) > 1 else sys.stdin.read()

	cowsay = Character()
	cowsay.say(message)

	return 0

if __name__ == "__main__":
	sys.exit(main(sys.argv) or 0)
