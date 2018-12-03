from xml.dom.minidom import parse, parseString
import random
import subprocess
import sys, platform
import pdb, time

class Random_Argos:

    def __init__(self, argos_xml = None):
        self.argos_xml = argos_xml

if __name__ == "__main__":
    #files = ['Random_CPFA_r2_tag64_5by5.xml', 'Random_CPFA_r16_tag256_10by10.xml', 'Random_CPFA_r72_tag1024_20by20.xml', 'Random_CPFA_r296_tag4096_40by40.xml']
    files = ['Random_CPFA_r2_tag64_5by5.xml', 'Random_CPFA_r16_tag256_10by10.xml', 'Random_CPFA_r72_tag1024_20by20.xml', 'Random_CPFA_r296_tag4096_40by40.xml', 'Random_CPFA_r1192_tag16384_80by80.xml']
    run_count = 10
    for file in files:
        print file 
        this_run = Random_Argos("./experiments/"+file)
        count =1
        startTime =time.time()
        for _ in range(run_count):
            print "Run "+str(count)
	    singleRun_StartTime =  time.time()
            count = count+1
            output = subprocess.check_output(['argos3 -n -c ' + this_run.argos_xml], shell=True, stderr=subprocess.STDOUT)
	    singleRun_EndTime = time.time()
	    print 'This run takes '+str((singleRun_EndTime-singleRun_StartTime)/60.0)+' minutes...' 
        endTime = time.time()
        print 'The total running time is '+str((endTime-startTime)/60.0)+' minutes...'
