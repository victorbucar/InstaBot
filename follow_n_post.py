import ait
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import subprocess

from bs4 import BeautifulSoup as bs
import os
#ait press enter didnt work using this instead
from pynput.keyboard import Key, Controller

def get_common_pic_path():
    cwd = os.getcwd()
    return cwd+'\pictures\\comum\\'

def get_pic_name(profile_name):
    picName = profile_name
    profileFolderAndPic = 'comum\\'+picName+'.JPG' 
    list_of_files = []


    cwd = os.getcwd()
    image_path = cwd+'\pictures\\'+profileFolderAndPic
    return image_path

caption = " " #Enter the caption for your picture

##for root, dirs, files in os.walk(image_path):
##	for file in files:
##		list_of_files.append(os.path.join(root,file))
##for name in list_of_files:
##    print(name)
##username = "super_cerelepe" #Enter your username
##password = "bright+192191" #Enter your password
profiles_to_follow = []
profiles_with_password = {
                        #   'victorbucar':'Bright+192191',
#                          'marcelaportes': 'alecram',
#                          'trabalho_na_europa': 'alecram',
                        #  'ppl_r_aw_some':'alecram',
#                          'to_na_europa':'alecram',
#                          'minha_doida_vida':'alecram',
                        #  'trenzito_fofo ':'alecram',
#                          'mto_feminina':'alecram',
#                          'super_extraordinario':'alecram1',
#                          'destino_europa_353':'Bright+192191',
#                          'bembem_distante':'bright+192191',
#                          'mto_esperto':'alecram', 
#                          'mto_lindo':'bright+192191', 
#                          'super_cerelepe':'bright+192191',
#                          'kalifa_357':'alecram',
#                          'eu_caduquei':'alecram',
#                          'raissinhasp':'alecram1',
#                          'malu_feris':'alecram,26032906',
#                          'sandrinha_lorenco':'alecram,26032906',
#                          'analu_verves':'alecram,26032906',
#                          'caio_pep':'bright',
#                          'joel_a_raujo':'bright1',
#                          'joanamarcelaalencar' : 'senpass',
#                          'otaku_lovers55':'bright',
#                          'amor_em_famili_a':'senpass',
#                          'el_ruan_te':'1bright',
#                          'tributo_nirvana':'alecram',
#                          'black_pwr_55': 'alecram1',  
#                          'tete_sabati': 'alecram',
#                          'jonan_traub':'lanpass',
#                          'otavio_salabino':'alecram',
#                          'fagner_sou_za':'alecram',
#                          'cris_duar_te':'alecram',
#                          'rubens_pepe':'alecram',
#                          'barto_p_29':'pereira29',
                         'carl_tome_de' : 'Bright192191',
#                          'doug_velozo':'alecram', 
                          }
 


def login(user, pwd):
    login_button = driver.find_element_by_xpath("//button[contains(text(),'Log In')]")
    login_button.click()
    sleep(3)
    username_input = driver.find_element_by_xpath("//input[@name='username']")
    username_input.send_keys(user)
    password_input = driver.find_element_by_xpath("//input[@name='password']")
    password_input.send_keys(pwd)
    password_input.submit()

def close_reactivated():
    try:
        sleep(2)
        not_now_btn = driver.find_element_by_xpath("//a[contains(text(),'Not Now')]")
        not_now_btn.click()
    except:
        pass

def close_notification():
    try: 
        sleep(2)
        close_noti_btn = driver.find_element_by_xpath("//button[contains(text(),'Not Now')]")
        close_noti_btn.click()
        sleep(2)
    except:
        pass

def close_add_to_home():
    sleep(3) 
    close_addHome_btn = driver.find_element_by_xpath("//button[contains(text(),'Cancel')]")
    close_addHome_btn.click()
    sleep(1)

def like_first_post():
    try:
        driver.execute_script("window.scrollTo(0, 200);")
        print('Starting like routine')
        like = driver.find_element_by_class_name('fr66n')
        soup = bs(like.get_attribute('innerHTML'),'html.parser')
        if(soup.find('svg')['aria-label'] == 'Like'):
            print('Clicking like button')
            print(like)
            like.click()
        sleep(2)
    except:
        pass

def follow_users(profile_list):
    for username in profile_list:
        driver.get(main_url +'/' + username + '/')
        sleep(2)
        followButton = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[2]/div/div/div/span/span[1]/button")
                                                    # /html/body/div[1]/section/main/div/header/section/div[2]/div/div[1]/button
        if (followButton.text != 'Message' and followButton.text != ''):
            followButton.click()
            sleep(2)
        else:
            print("You are already following this user")

def rename_file(file_path, user):
    os.rename(file_path+user,file_path+'\Posted.JPG')

def post_picture(user):

####    cwd = os.getcwd()
####    image_path = cwd+'\pictures\\'+profileFolderAndPic
    image_path=get_pic_name(user)
    print(image_path)
    keyboard = Controller()
    try:
        print('Starting post picture routine')
        new_post_btn = driver.find_element_by_xpath("//div[@role='menuitem']").click()
        sleep(1.5)
        print('will post: '+image_path)
        ait.write(image_path) 
        sleep(2)
##    Press and release space
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        sleep(2)

        next_btn = driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()

        sleep(1.5)

        caption_field = driver.find_element_by_xpath("//textarea[@aria-label='Write a caption…']")
        caption_field.send_keys(caption)

        share_btn = driver.find_element_by_xpath("//button[contains(text(),'Share')]").click()
    except:
        print('Could not post picture image not found for ' + user)
    
    rename_file(get_common_pic_path(), user)
    close_notification()

counter = 1

for user, pwd in profiles_with_password.items():
    ### EXECUTA A RENOVACAO DE IP E LIMPEZA DA PASTA PREFETCH e %TEMP%
    if (counter % 5 == 0):
        print('Clean up routine executed')
        subprocess.call([r'C:\Users\marce\AppData\Local\Programs\Python\Python37-32\Scripts\clean_up_temp_prefetch.bat'])
        subprocess.call([r'C:\Users\marce\AppData\Local\Programs\Python\Python37-32\Scripts\releaseip.bat'])
        sleep(60) ## wait 60 sec after clean up and renewal
        subprocess.call([r'C:\Users\marce\AppData\Local\Programs\Python\Python37-32\Scripts\reconnect.bat'])
        sleep(10)




    mobile_emulation = { "deviceName": "iPhone 6" }
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("mobileEmulation", mobile_emulation)
    
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=opts) #you must enter the path to your driver
    #shell = win32com.client.Dispatch("WScript.Shell")
    main_url = "https://www.instagram.com"
    driver.get(main_url)

    sleep(4)



    login(user,pwd)

    sleep(4)

    close_reactivated()

    close_notification()

    close_add_to_home()


    driver.execute_script("window.scrollTo(0, 100);")

##
##    close_notification()
    sleep(2)
    try:
        like_first_post()
    except:
        like_first_post()


    post_picture(user)

    # follow if there are users to follow
    if(len(profiles_to_follow) > 0):
        follow_users(profiles_to_follow)

    sleep(25)
##    os.remove(image_path)
    counter += 1 ## add to counter so it can execute clean up routine
##    driver.quit()


