"""The Covid-19 Spread Analysis Application
-----------------------------

About this Module
------------------
This module is the main entry point of The Covid-19 Spread Analysis Application.

"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-09"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

import sys

import folium
import pandas as pd
from flask import Flask, render_template


def find_top(data, group, cat, n=15):
    a_df = pd.read_csv(data)
    a_groupby = a_df.groupby(group).sum()[
        ['Confirmed', 'Deaths', 'Recovered', 'Active']
    ]
    results = a_groupby.nlargest(n, cat)[[cat]]
    return results


def circle_maker(x, a_map):
    folium.Circle(
        location=(x[0], x[1]), radius=float(x[2]) * 10, color="red",
        popup='confirmed cases:{}'.format(x[2], x[2])
    ).add_to(a_map)


if __name__ == '__main__':
    """Main entry point of sars2spread"""
    # Top 15 list
    if len(sys.argv) == 5:
        dataset = sys.argv[1]
        port = sys.argv[2]
        group = sys.argv[3]
        category = sys.argv[4]
    else:
        raise AttributeError(
            "Wrong number of arguments: {}".format(sys.argv)
        )

    cdf = find_top(data=dataset, group=group, cat=category)
    pairs = [
        (country, cat_nb)
        for country, cat_nb in zip(cdf.index, cdf[category])
    ]

    # Circle map
    corona_df = pd.read_csv(dataset)
    corona_df = corona_df[['Lat', 'Long_', category]]
    corona_df = corona_df.dropna()
    m = folium.Map(
        location=[45.505, -73.552],
        tiles='Stamen toner',
        zoom_start=8
    )
    corona_df[['Lat', 'Long_', category]].apply(
        lambda x: circle_maker(x, m), axis=1
    )
    m.save("templates/map.html")

    # Web server
    app = Flask(__name__)
    @app.route('/')
    def home():
        return render_template("home.html", cmap=m._repr_html_(), table=cdf,
                               pairs=pairs, group=group, category=category)
    app.run(debug=True, port=port)

    # Add unit tests
