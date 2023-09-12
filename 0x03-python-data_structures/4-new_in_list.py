#!/usr/bin/python3
# 4-new_in_list.py

def new_in_list(my_list, idx, element):
	new_list = my_list[:]

	if idx < 0 or idx >= len(my_list):
	return new_list

	return new_list
