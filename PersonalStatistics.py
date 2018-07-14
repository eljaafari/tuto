class PersonalStatistics:
    """This class will be the one responsablee for the different statistics
    for here we will distinct all the different results in order to compare the accuracy """
    def __init__(self,healthdata):
        """Constructor for this class. The parameter of the constructor is the dictionnary with the
        health data """
        self.healthdata=healthdata

    def get_pacer_information(self):
        """This function will return only the information comming from the pacer app"""
        print("Obtaining information from pacer")     
        mass=self.healthdata["mass"]
        stepcounter=self.healthdata["stepcounter"]
        sleep=self.healthdata["sleep"]
        flightclimbed=self.healthdata["flightclimbed"]
        activeenergieburned=self.healthdata["activeenergieburned"]
        basalenergieburned=self.healthdata["basalenergieburned"]
        distancewalkingrunning=self.healthdata["distancewalkingrunning"]

        pacermass=get_subset_for_a_source(mass,"Pacer")
        pacerstepcount=get_subset_for_a_source(stepcounter,"Pacer")
        pacersleep=get_subset_for_a_source(sleep,"Pacer")
        pacerflightclimbed=get_subset_for_a_source(flightclimbed,"Pacer")
        paceractiveenergieburned=get_subset_for_a_source(activeenergieburned,"Pacer")
        pacerbasalenergieburned=get_subset_for_a_source(basalenergieburned,"Pacer")
        pacerdistancewalkingrunning=get_subset_for_a_source(distancewalkingrunning,"Pacer")


        
        
        }

    def get_connect_information(self):
        """This function will return only the information from the connect app"""
        print("Obtaining information from connect")

    def get_iphone_information(self):
        """This function will return only the information stored by the iphone """
        print("Obtaining information from the iphone")

    def get_subset_for_a_source(values,nameofthesource):
        newvalues={}
        indicenewvalues=0
        for i in range(0,len(values)):
            if(values[i]["sourceName"]==nameofthesource):
                newvalues[indicenewvalues]=[values["startDate"][i],values["endDate"][i],values["value"][i],values["sourceName"]]
                indicenewvalues=indicenewvalues+1
        return newvalues
