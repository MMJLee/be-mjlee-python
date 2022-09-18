# be-mjlee-python (Backend for mjlee.dev Python version)

Hi, this is a Python version of the [backend](https://github.com/mmjlee/be-mjlee) for [my website](https://mjlee.dev)

This has the same functionality, but it has only been tested locally.

I used a local docker image for my postgres database. To run:

docker run --name docker-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres
docker start docker-postgres
.\env\Scripts\activate
cd src
uvicorn main:app --reload
