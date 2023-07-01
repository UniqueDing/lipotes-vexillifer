FROM nginx

RUN apt-get update && apt-get install -y python3 cron python3-ebooklib python3-yaml

COPY dist/ /lipotes-vexillifer
COPY nginx/default.conf /etc/nginx/conf.d/default.conf
RUN usermod -G root nginx

COPY generator-cron /etc/cron.d/generator-cron
RUN chmod 0644 /etc/cron.d/generator-cron
RUN crontab /etc/cron.d/generator-cron

# ENTRYPOINT nginx -g "daemon off;" && cron -f
CMD cron && nginx -g "daemon off;"
