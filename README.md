# Excel manager [![Build Status](https://travis-ci.org/GeorgiyII/excell_lib.svg?branch=development)](https://travis-ci.org/GeorgiyII/excell_lib)

Excel manager is a program that processes the specified excel page of a document with a table for calculating walls
that have a multilayer structure, and it is necessary to calculate the cost of materials by inserting columns into the table.

<div>
  <img src="https://github.com/GeorgiyII/excell_lib/raw/master/service_app/static/table.png" width="200" title="hover text">
  <img src="https://github.com/GeorgiyII/excell_lib/raw/master/service_app/static/right_arrow.png" width="40" alt="accessibility text">
  <img src="https://github.com/GeorgiyII/excell_lib/raw/master/service_app/static/new_table.png" width="220" alt="accessibility text">
</div>

All you need is to add the cipher materials to the main table of your Excel file, and the page with the table where
your ciphers will match the material name and price. See pictures below.

<div>
  <img src="https://github.com/GeorgiyII/excell_lib/raw/master/service_app/static/cypher.png" width="150" title="hover text">
  <img src="https://github.com/GeorgiyII/excell_lib/raw/master/service_app/static/model.png" width="150" alt="accessibility text">
</div>

<h2>Installing</h2>

Download or clone this repository:
```
$ git clone https://github.com/GeorgiyII/excell_lib.git
```

<h3>Python run</h3>

Need Python 3.7+ versions

Install requirements using pip:
```
$ cd excell_lib
$ virtualenv venv --no-site-packages
$ source venv/bin/activate
$ pip install -r requirements.txt
```
Run app:
```
$ python3 manage.py runserver
```

<h3>Docker run</h3>

Run app:
```
$ cd excell_lib
$ docker-compose up
```

<h2>Links</h2>
[Runing app on Heroku](https://excel-manager.herokuapp.com)
