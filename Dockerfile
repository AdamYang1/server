FROM registry.cn-beijing.aliyuncs.com/hub-mirrors/python:3

COPY . .
RUN pip3 install -r requirements.txt -t ./
CMD [ "python3", "app.py" ]