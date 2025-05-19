import os, shutil

project_root = "/home/cheese/workspace/github.com/klaas-wie/static-site-generator"


def main():

    test = "main is running"

    print(test)

    copy_from_static_to_public(project_root)


def copy_from_static_to_public(path):

    public_path = path+"/public"
    static_path = path+"/static"

    if os.path.exists(public_path):
        #delete /public and its contents recursively
        #print(f"deleting {public_path}")
        shutil.rmtree(public_path)
        
    copy_recursively(static_path, public_path)

def copy_recursively(dir_path, destination_dir_path):

    #check if destination exists, if not make the dir
    if os.path.exists(destination_dir_path) == False:
        os.mkdir(destination_dir_path)

    for item in os.listdir(dir_path):

        item_path = os.path.join(dir_path, item)

        #check if item in dir is another dir, if it is, create new destination dirpath & call function again
        if os.path.isfile(item_path) == False:
            new_destination = os.path.join(destination_dir_path, item)
            
            #print(f"calling copy_recursively with item_path = {item_path} and destination = {new_destination}")
            copy_recursively(item_path, new_destination)
        else:
            #print(f"copying {item_path}")
            shutil.copy(item_path, destination_dir_path)

if __name__ == "__main__":
    main()
    