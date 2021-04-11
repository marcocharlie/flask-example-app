FROM python:3.6

EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY api.py config.py database.py node_finder.py request.py response.py /app/

CMD python api.py
