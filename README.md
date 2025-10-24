# QR Code Generator (Dockerized)

This small project generates QR codes from a URL.

Building the Docker image:

    docker build -t qr-code-generator-app .

Running the container (default URL provided in Dockerfile):

    docker run --name qr-generator qr-code-generator-app

Override the URL:

    docker run --name qr-generator -v /host/path/to/qr_codes:/app/qr_codes \
      qr-code-generator-app --url http://www.njit.edu

Check logs:

    docker logs qr-generator

Stop & remove:

    docker stop qr-generator
    docker rm qr-generator

Push image to DockerHub:

    # login to DockerHub interactively
    docker login

    # tag the local image with your DockerHub username
    docker tag qr-code-generator-app your-dockerhub-username/qr-code-generator-app:latest

    # push the image
    docker push your-dockerhub-username/qr-code-generator-app:latest

Using GitHub Actions to publish automatically:

- Create repository secrets in GitHub: `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` (a personal access token or password).
- The workflow `.github/workflows/docker-publish.yml` will build and push the image on pushes to `main`.
