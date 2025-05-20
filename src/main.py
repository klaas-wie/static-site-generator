import os, shutil, pathlib, sys

from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title

project_root = "/home/cheese/workspace/github.com/klaas-wie/static-site-generator"

content_path = os.path.join(project_root, "content")
template = os.path.join(project_root, "template.html")
public_path = os.path.join(project_root, "public")

docs_dir = "/home/cheese/workspace/github.com/klaas-wie/static-site-generator/docs"


def main():

    test = "main is running"

    print(test)

    try:
        basepath = sys.argv[1]
    except IndexError:
        basepath = "/"

    copy_from_static_to_public(project_root)

    generate_pages_recursive(content_path, template, docs_dir, basepath)


def copy_from_static_to_public(path):

    public_path = path+"/public"
    static_path = path+"/static"

    if os.path.exists(public_path):
        #delete /public and its contents recursively
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
            
            copy_recursively(item_path, new_destination)
        else:
            shutil.copy(item_path, destination_dir_path)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):

    #check if destination exists, if not make the dir
    if os.path.exists(dest_dir_path) == False:
        os.mkdir(dest_dir_path)

    for item in os.listdir(dir_path_content):

        #convert item path to pathlib path for better usability
        item_path = pathlib.Path(os.path.join(dir_path_content, item))

        #check if item in dir is another dir, if it is, create new destination dirpath & call function again
        if os.path.isfile(item_path) == False:
            new_destination = os.path.join(dest_dir_path, item)
            
            generate_pages_recursive(item_path, template_path, new_destination, basepath)
        elif item_path.suffix == ".md":
            with open (item_path) as f:
                md = f.read()

            with open(template_path) as f:
                template = f.read()

            html = markdown_to_html_node(md).to_html()

            title = extract_title(md)

            full_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
            full_html = full_html.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}') 

            #change path to .html from .md
            item_stem = item_path.stem
            new_html_path = os.path.join(dest_dir_path, f"{item_stem}.html")

            with open (new_html_path, "w") as f:
                f.write(full_html)

if __name__ == "__main__":
    main()
    