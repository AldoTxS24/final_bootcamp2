# Proyecto Aldo Texis - Cine
 Despliegue a Prod - proyecto bootcamp

1. Crea un ambiente virtual:
```
python3 -m venv env
```
2. Activa el ambiente virtual:
```
# Activación en Unix
source env/bin/activate
```
```
# Activación en Windows
env\Scripts\activate
```

3. Instala las dependencias del archivo requirements.txt

```
pip install -r requirements.txt
```

4. Instala las dependencias del archivo requirements.txt

```
Si se va a ejecutar localmente, hay que crear el rchivo my.cnf con la database conrrepsondiente (cinema)
```


5. Genera las migraciones y ejeculatas:
```
python manage.py makemigrations
python manage.py migrate
```
6. Crea un super usuario:
```
python manage.py createsuperuser
```
7. Corre la aplicación:
```
python manage.py runserver
```

8. Para lanzar abrir el endpoint para dar de alta un usuario hay que abrir el link:
```
http://143.244.180.12:8000/usuarios/signup
```