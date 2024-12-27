FROM ubuntu
RUN apt update && apt install curl -y
WORKDIR /app
COPY --chown=root:root --chmod=100 ./entrypoint.sh .
ENTRYPOINT [ "./entrypoint.sh" ]
CMD [ "XPTO" ]