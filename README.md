# doc-flask

To build container:

```bash
docker build . -t lighthouse-app:v0.0.1
```

To run container:

```bash
docker run
    -p 5000:5000 --mount src="${PWD}/tests/fixtures",target="/home/models",type=bind
    -t lighthouse-app:v0.0.1 models/test_model.pkl
```

0.0.0.0:5000 will show a success message if container is running.
