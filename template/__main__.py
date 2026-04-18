from template import __version__

import sys
import logging
import pygame

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

from template.app import App

def main():
	parser = ArgumentParser(
		formatter_class=lambda prog: ArgumentDefaultsHelpFormatter(prog, width=120, max_help_position=50)
	)

	parser.add_argument("-l", "--log-level", type=str, choices=[level for level in logging._nameToLevel.keys()], default="INFO", metavar="level", help="set logging level")
	parser.add_argument("-v", "--version", action="store_true")
	parsed = parser.parse_args()

	logging.basicConfig(level=getattr(logging, parsed.log_level))

	if (parsed.version):
		print(__version__)
		exit(0)

	pygame.init()

	app = App()

	while (app.update()):
		pass

	app.quit()
	pygame.quit()

if __name__ == "__main__":
	main()
