#!/usr/bin/env python
# -*- coding: utf-8 -*-

def _main():

	s = set([1, 2, 3, 4, 5, 5, 2, 1, 2, 4, 3, 2, 1])

	print(s)

	print(type(s))

	if type(s) is set:
		print('s は set です')
	else:
		print('s は set ではありません')

	for e in s:
		print(e)

_main()

