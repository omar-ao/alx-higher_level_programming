#!/usr/bin/python3

import sys


if __name__ == "__main__":
	len_args = len(sys.argv)
	print("{} arguments:".format(len_args - 1))

	for i in range(1, len_args):
		print("{}: {}".format(i, sys.argv[i]))
