import os
import subprocess
import re

def putFullNameInLicense():
    full_name = raw_input("Enter your full name:")
    f = open("LICENSE", "r")
    license = f.read()
    f.close()
    license = license.replace("Jeffrey Thomas Farrell", full_name)
    wr = open("LICENSE", 'w')
    wr.write(license)
    wr.close()
   
putFullNameInLicense()

bash_command="curl -si https://api.github.com/users/linksapprentice1/repos |     grep ssh_url | cut -d '\"' -f4" 
process = subprocess.check_output(["bash", "-c", bash_command])
process= process.replace("git@github.com:", "https://github.com/")
process_lines=process.split("\n");

for i in process_lines:
    i=i.strip()
    if (i) and ("YACP.git" not in i) and ( "carlin.git" not in i):
        bash_command = "sudo git clone " + i;
        try:
            subprocess.check_output(["bash", "-c", bash_command])
        except:
            "Already downloaded. Moving on..."

        folder_name = i.replace("https://github.com/", "");
        folder_name = re.sub("[a-z1-9]*/","",folder_name)
        folder_name = folder_name.replace(".git","");
        bash_command = "sudo cp LICENSE " + folder_name + "/";
        subprocess.check_output(["bash", "-c", bash_command])
        subprocess.call ("bash pushLicense.sh "+ folder_name, shell=True);
