FROM public.ecr.aws/lambda/python:3.8 as build

COPY ./pyproject.toml .
COPY triggersqs/ triggersqs/

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install

COPY entrypoints/lambda_handler.py lambda_handler.py

CMD ["lambda_handler.lambda_handler"]

