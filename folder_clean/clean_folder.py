def clean(folder_path, exclude_list):
    dirs = os.listdir( folder_path )
    for item in dirs:
        print(item)
