FROM python:3.7.5-stretch

WORKDIR /root/slackapi
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# タイムゾーンとロケールの設定
RUN ln -sf  /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
  && apt update -y \
  && apt install -y locales \
  && locale-gen ja_JP.UTF-8 \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8  
ENV LANGUAGE ja_JP:en  
ENV LC_ALL ja_JP.UTF-8