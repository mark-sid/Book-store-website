# Book store website project
### A simple django online store website
# Installation
```
git clone https://github.com/mark-sid/Book-store-website.git
```
```
python -m venv venv
```
```
venv\Scripts\activate.bat # Windows
```
```
venv\Scripts\activate # Mac or Linux
```
```
pip install -r requirements.txt
```
# Launch
```
cd  Bookstore
```
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
docker run -d -p 6379:6379 redis
``` 
```
python manage.py runserver

```
# Technologies used
- Django
- Redis
- Html Css
