FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./website/app /app

WORKDIR /

CMD ["gunicorn" "example:app" "-w 4" -k uvicorn.workers.UvicornWorker"]