FROM rasa/rasa:2.5.0-full
COPY . /app
WORKDIR /app
USER root
RUN rasa train
ENTRYPOINT ["rasa", "run", "-p", "8080", "--cors", "*"]
