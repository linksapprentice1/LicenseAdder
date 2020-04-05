import os
import subprocess
import re

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
        print folder_name
        bash_command = "sudo cp LICENSE " + folder_name + "/";
        subprocess.check_output(["bash", "-c", bash_command])
        print("here1")
        subprocess.call ("bash pushLicense.sh "+ folder_name, shell=True);




          

