Created by Debasmita Bose - Version 1.0 - 18/04/2022
Python Version 2.7
This script performs health checks on RHEL/Centos Operating Systems esp. for Pre-Patch and Post-Patch Health Check details.

Copy the Script under desired folder in the server
# Login as the desired user preferably Admin User/root
# Change the file permission to 755 rwx-r-x-r-x 
  chmod 755 Health_Check_Linux_Patching.py
# Run the script
  python2.7 Health_Check_Linux_Patching.py
 
A menu will appear and you can choose to Run Pre-Patching Check (prior Starting the patching) or Run Post-Patching Check (once the server is patched to newer version or Compare Checks (to verify any differences which can be observed between pre-patch and post-patch health check report). 

Compare Checks is to be run when both Pre-Patch Health Check Report and Post-Patch Health Check Report is available. 
 

