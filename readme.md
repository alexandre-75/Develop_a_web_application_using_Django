<p align="center">
  <img src="picture\16004297044411_P7.png" alt="logo" />
</p>

## The Project

- Use the **Django** framework.
- Using server-side rendering in **Django**.
- Developing a web application using Django with **MVT structure** (Model-View-Template).
- The app is an **MVP** (Produit Viable Minimum).


## Context

- it is a social network for sharing around literature.
- Each user can follow other users of their choice and be followed by any user.
- The application allows to request or publish literature reviews.

The app has two main use cases:
- People **requesting reviews** on a particular book or article.
- People **looking for** interesting articles and books to read, based on the reviews of others.

## Database

- This repository comes with a pre-populated SQLite database of some user accounts.
- we have used SQLite for this project.


##  Project download

_Tested on Windows 10, Python 3.10.6. and Django 4.1.7_

[Technical Specifications ( english )](https://github.com/alexandre-75/Develop_a_web_application_using_Django/blob/main/picture/technical_specifications/technical_specifications-english.pdf)

[Technical Specifications ( french )](https://github.com/alexandre-75/Develop_a_web_application_using_Django/blob/main/picture/technical_specifications/technical_specifications-french.pdf)

[Database schema](https://s3-eu-west-1.amazonaws.com/course.oc-static.com/projects/Python+EN/Python+782+Develop+a+Web+Application+Using+Django/LITReview+-+Schema.pdf)

[Wireframes](https://s3-eu-west-1.amazonaws.com/course.oc-static.com/projects/Python%20FR/P7%20-%20D%C3%A9veloppez%20une%20application%20Web%20en%20utilisant%20Django/LITReview%20-%20Wireframes%20-%20FR.pdf)

####  1. project recovery

    $ git clone https://github.com/alexandre-75/Develop_a_web_application_using_Django.git

####  2. Creating a virtual environment

    python<version> -m venv nom_env_virtuel

    Activate the environment  `mon_env_virtuel\Scripts\activate` (Windows)

####  3. Installing packages

    pip<version> install -r requirements.txt
    
####  4. Start the program

- From the project root folder, go with the terminal to the ***source*** folder :
    ```sh
     cd source/
     ```
- ***Run the server*** by executing the command :
  ```sh
  python manage.py runserver
  ```

- Open your favorite browser and navigate to the ***local development server*** at :
  ```sh
  http://127.0.0.1:8000/
  ```

#### 5. Create an account directly with the application or use the account below 
   ```sh
   Username: username
   Password: a
   ```


## Use of the program


    
## Generate a flake8 report
    
flake8 can identify syntax errors and non-compliance with the PEP.

#### 1. To view a flake8-html report :

From the project root folder, go with the terminal to the ***_*** folder :

   

open file <html> to view the report
 
#### 2. A new report can be generated by running the following command in the terminal :

     $ flake8 --format=html --htmldir=flake8_rapport project_link/