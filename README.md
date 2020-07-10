# Ransomware
Simply Ransomware written in Python3.8
Only works on windows

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
  
  7- Check if the ransom file is in our folder 
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
  
  
  
