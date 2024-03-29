CREATE DATABASE django_toy;
CREATE USER new_user WITH LOGIN PASSWORD 'hello';
GRANT ALL PRIVILEGES ON DATABASE django_toy TO new_user;
ALTER USER new_user WITH SUPERUSER;