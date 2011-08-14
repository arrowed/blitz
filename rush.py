__author__="ghermeto"
__date__ ="$27/07/2011 23:23:30$"

from blitz.api import Curl, ValidationError
from blitz.validation import validate_url, validate_list, validate

class Point:
    """ Snapshot of a rush at time[i] containing information about hits, errors
        timeouts, etc. """
    
    def __init__(self, point):
        """ timestamp: The timestamp of this snapshot
            duration: The average response time at this time
            total: The total number of hits that were generated
            hits: The number of successful hits
            errors: The number of errors
            timeouts: The number of timeouts
            volume: The concurrency level at this time
            txbytes: The total number of bytes sent
            rxbytes: The total number of bytes received """
        
        self.timestamp = point['timestamp'] if 'timestamp' in point else None
        self.duration = point['duration'] if 'duration' in point else None
        self.total = point['total'] if 'total' in point else None
        self.hits = point['executed'] if 'executed' in point else None
        self.errors = point['errors'] if 'errors' in point else None
        self.timeouts = point['timeouts'] if 'timeouts' in point else None
        self.volume = point['volume'] if 'volume' in point else None
        self.txbytes = point['txbytes'] if 'txbytes' in point else None
        self.rxbytes = point['rxbytes'] if 'rxbytes' in point else None

class Result:
    """ Represents the results returned by the rush. Contains the entire 
        timeline of snapshot values from the rush as well as the region from 
        which the rush was executed. """
    
    def __init__(self, result):
        """ region: The region from which the rush was executed
            timeline: The timeline of the rush containing various statistics."""
        
        self.region = result['region'] if 'region' in result else None
        if 'timeline' in result and validate_list(result['timeline']):
            def point(p):
                return Point(p)
            self.timeline = list(map(point, result['timeline']))
        else:
            self.timeline = None

class Rush(Curl):
    """ Use this to run a rush (a load test) against your app. The return values
        include the entire timeline containing the average duration, the 
        concurrency, the bytes sent/received, etc."""
    
    def _validate(self, options):
        """ Raises a ValidationError if validation fails. """
        failed = validate(options)
        if not 'url' in options or not validate_url(options['url']):
            failed.append('url')
        
        if not 'pattern' in options or not 'intervals' in options['pattern'] \
        or not validate_list(options['pattern']['intervals']):
            failed.append('pattern')
        if len(failed) > 0:
            raise ValidationError('Validation error.', failed)
    
    def _format_result(self, result):
        """ Return the rush result object to be passed to the callback. """
        return Result(result)