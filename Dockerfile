FROM python:3.12-alpine as builder

WORKDIR /appdir

COPY requirements.txt /appdir

RUN pip3 install --no-cache-dir -r /appdir/requirements.txt

COPY . /appdir

EXPOSE 5000

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]