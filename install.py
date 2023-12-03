import os

def install_requirements_in_folders(directory_path):
    folders_with_requirements = []
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isdir(item_path):
            os.chdir(item_path)
            if os.path.exists('requirements.txt'):
                # The actual command to run is commented out as we cannot run it in this environment.
                os.system('pip install -r requirements.txt')
                print(f"Running 'pip install -r requirements.txt' in {item_path}")
                folders_with_requirements.append(item_path)
            os.chdir(directory_path)
    return folders_with_requirements

# Replace 'your_directory_path' with the actual directory path.
os.system('apt-get update -y')
os.system('apt-get install build-essential -y')
os.system('apt-get install ffmpeg -y')
folders_installed = install_requirements_in_folders('/workspace/ComfyUI/custom_nodes')
