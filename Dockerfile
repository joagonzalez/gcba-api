FROM python:3.10

COPY ./ /src/

WORKDIR /src/
RUN ls
# RUN mkdir logs
RUN pip install -r requirements.txt
# EXPOSE 8000
CMD ["python", "run.py"]