# Exposing User Activites Using Django REST API

- This project is an attempt to expose the user activity related information through REST API


## Dependencies

1. Django Rest Framework
2. uuid
3. Random

## Custom Management Command

Use the below sequence of commands to delete the db and  populate it with dummy data 

```
python manage.py flush
python manage.py create_users count
python manage.py create_activites count
```


