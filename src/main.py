import os, shutil, pathlib

from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title

project_root = "/home/cheese/workspace/github.com/klaas-wie/static-site-generator"

# content_index = os.path.join(project_root, "content/index.md")
# public_index = os.path.join(project_root, "public/index.html")

content_path = os.path.join(project_root, "content")
template = os.path.join(project_root, "template.html")
public_path = os.path.join(project_root, "public")


def main():

    test = "main is running"

    print(test)

    copy_from_static_to_public(project_root)

    #generate_page(content_index, template, public_index)

    generate_pages_recursive(content_path, template, public_path)


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

def generate_page(from_path, template_path, dest_path):

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open (from_path) as f:
        md = f.read()

    with open(template_path) as f:
        template = f.read()

    html = markdown_to_html_node(md).to_html()

    title = extract_title(md)

    full_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    
    dir = os.path.dirname(dest_path)
    os.makedirs(dir, exist_ok=True)

    with open (dest_path, "w") as f:
        f.write(full_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):

    #check if destination exists, if not make the dir
    if os.path.exists(dest_dir_path) == False:
        os.mkdir(dest_dir_path)

    for item in os.listdir(dir_path_content):

        #convert item path to pathlib path for better usability
        item_path = pathlib.Path(os.path.join(dir_path_content, item))

        #check if item in dir is another dir, if it is, create new destination dirpath & call function again
        if os.path.isfile(item_path) == False:
            new_destination = os.path.join(dest_dir_path, item)
            
            generate_pages_recursive(item_path, template_path, new_destination)
        elif item_path.suffix == ".md":
            with open (item_path) as f:
                md = f.read()

            with open(template_path) as f:
                template = f.read()

            html = markdown_to_html_node(md).to_html()

            title = extract_title(md)

            full_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

            #change path to .html from .md
            item_stem = item_path.stem
            new_html_path = os.path.join(dest_dir_path, f"{item_stem}.html")

            with open (new_html_path, "w") as f:
                f.write(full_html)

if __name__ == "__main__":
    main()
    