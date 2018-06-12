docker kill `docker ps --format "{{.ID}}"`
docker rm `docker ps -a --format "{{.ID}}"`

