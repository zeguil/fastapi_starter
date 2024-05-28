import os
import shutil

def create_app(app_name):
    current_dir = os.path.dirname(__file__)
    template_dir = os.path.join(current_dir, '..', 'templates', 'app_template')
    app_dir = os.path.join(os.getcwd(), app_name)

    if os.path.exists(app_dir):
        print(f"Error: Directory '{app_dir}' already exists.")
        return

    shutil.copytree(template_dir, app_dir)
    print(f"App '{app_name}' created successfully at {app_dir}.")
