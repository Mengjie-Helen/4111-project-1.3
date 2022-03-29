import os
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response

DATABASEURI = "postgresql://mz2840:20224111ab@35.211.155.104/proj1part2"
engine = create_engine(DATABASEURI)

engine.connect()


cursor = engine.execute("select * from customer;")
names = []
for result in cursor:
    names.append(result['name'])  # can also be accessed using result[0]
cursor.close()
names

engine.connect().close()