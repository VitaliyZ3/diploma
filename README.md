# Accounting system "Новатор-Агро"
### Data schema
&ensp;
![](/images/product_accounting0.0.1.png "Диаграма классов")

# How to install

Create virtual environment python, use this command

```
python -m venv venv
```
Activate venv
```
.\venv\Scripts\activate
```
Next install pip packages from requirements.txt
```
pip install -r requirements.txt
```
And now go to directory with manage.py file
```
cd .\staff_accounting\

dir
d-----        07.02.2022     14:07                accounting
d-----        31.01.2022     20:07                staff_accounting
-a----        07.02.2022     14:41         159744 db.sqlite3
-a----        31.01.2022     20:04            694 manage.py <--- this file
```
It remains to write a command below to start the server and go to the address http://127.0.0.1:8000/
```
python manage.py runserver
```
