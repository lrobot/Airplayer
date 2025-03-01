FROM lrobot/py2airplay_debian
#pushname lrobot/airplayer_pascalw
RUN pip install tornado==1.2.1
RUN pip install simplejson==2.1.3
RUN apt-get install -y vim
ENV PATH=/venv/bin:$PATH
CMD ["bash", "-c", "source /boot.inc && (cd /app/airplayer/ && python airplayer.py ) "]

