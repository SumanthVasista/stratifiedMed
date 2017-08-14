from __future__ import division
import math as mt
import numpy as NP
import itertools, numbers, random, os, re, sys, operator
import cwgutils
import cwgpatient

def normalizeHeatMap(patientPathwaysSig):
	for element in patientPathwaysSig:
		patientPathwaysSig[element] = mt.tanh(patientPathwaysSig[element]/2) #Normalizing all values to range of -1 to 1
	return patientPathwaysSig

def clusterPatient(patient, bPopulation):
	searchSpace = []
	searchSpaceReduced = []
	if len(population.keys()) > 5:

		for element1 in bPopulation.keys():
			searchSpace.append(bPopulation[element1])

		while len(searchSpace) != 0:
			for query in patient.keys():
				for otherPatient in bPopulation:
					if query not in otherPatient or patient[query]*otherPatient[query] <= 0:
						searchSpaceReduced = []
						for element2 in searchSpace:
							searchSpaceReduced.append(element2)
						searchSpace.pop(searchSpace.index(otherPatient))
					if len(searchSpace) == 0:
						break
			break
	closestCousins = {}
	for element in searchSpaceReduced:
		if len(element.keys()) >= len(patient.keys()):
			if len(patient.keys()) / len(element.keys()) > 0.7:
				closestCousins[str(element)] = len(patient.keys()) / len(element.keys())
		elif len(element.keys()) < len(patient.keys()):
			if len(element.keys()) / len(patient.keys()) > 0.7:
				closestCousins[str(element)] = len(element.keys()) / len(patient.keys())
	return closestCousins

def identifyClusters(ccset):
	CLUSTERS = {}
	patientSet = ccset.keys()
	for patient in patientSet:
		group = [patient]
		for otherPatient in ccset:
			if patient != otherPatinet:
				if patient in ccset[otherPatient]:
					group.append(str(otherPatient))

		for element in group:
			for groups in CLUSTER:
				if element not in groups:
					if len(group) > 3:
						CLUSTERS[str(len(CLUSTERS)+1)] = group
				else:
					if len(group) > 3:
						groups.append(group)
	return CLUSTERS

def stratifyPopulation(population, bPopulation):
#	Data structure of population:
#	mainObject : {
#		element : {
#			pathway_scores : {
#		}
#	}
	ClosestCousinSet = {}
	populationList = population.keys()
	for patient in population:
		patient = normalizeHeatmap(patient)
		ClosestCousinSet[str(patient)] = clusterPatient(patient, bPopulation)
		if patient not in bPopulation:
			bPopulation[str(patient)] = population[patient]
	Clusters = identifyClusters(ClosestCousinSet)
	print "Identified", len(Clusters), "from population of n = ", len(population), "and a backgroup population of n = ", len(bPopulation)
	return bPopulation, Clusters

def extractCommonFeatures(group):
	




