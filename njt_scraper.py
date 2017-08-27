from bs4 import BeautifulSoup
import requests
import re
import unicodedata

SELECTED_ROUTE        = 'Selected Route:'
SELECTED_DIRECTION    = 'Selected Direction:'
SELECTED_STOP         = 'Selected Stop:'
SELECTED_STOP_NUMBER  = 'Selected Stop #:'
ROUTE_DETAILS_COUNT   = 4
ROUTE_OPTIONS_REGEX   = r'#\d+.*Vehicle \d+\)'
ROUTE_DETAILS_REGEX   = r'[^a-zA-Z0-9-_*.\s\(\)#]'
TO_EXTRACT_ITEMS = (SELECTED_ROUTE, SELECTED_DIRECTION, SELECTED_STOP, SELECTED_STOP_NUMBER)

CLEANUP_NL_SPACES = lambda text : [unicodedata.normalize('NFKD', line.strip()).encode('ascii', 'ignore') for line in text.split('\n') if line.strip()]
CLEANUP_SPL_CHARS = lambda text: re.sub(ROUTE_DETAILS_REGEX, '', text).strip()

def getURLText(url):
  ''' Gets the text(only) version of the browser view of URL'''
  return CLEANUP_NL_SPACES(BeautifulSoup(requests.get(url).text).text)

def getRouteDetails(lines):
  ''' given the lines of the text only view, returns the route details'''
  details = {}
  for item in TO_EXTRACT_ITEMS:
    for line in lines:
      if not item in line:
        continue
      line = re.sub(item, '', line)
      details[CLEANUP_SPL_CHARS(item)] = CLEANUP_SPL_CHARS(line)
      continue
  return details 

def getRouteOptions(lines):
  ''' given the lines of the text only view, returns the route options
      i.e. different bus route available at that time based on the input
  '''
  routeOptions = re.findall(ROUTE_OPTIONS_REGEX, '\n'.join(lines), re.DOTALL)
  if routeOptions:
    routeOptions = [ro for ro in routeOptions[0].split('\n') if ro.strip()]
    routeOptions = list(chunks(routeOptions, ROUTE_DETAILS_COUNT))
  return routeOptions

def chunks(l, n):
    '''Yield successive n-sized chunks from l.'''
    for i in range(0, len(l), n):
        yield l[i:i + n]

if __name__=='__main__':
  pass