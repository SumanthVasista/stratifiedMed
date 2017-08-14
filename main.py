import icogutils, mathutils, cwgutils
import sys, os


if __name__=="__main__":
	#Read and parse data
	script, grouplist, druglist = sys.argv
	population = icogutils.createPatientHMaps(grouplist)
	drugMatrix = icogutils.loadDrugs(druglist)
	combinations = icogutils.createDrugCombinations(drugMatrix)
	
	#Read background population dataset
	bPopulation = icogutils.readBGPopulation()

	#Stratification

	#Step 0 : Create clusters from population
	UpdatedbPopulation, StratifiedSets = mathutils.stratifyPopulation(population, bPopulation)

	#Write Back new population into existing BGP
	writeBGPopulation(UpdatedbPopulation)

	#Step 1	: Calculate <Cx> scores

	#Step 2 : Calculate <CDI> scores

	#Step 3 : Calculate relative efficacy distribution

