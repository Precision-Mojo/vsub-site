web: newrelic-admin run-program python manage.py run_gunicorn -c vsub_site/settings/gunicorn.py
scheduler: python manage.py celeryd -B -E --loglevel=INFO --maxtasksperchild=1000
worker: python manage.py celeryd -E --loglevel=INFO --maxtasksperchild=1000
