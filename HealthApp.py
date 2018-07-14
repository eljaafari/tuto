from Personne import Personne
from AppleHealthLib import AppleHealthLib
import xml.etree.ElementTree as ET
import glob
if __name__ == "__main__":
    filepathtothedata="/Users/keine/Documents/python/data/"
    print("-------Welcome to the Health App--------") 
    user=Personne("Eljaafari","Nail",25,109,176)   
    #check if the csv are akready there
    listofcsvfiles=glob.glob("/home/olivier/scripts/*.csv")
    if(len(listofcsvfiles)==0):
        #Read the Xml file
        data=AppleHealthLib(filepathtothedata + "data.xml")
        healthresults=data.get_user_data(data.root)
        AppleHealthLib.export_heath_in_csv(healthresults,"/Users/keine/Documents/python/data/")
        





