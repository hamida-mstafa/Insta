# Insta
  Insta is a website dedicated to sharing photography entirely designed with Instagram simulation.


## Author

* **Hamida Mstafa**

## Features


As a user of the application you will be able to:



1. Sign in to the application to start using.
2. Upload my pictures to the application.
3. View different photos that interest you.
4. See my profile with all my pictures.

### Installing

*** To view the app.Visit -> [insta](http://instamids.herokuapp.com/)

1. Clone this repo: git clone https://github.com/hamida-mstafa/insta.git.
2. The repo comes in a zipped or compressed format. Extract to your prefered location and open it.
3. open your terminal and navigate to gallery then create a virtual environment.For detailed guide refer  [here](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
3. To run the app, you'll have to run the following commands in your terminal


       pip install -r requirements.txt
4. On your terminal,Create database  using the command below.


       CREATE DATABASE insta;
       **if you opt to use your own database name, replace insta your preferred name, then also update settings.py variable DATABASES > NAME**

5. Migrate the database using the command below


       python3.6 manage.py migrate
6. Then serve the app, so that the app will be available on localhost:8000, to do this run the command below


       python manage.py runserver
7. Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.

## Running the tests

Use the command given below to run automated tests.


        python manage.py test insta
        python manage.py test user




## Built With

* [Django](https://www.djangoproject.com/) - web framework used
* Javascript - For DOM(Document Object Manipulation) scripts
* HTML - For building Mark Up pages/User Interface
* CSS - For Styling User Interface


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
