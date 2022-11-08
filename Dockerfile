FROM python:3.9
WORKDIR /patentabilidad-bespokem-project/
COPY "main.py" .
RUN python -m pip install pipenv
RUN pipenv install --dev --skip-lock
RUN pipenv install --dev
CMD ["python","-m","pipenv","run","python","main.py"]