web: gunicorn 'newsscrapper.wsgi'
worker: celery -A newsscraper worker -loglevel info 
beat: celery -A newsscraper beat -loglevel error