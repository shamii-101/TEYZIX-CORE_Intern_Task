import os
import shutil
from datetime import datetime
import json

# making menu for backup

Source_Folder = r"H:\TEYZIXCORE\Task2\SourceFiles"
Backup_Folder = r"H:\TEYZIXCORE\Task2\Backups"
Restore_Folder =r"H:\TEYZIXCORE\Task2\RestoreFolder"
backup_log_file = r"H:\TEYZIXCORE\Task2\Backup.log"
json_file= r"H:\TEYZIXCORE\Task2\metadata.json"
choice = -1

while choice != 5:
    print("1. Create Backup")
    print("2. View Backup History")
    print("3. Restore Backup")
    print("4. View Logs")
    print("5. Exit")

    try:
     choice = int(input("Enter your choice: "))
    except ValueError:
      print("Please enter a valid number!")
      continue

    if choice == 1:
        Source_Folder = (r"H:\TEYZIXCORE\Task2\SourceFiles")
        Backup_Folder = (r"H:\TEYZIXCORE\Task2\Backups")
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_folder_name = f"Backups{current_time}"
        final_backup_path = os.path.join(Backup_Folder, backup_folder_name)
        if os.path.exists(Source_Folder):
             shutil.copytree(Source_Folder, final_backup_path) 
             with open(backup_log_file,"a") as log:
               log.write(f"{current_time} -Backup created: {backup_folder_name}\n")

             metadata ={
                    "backup_id": backup_folder_name,
                     "backup_date" : current_time, 
                    "Source" : Source_Folder,
                     "destination" :final_backup_path,
                    "status" :"Success"
            }
             with open(json_file ,"r") as file:
              data = json.load(file)
              data.append(metadata)
    
             with open(json_file,"w") as file:
              json.dump(data,file , indent=5)
        
             print("Backup created Sucessfully!")
        else:
         print("not created")
        
            
    elif choice == 2:
        backups=os.listdir(Backup_Folder)
        for backup in backups:
            print(backup)
    

     
    elif choice == 3:
        backups = os.listdir(Backup_Folder)
        for i,backup in enumerate(backups, start=1):
            print(f"{i}. {backup}")
        input_backup = int(input("Enter the backup folder name to restore: "))
        selected_backup=backups[input_backup-1]
        backup_path = os.path.join(Backup_Folder, selected_backup)
        print(selected_backup)
        print(backup_path)
        print(os.path.join(Restore_Folder, selected_backup))
        shutil.copytree(backup_path, os.path.join(Restore_Folder, selected_backup))
        with open(backup_log_file, "a") as log:
         log.write(f"{current_time} - Backup Restored: {selected_backup}\n")
        
    elif choice == 4:
         with open(backup_log_file, "r") as log:
           content = log.read()
         print("===== LOG HISTORY =====")
         print(content)
    elif choice == 5:
     print("Exit")
     
    else:
        print("Invalid Input")


    
       
    
   
  
         


    
   


          

          


                  

     
    
     
       

   

        
    
    
