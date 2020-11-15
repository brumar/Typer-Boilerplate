docker build . -t mycli
clear
docker run -it --entrypoint sh mycli -c "cd /app && pytest $@"
