import xml.etree.ElementTree as ET
import pandas as pd 

class AppleHealthLib:
    """ This class objective is to read the xml file given by apple health
    The first parameter from the constructor is the object itself 
    The second parameter from the constructoris the filepath to the xml file"""
    def __init__(self,xmlfilepath):
        """ constructor from the object AppleHealtLib it work as a reader"""
        self.record= pd.DataFrame()
        self.userData= pd.DataFrame()     
        tree = ET.parse(xmlfilepath)
        self.root= tree.getroot()


    def get_user_data(self,rootfromXml):
        """This function is the one thar recover the data we want ro read thom the xml"""
        print("Begin reading")
        height=0
        mass={}
        stepcounter={}
        sleep={}
        flightclimbed={}
        activeenergieburned={}
        basalenergieburned={}
        distancewalkingrunning={}
        indiceofmass=0
        indiceofstep=0
        indiceofsleep=0
        indiceofflightclimbed=0
        indiceofactiveenergieburned=0
        indiceofbasalenergieburned=0
        indiceofdistancewalkingrunning=0
        for child in rootfromXml:
            if(child.tag=="Record"):
                if(child.attrib["type"]=="HKQuantityTypeIdentifierStepCount"): #stepCounter
                    stepcounter[indiceofstep]=[child.attrib["startDate"],child.attrib["endDate"],child.attrib["value"],child.attrib["sourceName"]]
                    indiceofstep=indiceofstep+1
                elif(child.attrib["type"]=="HKQuantityTypeIdentifierBodyMass"): #mass
                    mass[indiceofmass]=[child.attrib["startDate"],child.attrib["endDate"],child.attrib["value"],child.attrib["sourceName"]]
                    indiceofmass=indiceofmass+1
                elif(child.attrib["type"]=="HKQuantityTypeIdentifierHeight"): #height
                    height=child.attrib["value"]
                elif(child.attrib["type"]=="HKCategoryTypeIdentifierSleepAnalysis"): # sleepAnalyse
                    sleep[indiceofsleep]=[child.attrib["startDate"],child.attrib["endDate"],child.attrib["value"],child.attrib["sourceName"]]
                    indiceofsleep=indiceofsleep+1
                elif(child.attrib["type"]=="HKQuantityTypeIdentifierFlightsClimbed"): #?
                    flightclimbed[indiceofflightclimbed]=[child.attrib["startDate"],child.attrib["endDate"],child.attrib["value"],child.attrib["sourceName"]]
                    indiceofflightclimbed=indiceofflightclimbed+1
                elif(child.attrib["type"]=="HKQuantityTypeIdentifierActiveEnergyBurned"): #calories
                    activeenergieburned[indiceofactiveenergieburned]=[child.attrib["startDate"],child.attrib["endDate"],child.attrib["value"],child.attrib["sourceName"]]
                    indiceofactiveenergieburned=indiceofactiveenergieburned+1                
                elif(child.attrib["type"]=="HKQuantityTypeIdentifierBasalEnergyBurned"): #calories
                    basalenergieburned[indiceofbasalenergieburned]=[child.attrib["startDate"],child.attrib["endDate"],child.attrib["value"],child.attrib["sourceName"]]
                    indiceofbasalenergieburned=indiceofbasalenergieburned+1                              
                elif(child.attrib["type"]=="HKQuantityTypeIdentifierDistanceWalkingRunning"): #calories
                    distancewalkingrunning[indiceofdistancewalkingrunning]=[child.attrib["startDate"],child.attrib["endDate"],child.attrib["value"],child.attrib["sourceName"]]
                    indiceofdistancewalkingrunning=indiceofdistancewalkingrunning+1                                  
                else:
                    print(child.attrib["type"])
        print("Done reading")
        return {        
        "height":height,
        "mass":mass,
        "stepcounter":stepcounter,
        "sleep":sleep,
        "flightclimbed":flightclimbed,
        "activeenergieburned":activeenergieburned,
        "basalenergieburned":basalenergieburned,
        "distancewalkingrunning":distancewalkingrunning,
        }


    def export_heath_in_csv(resultstoexport,filepath):
        print("Begin of export")
        height=pd.DataFrame(resultstoexport["mass"])
        mass=pd.DataFrame(resultstoexport["mass"])
        stepcounter=pd.DataFrame(resultstoexport["stepcounter"])
        sleep=pd.DataFrame(resultstoexport["sleep"])
        flightclimbed=pd.DataFrame(resultstoexport["flightclimbed"])
        activeenergieburned=pd.DataFrame(resultstoexport["activeenergieburned"])
        basalenergieburned=pd.DataFrame(resultstoexport["basalenergieburned"])
        distancewalkingrunning=pd.DataFrame(resultstoexport["distancewalkingrunning"])
        height.to_csv(filepath + "height.csv")
        mass.to_csv(filepath + "mass.csv")
        stepcounter.to_csv(filepath + "stepcounter.csv")
        sleep.to_csv(filepath + "sleep.csv")
        flightclimbed.to_csv(filepath + "flightclimbed.csv")
        activeenergieburned.to_csv(filepath + "activeenergieburned.csv")
        basalenergieburned.to_csv(filepath + "basalenergieburned.csv")
        distancewalkingrunning.to_csv(filepath + "distancewalkingrunning.csv")           
        print("End of export")
            

        
        
    

    

            

