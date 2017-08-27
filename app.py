from flask import Flask, render_template
import njt_scraper
import tabulate

app = Flask(__name__)

TO_N_ARLINGTON = [
  'http://mybusnow.njtransit.com/bustime/wireless/html/eta.jsp?route=40&direction=Kearny&id=30969&showAllBusses=on',
  'http://mybusnow.njtransit.com/bustime/wireless/html/eta.jsp?route=30&direction=North+Arlington&id=20475&showAllBusses=on',
  'http://mybusnow.njtransit.com/bustime/wireless/html/eta.jsp?route=76&direction=Hackensack&id=18835&showAllBusses=on',
]

TO_N_YORK = [
  'http://mybusnow.njtransit.com/bustime/wireless/html/eta.jsp?route=76&direction=Newark&id=12827&showAllBusses=on',
  'http://mybusnow.njtransit.com/bustime/wireless/html/eta.jsp?route=40&direction=Jersey+Gardens&id=12811&showAllBusses=on'
]

DIRECTIONS = {
  'To N Arlington'  : TO_N_ARLINGTON,
  'To New York'     : TO_N_YORK
}

@app.route('/')
@app.route('/index')
def index():
  return render_template('sample.html', results=getLatestScheduleData())

def getLatestScheduleData():
  results = {}
  for direction, directionURLs in DIRECTIONS.iteritems():
    for directionURL in directionURLs:
      urlDetails = njt_scraper.getURLText(directionURL)
      if urlDetails:
        routeDetails = njt_scraper.getRouteDetails(urlDetails)
        routeOptions = njt_scraper.getRouteOptions(urlDetails)
        routeHeader  = "{0} towards {1} from {2}".format(routeDetails['Selected Route'], routeDetails['Selected Direction'], routeDetails['Selected Stop'])
        routeOptions = tabulate.tabulate(routeOptions) if routeOptions else 'No Route Options At This Time'

        if not direction in results:
          results[direction] = []
        results[direction].append((routeHeader, directionURL, routeOptions))
  return results

if __name__ == '__main__':
  app.run(debug=True)