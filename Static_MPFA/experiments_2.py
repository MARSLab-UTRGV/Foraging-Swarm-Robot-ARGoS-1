from xml.dom.minidom import parse, parseString
import random
import subprocess
import sys, platform
import pdb, time

class Random_Argos:

    def __init__(self, argos_xml = None):
        self.argos_xml = argos_xml

if __name__ == "__main__":
    #system = 'linux' if platform.system() == 'Linux' else 'mac'
    files = ['04_07_19_vary_speed_2over3_scaling/Random_MPFA_r112_d17_tag64_8by8.xml', '04_07_19_vary_speed_2over3_scaling/Random_MPFA_r4864_d257_tag4096_64by64_mapTo_r960_d65_tag1024_32by32.xml']
    run_count = 20
    for file in files:
        print(file)        this_run = Random_Argos("./experiments/"+file)
        count =1
        startTime =time.time()
        for _ in range(run_count):
            print("Run "+str(count))            singleRun_StartTime =  time.time()
            count = count+1
            output = subprocess.check_output(['argos3 -c ' + this_run.argos_xml], shell=True, stderr=subprocess.STDOUT)
            singleRun_EndTime = time.time()
            print('This run takes '+str((singleRun_EndTime-singleRun_StartTime)/60.0)+' minutes...')        endTime = time.time()
        print('The total running time is '+str((endTime-startTime)/60.0)+' minutes...')