import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/api/v1.0/precipitation")
def welcome():
   session = Session(engine)
   results = session.query(Measurement.date, Measurement.prcp) \
   .filter(Measurement.date >"2015-01-01").order_by(Measurement.date).all()

   almost_json = [{'date':date, 'prcp':prcp} for date, prcp in results]
   import json
   return json.dumps(almost_json)
 #get dates and temp , return json 
if __name__ == '__main__':
    app.run(debug=True)

