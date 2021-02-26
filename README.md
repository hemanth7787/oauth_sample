# oauth_sample authorization and resource servers
```
git clone <this repo>
cd <this repo>
python3 -m venv env
source env/bin/activate
pip install --upgrade pip && pip install -r req.txt
```

---

```
cd auth_server
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver 127.0.0.1:8000
```
---

```
cd resource_server_r1
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver 127.0.0.1:8001
```

goto http://localhost:8000/admin/oauth2_provider/application/add/
create application. You can put any name on it. client_type uses confidential . grant_type uses password. redirected_uri you can use anything.

user postman to get access token with "intospection" scope
save token in resoource server srrtings.py RESOURCE_SERVER_AUTH_TOKEN

generate a token from auth server
use the token to access protected resource at resource server