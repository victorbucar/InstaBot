from time import sleep
import subprocess

while True:
    ### EXECUTA A  PASTA PREFETCH e %TEMP% de 1 em 1 min
    print('Clean up routine executed')
    subprocess.call([r'C:\Users\marce\AppData\Local\Programs\Python\Python37-32\Scripts\clean_up_temp_prefetch.bat'])
    sleep(90)
