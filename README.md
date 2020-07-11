<img src="https://cdn.onlinewebfonts.com/svg/img_556375.png" width="200">










# Ransomware Bad Buffoon

Ransomware written in Python3.x

Only works on windows

Can encrypt files with this extension : ['txt','jpg','jpeg','png','docx','doc','gif','html','ico','mp3','mp4','odt','odp','ods','odg','pdf','ppt','pps','pptx','py','zip','tar','md','xls','xlsx','wav','xml','log','exe']

# Dependencies : 
  
  Cryptography
  
  PIL
  
  pyperclip
  
 
 # How the ransomware works ? 
 
  1- Try to find the windows letter partition and create a folder named 'test' into  {}\\Users\\{}\\Appdata\\ 
  
  2- Then download images from Internet 
  
  3- Generate the encryption key ( AES 128-bit ) 
  
  4- Send the encryption key to the server 
  
  5- Encrypt files and rename them with '.encrypted'
  
  6- Change wallpaper with a dirty buffoon
  
  7- Send the ransomware file into our folder
  
  8- Add/Check the key in the registre for launch ransom every time victim turn on computer
  
  9- Create a note in Desktop
  
  10- Generate a Identification Key and save it into our folder
  
  11- Write the deadline into a file
  
  12- Launch the GUI 
  
# If decryption key is right :

  1- Decrypt files and rename them without '.encrypted'
  
  2- Delete our folder and delete the key in the registre 
  
# If victim cross the deadline : 

  Delete encrypted files
  
  
  
# Weekness 

  Pretty slow to encrypt big data
  
  Internet connection is fundamental
  
  Can't spread throught a network
  
  If encrypted files are moved or renamed, decryption will probably fail 
  
  
# Server 

  Listen for any connection 
  
  When a connection pop create a file with the IP target , decryption key , time
