# django-ci

# jenkins-docker
```
docker run -p 8080:8080 -p 50000:50000 -v /var/jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock --name jenkins -d ebzdag/docker-jenkins
```

```
docker-compose run app sh -c "django-admin.py startproject app ."
docker-compose run app sh -c "python manage.py test && flake8"
docker-compose run app sh -c "python manage.py startapp core"
docker-compose run app sh -c "python manage.py makemigrations core"
```