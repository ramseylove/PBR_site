## My Resume - Portfolio site built in Django
It currently can only have a single resume but future plans to allow for multiple different resumes seperated by sub-domains
- Core was built with my django template

### Sections
- About
- Work experience
- Education
- Skills
- Portfolio
- Contact

### Tech
- Docker-Compose - used for development environment
- Dockerfile - optimized with slim-buster image
- DB in Postgres 11
- Emails sent via sendgrid
- Static and media files hosted with s3 compatible storage
- Makefile - rules written to make development in docker easier
- Github Action setup to push to linode
- Hosted on Dokku via Linode

### Deploy to Dokku with github action
*Requirements* 
- define SSH_PRIVATE_KEY in github secrets
- setup new app on dokku and create new ssh key for deployment

### To get started with development define dev.env in /envs folder
SECRET_KEY= \
ENVIRONMENT=docker_development \
DEBUG= \
ALLOWED_HOSTS=127.0.0.1,localhost,0.0.0.0 \
USE_S3=False \
SEND_GRID_KEY= \
DB_USER=postgres \
DB_PORT=5432 \
DB_HOST=db 
