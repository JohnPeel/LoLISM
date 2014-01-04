#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import argparse
import LoLISM
import pyamf

from Tkinter import *
from tkMessageBox import *
from ttk import *


class SummonerSelection(Frame):
	def submit(self):
		self.summoner = self.summoner_value.get()
		self.quit()

	def __init__(self, parent, summoners):
		Frame.__init__(self, parent)
		self.pack()
		
		self.summoner = None
		
		self.summoner_value = StringVar()
		self.summoners = Combobox(self, exportselection=0, textvariable=self.summoner_value, values=summoners, state='readonly')
		self.summoners.current(0)
		self.summoners.pack(side='left', padx=5, pady=5)
		
		self.button = Button(self, text="Cancel", command=self.quit)
		self.button.pack(side='right', padx=5, pady=5)
		
		self.button = Button(self, text="Inject", command=self.submit)
		self.button.pack(side='right', padx=5, pady=5)		

def process_cmdline(argv):
	parser = argparse.ArgumentParser(description='League of Legends - Item Set Manager', prog='LoLISM-gui')
	
	itemset_group = parser.add_mutually_exclusive_group(required=True)
	itemset_group.add_argument('-l', '--link', help='ItemSet Link')
	itemset_group.add_argument('-j', '--json', help='JSON File')
	
	return parser.parse_args(argv)

def main(argv = None):
	master = Tk()
	master.title('LoLISM - Summoner Selection')
	master.withdraw()
	
	args = process_cmdline(argv)
	
	itemset = LoLISM.ItemSet(args.json)
	if (args.json is None):
		itemset.link = args.link
	
	path = LoLISM.getSummonersPath()
	summoners = LoLISM.getSummoners(path=path)
	summoner = None
	
	if (len(summoners) > 1):
		selection = SummonerSelection(master, summoners)
		master.deiconify()
		selection.mainloop()
		master.withdraw()
		summoner = selection.summoner
		if (summoner is None):
			master.destroy()
			return 0
	elif (len(summoners) == 1):
		summoner = summoners[0]
	else:
		showerror('LoLISM', 'I could not find any summoners...')
		master.destroy()
		return 1
	
	try:
		propfile = LoLISM.PropertiesFile(os.path.join(path, summoner + '.properties'))
		propfile.read()
		itemSets = LoLISM.ItemSetDecoder().decode(propfile.data.itemSets)
		itemSets.itemSets.append(itemset)
		propfile.data.itemSets = itemSets
		propfile.write()
		showinfo('LoLISM', 'Injected itemset "%s" into summoner "%s".' % (itemset.title, summoner))
	except (pyamf.EOStream, AttributeError) as e:
		showerror('LoLISM', 'Summoner file seems to be empty...')
		master.destroy()
		return 1
	
	master.destroy()	
	return 0

if (__name__ == '__main__'):
	status = main()
	sys.exit(status)