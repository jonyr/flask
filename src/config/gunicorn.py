# pylint: disable=C0103
bind = '0.0.0.0:5000'
workers = 1
errorlog = '-'
loglevel = 'warning'
accesslog = '-'
access_log_format = (
    '%({X-Forwarded-For}i)s %(t)s %(M)s %(b)s "%(r)s" %(s)s "%(f)s" "%(a)s"'
)
