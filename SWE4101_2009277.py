weightList=[]
heightList=[]
ageList=[]
genderList=[]
bmiList=[]

def main():
    
    #program introduction
    print("This program will calculate Your BMI. It's working in sertine patern, so:")
    print("in stage 1 we will ask for basic info about You like age and gender")
    print("in stage 2 we will ask You to choose units of weight and height plus to give us thoes data")
    print("in stage 3 program will calculate you BMI")
    print("in stage 4 program will give You statistics for all the data You will put it")
    input("press 'enter' to enter the data")

    #basic data as age and gender
    def ageTry():
        
        try:
            global age
            age=float(input("whats your age?:"))
            ageList.append(age)
            
        except ValueError:
            print("thats not age value, try one more time")
            ageTry()
    ageTry()

    def genderCheck():

        global gender
        gender=input("Whats Your gender: \nfor male write 'm', \nfor female 'f', \nfor other 'o', \nor 'x' if you rather not to say")

        if gender == 'm':
            genderList.append(gender)
            
        elif gender == 'f': 
            genderList.append(gender)
            
        elif gender == 'o':         
            genderList.append(gender)
            
        elif gender == 'x':
            genderList.append(gender)
            
        else:
            print("thats incorect value, try one more time")
            genderCheck()
    genderCheck()
     
    #convert units
    
#weight function (choose unit, convert them to kg, check for errors to count it corectly)
    def weightCheck():
            
        global weightChoice
        weightChoice=input("choose your weight unit, \nfor kilograms write 'kg', \nfor pounds 'lbs', \nfor stone 'st':")
            
        try:
            global weight
            w=float(input("whats your weight (remember to put it in the unit you choose before) use '.' as separator?:"))
                
            while True:
                    
                if weightChoice=='kg' .casefold():
                    weight=float(w)
                    print(weight,'kg')
                    break
                    
                elif weightChoice=='lbs' .casefold():
                    weight=float(w*2.2046)
                    print(weight,'kg')
                    break
                    
                elif weightChoice=='st' .casefold():
                    weight=float(w*6.35)
                    print(weight,'kg')
                    break
                else:
                    print("the chosen units are incorect, try one more time")
                    weightCheck()
            
            weightList.append(weight)
            
        except ValueError:
            print("thats not float value, try one more time")
            weightCheck()
                
    weightCheck()
    
#height function (choose unit, convert them to kg, check for errors to count it corectly)

    def heightCheck():
            
        global heightChoice
        heightChoice=input("choose your height unit, \nfor meters write 'm', \nfor centimeters 'cm', \nfor feet 'ft', \nfor inches 'inch':")
            
        try:
            global height

            h=float(input("whats your height (remember to put it in the unit you choose before) use '.' as separator?:"))
            while True:
                    
                if heightChoice=='m' .casefold():
                    height=float(h)
                    print(height,'m')
                    break
                    
                elif heightChoice=='cm' .casefold():
                    height=float(h/100)
                    print(height,'m')
                    break
                    
                elif heightChoice=='inch' .casefold():
                    height=float(h*39.37)
                    print(height,'m')
                    break
                    
                elif heightChoice=='ft' .casefold():
                    height=float(h/0.3048)
                    print(height,'m')
                    break
                else:
                    print("the chosen units are incorect, try one more time")
                    heightCheck()
                    
            heightList.append(height)
                
        except ValueError:
            print("thats not float value, try one more time")
            heightCheck()
                
    heightCheck()

# calculate BMI + give the feedback + check if we are working with adult or child and give feedback about that too

    def calculateBMI():

#calulate BMI (round it to ,00) 
        
        z=round(float(weight/(height*height)),2)
        bmiList.append(z)

#define the feedback responds

        def resultBMI():
            
            if z < 18.5:
                print("Your BMI is :",z," that means you're underweight")
                
            elif z >= 18.5 and  z < 25:
                print("Your BMI is :",z," that means you're in the healthy weight")
                
            elif z >= 25 and z < 30:
                print("Your BMI is :",z," that means you're overweight")
                
            elif z >= 30 and z <40:
                print("Your BMI is :",z," that means you're obese")

