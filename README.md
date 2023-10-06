# My First Wagtail Site

Welcome to "My First Wagtail Site," a simple Wagtail-powered website that I created by following the tutorial [Your first Wagtail site](https://docs.wagtail.org/en/stable/getting_started/tutorial.html). This README will guide you through the prerequisites, provide an overview of the affected parts of the code, and explain how to run the site locally.

## Prerequisites

Before you can run this Wagtail site locally, make sure you have the following prerequisites installed:

- **Python**: This project is built using Python, so you'll need to have `Python 3.x` installed on your system. You can download it from the official [Python website](https://www.python.org/downloads/).
- **Virtual Environment (Optional, but recommended)**: It's a good practice to create a virtual environment for Python projects. You can use `virtualenv` or `venv` to create one. Install `virtualenv` using `pip`:
```
pip install virtualenv
```
- **Git (Optional)**: If you plan to clone this project from a Git repository, you'll need Git installed on your system. You can download it from [Git's official website](https://git-scm.com/downloads).

## Affected Parts of the Code

Here's a summary of the important parts of the code that you'll find in this project:

|File/Folder |	Description|
|:--|:--|
|codewithmideWagtailSite/ |This folder contains the core Django and Wagtail project settings.|
|home/ |This is the Django app for the main homepage and its templates.|
|blog/	|This app handles the blog section of the website.|
|requirements.txt	|Lists all the Python packages required for this project.|

## How to Run It Locally

Follow these steps to run "My First Wagtail Site" on your local machine:

1. **Clone the Repository (If Not Already Done)**: If you haven't already cloned this project's Git repository, you can do so with the following command:

```bash
git clone https://github.com/codewithmide/WagtailSite
```
2. **Navigate to the Project Folder:**
```bash
cd myfirstwagtailsite
```
3. **Create a Virtual Environment (Optional)**: It's recommended to create a virtual environment for this project. If you choose to create one, use the following commands:
```bash
python -m venv mysite/env
# Then:
source mysite/env/bin/activate
```
On Windows, use:
```bash
py -m venv mysite\env

# then

mysite\env\Scripts\activate.bat

# If mysite\env\Scripts\activate.bat doesn't work, run:

mysite\env\Scripts\activate
```
4. **Install Dependencies**:
```bash
pip install -r requirements.txt
```
5. **Apply Migrations**:
```bash
python manage.py migrate
```
6. **Create a Superuser**: This prompts you to create a new admin user account with full permissions. It’s important to note that for security reasons, the password text won’t be visible while typing.
```bash
python manage.py createsuperuser
```
7. **Run the Development Server**:
```bash
python manage.py runserver
```
The development server will start, and you can access the site at `http://localhost:8000/`.
8. **Access the Wagtail Admin Interface**: To access the Wagtail admin interface and start managing your site's content, go to `http://localhost:8000/admin/` and log in with the superuser credentials you created earlier.

That's it! You now have "My First Wagtail Site" up and running on your local machine. Feel free to explore the code, customize the templates, and add your own content to make it your own.

Enjoy building with [Wagtail](https://wagtail.org/)!

