from __future__ import division
import math as mt
import numpy as NP
import itertools, numbers, random, os, re, sys
import cwgutils
import cwgpatient

def readBGPopulation():
	try:
		with open('./BGP.data','r') as f:
			BGP = pickle.load(f)
	except:
		BGP = {}
	return BGP

def writeBGPopulation(updatedbpopulation):
	with open('./BGP.data','w') as f:
		f.truncate()
		f = pickle.dump(updatedbpopulation, f)
	return None


def createPatientHMaps(patientList, defaultLoc):
	patientMatrix = {}
	ptPop = cwgutils.readLines(patientList)
	for element in ptPop:
		try:
			#Read patientnames from database
			t = open('./nonexistent','r')
		except:
			#Read from local file path provided in list
			with open(os.dir.join(defaultLoc, str(element)),'r') as f:
				patientMatrix[element] = pickle.load(f)
	return patientMatrix

def drugMatrix(druglist, defaultLoc):
	drugMatrix = {}
	drPop = cwgutils.readLinesAndSplit(druglist)
	for element in drPop:
		try:
			#Read patientnames from database
			t = open('./nonexistent','r')
		except:
			#Read from local file path provided in list
			with open(os.dir.join(defaultLoc, str(element)),'r') as f:
				drugMatrix[element] = pickle.load(f)
	return drugMatrix


def createDrugCombinations(drugmatrix):
	combination = {}
	drugList = drugmatrix.keys()
	if len(drugList) <= 1:
		exit(0)
	else:
		for i in range(drugList):
			for j in range(drugList):
				if str(drugList[i])+"+"+str(drugList[j]) not in combination or str(drugList[j])+"+"+str(drugList[i]) not in combination:
					comboName = drugList[i])+"+"+str(drugList[j]
					conCat = drugmatrix[drugList[i]].keys() + drugmatrix[drugList[j]].keys()
					for element in conCat:
						if element in drugmatrix[drugList[i]] and element in drugmatrix[drugList[j]]:
							combination[comboName][element] = (drugmatrix[drugList[i]][element] + drugmatrix[drugList[j]])/2
						else:
							if element in drugmatrix[drugList[i]]:
								combination[comboName][element] = drugmatrix[drugList[i]][element]/2
							elif element in drugmatrix[drugList[j]]:
								combination[comboName][element] = drugmatrix[drugList[j]][element]/2
	print combination.keys()
	return combination

