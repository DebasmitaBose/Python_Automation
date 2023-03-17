# This Python file uses the following encoding: utf-8
import subprocess
import difflib
import re

class HealthCheck:
        def __init__(self, file_path):
            self.file_path = file_path
        def check_boot(self):
            df_output = subprocess.check_output(["df", "-h", "/boot"])
            df_line = df_output.splitlines()[1]
            boot_usage = df_line.split()[2]
            boot_pct = df_line.split()[4]
            print("******************************************************************************************")
            print("*                                      SUMMARY                                           *")
	    print("******************************************************************************************")
	    print("......................................Boot Space..........................................")
            print("The /boot partition is using {} of disk space which is {} of utilization \n".format(boot_usage,boot_pct))
            return df_line
	def kernel_version(self):
	    uname_output = subprocess.check_output(["uname", "-a"])
	    print("......................................Kernel Details.......................................")
            print(uname_output)
	    print("\n")
            return uname_output
	def uptime(self):
	    uptime_1=subprocess.check_output(["uptime"])
	    print("......................................Uptime.......................................")
	    print(uptime_1)
	    print("\n")
	    return uptime_1
	def release(self):
	    rhel_rel=subprocess.check_output(["cat", "/etc/redhat-release"])
	    print("......................................Redhat Release.......................................")
	    print(rhel_rel)
	    print("\n")
	    return rhel_rel
	def fstab(self):
	    fstab=subprocess.check_output(["grep","-v","^#", "/etc/fstab"])
	    print("......................................FSTAB Entries.......................................")
	    print(fstab)
	    print("\n")
	    return fstab
        def mount(self):
	    df_mount=subprocess.check_output(["df","-kh"])
            print("......................................DF Entries.......................................")
	    print(df_mount)
	    print("\n")
	    return df_mount
        def waagent_1(self):
	    waagent=subprocess.check_output(["systemctl","status", "waagent"])
	    print("......................................WAAGENT Entries.......................................")
	    print(waagent)
	    print("\n")
	    return waagent
        def java_ver(self):
	    print("......................................Java Version.......................................")
	    java1=subprocess.check_output(["java","-version"])
	    print(java1)
	    print("\n")
	    return java1
        def store_result(self):
            boot_space = self.check_boot()
            uname_output=self.kernel_version()
            uptime_1=self.uptime()
            rhel_rel=self.release()
            fstab=self.fstab()
            df_mount=self.mount()
            waagent=self.waagent_1()
            java=self.java_ver()
	    with open(self.file_path, "w") as file:
            	file.write(boot_space)
	    	file.write(uname_output)
	    	file.write(uptime_1)
	    	file.write(rhel_rel)
	    	file.write(fstab)
            	file.write(df_mount)
            	file.write(waagent)
            	file.write(java)
def pre_patch_health_check():
    	health_check = HealthCheck("pre_patch_health_check_result.txt")
    	health_check.store_result()
    	print("Pre-patch health check report stored in pre_patch_health_check_result.txt")
def post_patch_health_check():
    	health_check = HealthCheck("post_patch_health_check_result.txt")
    	health_check.store_result()
    	print("Post-patch health check report stored in pre_patch_health_check_result.txt")
def compare_health_check_reports():
#       health_check = HealthCheck("pre_patch_health_check_result.txt")
#       health_check.compare_result("post_patch_health_check_result.txt")
        # read in contents of pre-check file
    with open('pre_patch_health_check_result.txt', 'r') as f:
        pre_check_contents = f.read()
# read in contents of post-check file
    with open('post_patch_health_check_result.txt', 'r') as f:
        post_check_contents = f.read()
# compare contents of pre-check and post-check files
    diff = difflib.unified_diff(pre_check_contents.splitlines(), post_check_contents.splitlines())
# check for lines starting with "+" indicating new lines added
    for line in diff:
	if line.startswith("+"):
		print("-------------------------------------ALERT:- difference found Post the Patching:--------------------------------------- \n")
		print("..........................................................................................................................")
		print(line)
def main_menu():
    print("\nMain Menu")
    print("1. Run pre-patch health check")
    print("2. Run post-patch health check")
    print("3. Compare health check reports")
    print("4. Quit")
    choice = int(input("Enter your choice (1-4): "))
    return choice

if __name__ == "__main__":
    while True:
        choice = main_menu()
        if choice == 1:
            pre_patch_health_check()
        elif choice == 2:
            post_patch_health_check()
        elif choice == 3:
            compare_health_check_reports()
        elif choice == 4:
            break


