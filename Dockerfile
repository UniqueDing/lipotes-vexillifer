FROM nginx
COPY dist/ /lipotes-vexillifer
COPY nginx/default.conf /etc/nginx/conf.d/default.conf

