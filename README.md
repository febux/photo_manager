# photo_manager
test_task

---
### login: febux
### password: 1234

---
# API POST:

```
/api/photos/create/ - add new photo with params (login required)
```
{user_created: <int:id>, location: <str:str>, description: <str:str>, people_on_photo: <str:str>}


example: {user_created: 1, location: '41.24, 2,72', description: 'description', people_on_photo: 'Miha, Maiha'}

---
# API GET:

```
/api/photos/ - get list of photos through serializer
```

```
/api/photos/<int:pk> - get one photo through serializer
```

---
# API GET filterset:

date_created - exact,
location - icontains,
people_on_photo - icontains

```
/api/photos/?people_on_photo=&location=&date_created=
```

---

## Global relations: 
- Ubuntu `22.04`
- python `3.10.6`
- pipenv