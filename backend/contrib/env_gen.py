"""
Python SECRET_KEY generator
"""
import random

chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!?@#$%^&*()"
size = 50
secret_key = "".join(random.sample(chars, size))

chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!?@#$%_"
size = 20
password = "".join(random.sample(chars, size))

CONFIG_STRING = """
DEBUG=True
SECRET_KEY=%s
ALLOWED_HOSTS='127.0.0.1,localhost,0.0.0.0'
MAIN_SERVER=False

#DATABASE_ENGINE=django.db.backends.postgresql_psycopg2
#DATABASE_NAME=DBName
#DATABASE_USER=UserName
#DATABASE_PASS=%s
#DATABASE_HOST=localhost
#DATABASE_PORT=5432

#DEFAULT_FROM_EMAIL=
#EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
#EMAIL_HOST=localhost
#EMAIL_PORT=
#EMAIL_HOST_USER=
#EMAIL_HOST_PASSWORD=
#EMAIL_USE_TLS=True
""".strip() % (secret_key, password)

# Writing our configuration file to '.env'
with open('.env', 'w') as configfile:
    configfile.write(CONFIG_STRING)

print('Success!')
print('Type: cat .env')