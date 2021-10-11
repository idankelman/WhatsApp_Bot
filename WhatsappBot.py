from selenium import webdriver
from selenium.webdriver.common.by import By

import time 
import datetime
from datetime import datetime


#================================================================================
#decleration of variables:
#================================================================================ 
Statement = True
Favorites = ['Hagar ❣️','Omer The Legendary Warrior','Soy Yo','The Wolf From Jerusalem 📈']
FavIndex = -1
SavedPics = ['░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░\n░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░\n░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░']

def WriteToUser():

    Message = input('-------------------------------------------------------\n what would you like to write?> :')
    Counter= input('how many times would you like to write that message >:')
    BackTime = input('Would you like to set a time for the message to appear? [Y/N]')
    if BackTime =='Y':
        Timer = input('Specify the time that you want the message to be sent at e.g <15:32> :  ')
        now= datetime.now()
        Timer=Timer + ':00'
        TimerObject = datetime.strptime(Timer,'%H:%M:%S')
        my_datetime = now.replace(hour=TimerObject.time().hour, minute=TimerObject.time().minute, second=TimerObject.time().second, microsecond=0)
        while datetime.now()< my_datetime: 
            print('still waiting for timer : ')
            print('Time Now : "{}"'.format(datetime.now()))
            time.sleep(5)

    Count_=1
    try :
        Count_ = (int) (Counter)
        if Count_ <=0 :
            Count_ =1
    except:
        print('you didnt pass valid number , therefor the counter will be 1 ')
        Count_ =1

    TextBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    
    for i in range(0,Count_):
        TextBox.send_keys(Message)
        SendBtn = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
        SendBtn.click()
        
        

   



#================================================================================
#Connect to the webBrowser:
#================================================================================

driver = webdriver.Chrome()
driver.get('https://www.whatsapp.com')

WhatsUp_Btn= driver.find_element_by_xpath('//*[@id="hide_till_load"]/div[1]/div[1]/header/div/div[2]/span[1]/a[1]/h5')
WhatsUp_Btn.click()

#================================================================================
#Main Menu
#================================================================================


Action = input('________________________________________________________________________________\n welcome to whatsUp bot by idan kelman ,\n scan the QR code and when youre done , click any key to continue, or click Exit to exit')

while Action != 'Exit':
    print('You have Sucsessfuly logged in , what would you like to do ?')
    print('[1] press 1 to enter who would you like to send your message to')
    print('[2] press 2 to get favorite list information' )
    print('[3] press 3 to add someone to favorites ')
    
    answer = input(':')
    if answer == '1':
        Loop = 3 
        userName = input('Enter the username: ') 
        while Loop> 0 :
            try: 
                UserBtn = driver.find_element_by_xpath('//span[@title = "{}"]'.format(userName))
                UserBtn.click()
                Loop= -2
            except :
                print('failed , trying again ')
                Loop= Loop-1
                userName = userName[0:len(userName)-1] 
        if Loop == -2:
            Statement = False
        else:
            print('the given user could not be found , try looking again(watch your upper and lower cases)')
    if answer == '2':
        print('\n your favorites are: ')
        i = 0 
        for fav in Favorites:
            print('index = "{}" , name : "{}"'.format(i,fav))
            i=i+1
        while FavIndex < 0 or FavIndex >len(Favorites):
            FavIndex = (int)(input('type which index would you like write to'))
        UserBtn = driver.find_element_by_xpath('//span[@title = "{}"]'.format(Favorites[FavIndex]))
        UserBtn.click()
        Statement = False
        FavIndex = -1

    if answer == '3':
        NewFav = input('type the exact name of who would you like to add to your favorites:')
        Favorites.append(NewFav)
        print('User was added sucsessfuly to Favorties')

    if not Statement:
        WriteToUser()
        Statement = True
    Action = input('________________________________________________________________________________\n welcome to whatsUp bot by idan kelman ,\n scan the QR code and when youre done , click any key to continue, or click Exit to exit')


 #================================================================================
 #Write the Message 
 #================================================================================


   
    
