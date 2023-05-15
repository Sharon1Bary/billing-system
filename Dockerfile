FROM python:3.8

WORKDIR /fast-api-tasker

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./src ./src

CMD ["python", "./src/apps/Processor.py"]
CMD ["python", "./src/apps/BillingSystem.py"]
