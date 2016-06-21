#!/usr/bin/env python3
import psycopg2
import psycopg2.extras
from functools import partial
from subprocess import check_output
from configparser import ConfigParser


def main():
    # parse application configurations
    cfg_parser = ConfigParser()
    cfg_parser.read('../config.ini')
    conf = dict(cfg_parser.items('db'))

    # get IP address of the database container
    host = check_output("docker ps | grep %s | awk '{print $NF;}' | \
                        xargs docker inspect --format \
                        '{{ .NetworkSettings.IPAddress }}'" % conf['host'],
                        shell=True).decode('utf-8').strip("\n")

    try:
        db = None
        db = psycopg2.connect(
            "dbname='{}' user='{}' host='{}' password='{}'".format(
                conf['name'], conf['user'], host, conf['pass']))

        cursor = db.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)

        cursor.execute("SELECT value FROM settings WHERE key='languages'")
        languages = cursor.fetchone().value

        languages = {v: k for k, v in languages.items() if len(v) != 0}

        # partial replace langs
        prl = partial(replace_langs, cursor, languages)

        prl('accounts', ['data'])
        prl('actions', ['title'])
        prl('address_book', ['name', 'descr', 'address'])
        prl('calendar', ['comment'])
        prl('groups', ['title'])
        prl('libraries', ['title', 'fields'])
        prl('roles', ['title', 'division'])
        prl('sequences', ['descr'])
        prl('service_users', ['descr'])
        prl('settings', ['value'])
        prl('snippets', ['descr'])
        prl('statuses', ['title'])
        prl('tabs', ['title'])
        prl('task_states', ['new_data'])
        prl('tasks', ['data'])
        prl('templates', ['descr', 'body'])
        prl('workflows', ['title', 'descr'])

        cursor.execute("SELECT * FROM libraries")
        libs = cursor.fetchall()
        for lib in libs:
            fields = [f['name'] for k, f in lib.fields.items()
                      if f['type'] == 'jsonb']

            if len(fields) > 0:
                prl(lib.name, fields)

        db.commit()
        cursor.close()

    except Exception as e:
        if db is not None:
            db.rollback()
        print("Database Error [{}]".format(str(e)))
    finally:
        if db is not None:
            db.close()


def replace_langs(cur, languages, table, fields):
    rpl = '{0}=replace({0}::text, \'"{1}":\', \'"{2}":\')::jsonb'

    for k, v in languages.items():
        rpls = [rpl.format(f, k, v) for f in fields]

        cur.execute("UPDATE {0} SET {1}".format(table, ",".join(rpls)))


if __name__ == '__main__':
    main()
