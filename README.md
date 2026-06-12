# Django / Svelte - Playground

use this link: \
<http://127.0.0.1:8000/api/tables/3708/rows> \
to test the most bassic api call.

## Helpful Links

### Backend

- [My Django-Svelte setup for fullstack development](https://dev.to/besil/my-django-svelte-setup-for-fullstack-development-3an8)
- [Django setup guide](https://www.w3schools.com/django/django_create_project.php)

### Frontend

- [SvelteKit Tutorial](https://svelte.dev/tutorial/kit/introducing-sveltekit)

## Setup

### Secrets

Create a toplevel `.env` file with the following secrets:

- `TABLES_URL=https://cloud.ovgu.de/apps/tables/`
- `TABLES_USERNAME=<user_name>`
- `TABLES_PASSWORD=>user_password>`

> [!note] How to get username / password \
> You cant youse your personal login information, instead you need to:
>
> 1. go to the nextcloud and log in
> 2. navigate to your setting _(click on your profile)_
> 3. navigate to the security tab _(on the left)_
> 4. at the bottom choose a fitting app-name and create a new **app-password**

### Excecution

1. Install requirements
2. excecute backend with `python.exe .\backend\manage.py runserver`
3. serve frontent with `???`