#check age and give feedback for adult and child                
                
        def ageCheck():
            
            if age > 2 and age < 18:
                print ("Your BMI is:",z)
                print("as a child you should take this result to the child BMI charts and check it with the chart")
                
            elif age> 18:
                resultBMI()
                
        ageCheck()

    calculateBMI()

def statisticGeneral():        
#funkcje statystyczne
    def statisticBmi():

        #avarage BMI (srednia)
        a=round(sum(bmiList)/len(bmiList),2)

        print("the avarage BMI is: ",a)

        #print the highest BMI
        print("the highest BMI in that group is: ",max(bmiList))

        #print the lowest BMI
        print("the lowest BMI in that group is: ",min(bmiList))

        #mod (mediana)
        bmiList.sort()
        z=int(len(bmiList)%2)
        y=int(len(bmiList)/2)
    
        if z==0:
      
            print("the middel BMI in that group is: ",round(((bmiList[y-1]+bmiList[y])/2),2))
        else:
            print("the middel BMI in that group is: ",round(bmiList[y],2))

        #percentBMI
        def percentBMI():
        
            bmiList.sort()
            tempListToLow=[]
            tempListOk=[]
            tempListToHigh=[]
            tempListObese=[]
            tempListAdvice=[]
        
            for x in bmiList:
            
                if x <= 18.5:
                    percent1 = tempListToLow.append(x)
            
                elif x > 18.5 and x <=24.9:
                    percent2 = tempListOk.append(x)
                 
                elif x > 24.9 and x <=29.9:
                    percent3 = tempListToHigh.append(x)
                
                elif x > 29.9 and x <=39.9:
                    percent4 = tempListObese.append(x)
                
                elif x > 39.9:
                    percent5 = tempListAdvice.append(x)
            
            print("The ",round((len(tempListToLow)/len(bmiList)*100),2),"% of the group is underweight")
            print("The ",round((len(tempListOk)/len(bmiList)*100),2),"% of the group is with healthy weight")
            print("The ",round((len(tempListToHigh)/len(bmiList)*100),2),"% of the group is overweight")
            print("The ",round((len(tempListObese)/len(bmiList)*100),2),"% of the group is obese")
            print("The ",round((len(tempListAdvice)/len(bmiList)*100),2),"% of the group need to get medical advice\n")
        
        percentBMI()
    
    def statisticHeight():

        #avarage height (srednia)
        a=round(sum(heightList)/len(heightList),2)

        print("the avarage height is: ",a)

        #print the highest
        print("the highest in that group is: ",max(heightList))

        #print the lowest 
        print("the lowest in that group is: ",min(heightList))

        #mod (mediana)
        heightList.sort()
        z=int(len(heightList)%2)
        y=int(len(heightList)/2)
    
        if z==0:
            print("the middel hight in that group is: ",(heightList[y-1]+heightList[y])/2)
        
        else:
            print("the middel hight in that group is: ",heightList[y])
        print("")

    def statisticWeight():

        #avarage weight (srednia)
        a=round(sum(weightList)/len(weightList),2)

        print("the avarage weight is: ",a)

        #print the heaviest
        print("the heaviest in that group is: ",max(weightList))

        #print the lightest 
        print("the lightest in that group is: ",min(weightList))

        #mod (mediana)
        weightList.sort()
        z=int(len(weightList)%2)
        y=int(len(weightList)/2)
        
        if z==0:
            print("the middel hight in that group is: ",(weightList[y-1]+weightList[y])/2)
            
        else:
            print("the middel hight in that group is: ",weightList[y])
            
        print("")

    def statisticAge():

        #avarage age (srednia)
        a=round(sum(ageList)/len(ageList),2)
    
        print("the avarage age is: ",a)

        #print the oldest
        print("the oldest in that group is: ",max(ageList))

        #print the youngest
        print("the youngest in that group is: ",min(ageList))

        #mod (mediana)
        ageList.sort()
        z=int(len(ageList)%2)
        y=int(len(ageList)/2)
        
        if z==0:
            print("the middel age in that group is: ",(ageList[y-1]+ageList[y])/2)
            
        else:
            print("the middel age in that group is: ",ageList[y])

    #agePercent
        def percentAge():
            
            tempListKid=[]
            tempListYAdult=[]
            tempList20=[]
            tempList30=[]
            tempList40=[]
            tempList50=[]
            tempList60=[]
            tempList70=[]
            
            for x in ageList:
                if x < 18:
                    percent1 = tempListKid.append(x)
                    
                elif x>=18 and x<20:
                    percent2 = tempLisYAdult.append(x)
                    
                elif x >=20  and x <30:
                    percent3 = tempList20.append(x)
                    
                elif x >= 30 and x<40:
                    percent4 = tempList30.append(x)
                    
                elif x >= 40 and x<50:
                    percent5 = tempList40.append(x)
                    
                elif x >=50  and x <60:
                    percent6 = tempList50.append(x)
                    
                elif x >= 60 and x<70:
                    percent7 = tempList60.append(x)
                    
                elif x >= 70 :
                    percent8 = tempList70.append(x)
                    
            print("The ",round((len(tempListKid)/len(ageList)*100),2),"% of the group are kids")
            print("The ",round((len(tempListYAdult)/len(ageList)*100),2),"% of the group is between 18 and 20 years old")
            print("The ",round((len(tempList20)/len(ageList)*100),2),"% of the group is in their 20's")
            print("The ",round((len(tempList30)/len(ageList)*100),2),"% of the group is in their 30's")
            print("The ",round((len(tempList40)/len(ageList)*100),2),"% of the group is in their 40's")
            print("The ",round((len(tempList50)/len(ageList)*100),2),"% of the group is in their 50's")
            print("The ",round((len(tempList60)/len(ageList)*100),2),"% of the group is in their 60's")
            print("The ",round((len(tempList70)/len(ageList)*100),2),"% of the group is in older than 70\n")
            
        percentAge()
        
    #gender statistic
    def statisticGender():
        
        genderList.sort()
        tempListM=[]
        tempListF=[]
        tempListO=[]
        tempListX=[]
           
        for x in genderList:
            
            if x == 'm' .casefold():
                percent1 = tempListM.append(x)
                
            elif x == 'f' .casefold():
                percent2 = tempListF.append(x)
                
            elif x == 'o' .casefold():
                percent3 = tempListO.append(x)
                
            elif x == 'x' .casefold():
                percent4 = tempListX.append(x)
                
        print("The ",round((len(tempListM)/len(genderList)*100),2),"% of the group are males")
        print("The ",round((len(tempListF)/len(genderList)*100),2),"% of the group are females")
        print("The ",round((len(tempListO)/len(genderList)*100),2),"% of the group are diferent gender then above")
        print("The ",round((len(tempListX)/len(genderList)*100),2),"% of the group decided not to reveal their gender")

    statisticBmi()
    statisticHeight()
    statisticWeight()
    statisticAge()
    statisticGender()
    
