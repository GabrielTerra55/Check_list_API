FROM python:3

WORKDIR /Check_list_API/ ..

RUN pip install --upgrade pip

COPY requirements.txt /Check_list_API/

RUN pip install --no-cache-dir -r /Check_list_API/requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "main.py"]
