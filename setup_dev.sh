#!bin/sh

# docker-compose -f docker-compose.dev.yml build
docker-compose -f docker-compose.dev.yml up -d 
docker exec -it django /bin/sh -c "python manage.py makemigrations && 
python manage.py migrate"
docker-compose -f docker-compose.dev.yml down
docker-compose -f docker-compose.dev.yml up