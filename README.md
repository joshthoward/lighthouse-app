# doc-flask

To build container:

```bash
docker build . -t doc-flask:v1
```

To run container:

```bash
docker run -p 5000:5000 doc-flask:v1
```

0.0.0.0:5000 will show a success message if container is running.