main()

#loop the program so we can add more date sets
def Loop():
    
    while True:

        YesNo=input("Do you want to continue? Y for Yes (insert data of another person), \nN for No (entered data for whole group and You want ot go to statistic): ")

        if YesNo=="Y" or YesNo=="y" .casefold():
        
            print("Thank You, let`s continiue")
            main()
                
        elif YesNo=="N" or YesNo=="n" .casefold():

            print("\nOK, here are the data for Your group\n")
            print(weightList,"\n", heightList,"\n", ageList,"\n", genderList,"\n",bmiList)
            print("\nand, here are the statistics for Your group\n")
            statisticGeneral()
            print("\nthank You for using my program")
            break
Loop()

def restart():
    #clear lists and run the program one more time
    while True:

        YesNo=input("Do you want to run program for another group? Y for Yes (the program will restart with empty lists), \nN for No (the program will end): ")

        if YesNo=="Y" or YesNo=="y" .casefold():
        
            print("Thank You, let`s restart the program")
            #clearing lists
            weightList.clear
            heightList.clear
            ageList.clear
            genderList.clear
            bmiList.clear

            tempListToLow.clear
            tempListOk.clear
            tempListToHigh.clear
            tempListObese.clear
            tempListAdvice.clear

            tempListKid.clear
            tempListYAdult.clear
            tempList20.clear
            tempList30.clear
            tempList40.clear
            tempList50.clear
            tempList60.clear
            tempList70.clear

            tempListM.clear
            tempListF.clear
            tempListO.clear
            tempListX.clear

            main()
            Loop()
        #end the program        
        elif YesNo=="N" or YesNo=="n" .casefold():

            print("\nthank You, the program has ended")
            break
restart()
