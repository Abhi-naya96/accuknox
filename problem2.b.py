import subprocess
import datetime

def backup(source_path, destination_path):
    try:
        # Generate timestamp for the backup file
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        # Execute rsync command to sync the directory to the destination
        rsync_command = f"rsync -avz --progress {source_path} {destination_path}/backup_{timestamp}"
        subprocess.run(rsync_command, shell=True, check=True)

        print("Backup successful.")
    except subprocess.CalledProcessError as e:
        print(f"Backup failed: {e}")
        return False
    return True

if __name__ == "__main__":
    # Specify the directory to be backed up and the destination
    source_path = "/var/log"
    destination_path = "/root"

    # Perform the backup operation
    success = backup(source_path, destination_path)

    # Print the result
    if success:
        print("Backup operation successfully completed.")
    else:
        print("Backup operation failed.")

