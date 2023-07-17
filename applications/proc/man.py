#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  man
#  
#  Copyright 2023 Felipe Souza <lubuntu@lubuntu>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

if cmd != "":
	try:
		with open(f"{root}/proc/docs/{cmd}", "r") as help_text:
			print(recognize(help_text.read()))
			
	except FileNotFoundError: print(f"ash: man: {cmd}: page not found")
else: 
	try:
		docs = os.listdir(f"{root}/proc/docs")

		print(f"{appname} v{version} - Manual pages:\n")
		n = 1
		for page in docs: 
			print(f"\t{page}", end="")

			if n == 3: 
				print("")

				n = 0
			
			n = n + 1

	except Exception as traceback: print("ash: man: failed to list manual pages.")
