FROM python:3.9

WORKDIR /linx
COPY ./versioning/requirements.txt /linx/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /linx/requirements.txt
COPY ./ /linx/

ENTRYPOINT ["sh", "/linx/entrypoint.sh"]
