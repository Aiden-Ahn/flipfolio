FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/Aiden-Ahn/flipfolio.git

WORKDIR /home/flipfolio/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-a+8!pinn*(=toyep3p5ncm0k74(kxq6#c5*6_f(1(oatj&@mp=" > .env

RUN python manage.py migrate

EXPOSE 8000
 
CMD ["python","manage.py","runserver","0.0.0.0:8000"]