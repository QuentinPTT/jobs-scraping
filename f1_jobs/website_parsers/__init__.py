from .haas import get_jobs as haas_get_jobs
from .audi import get_jobs as audi_get_jobs
from .williams import get_jobs as williams_get_jobs
from .alpine import get_jobs as alpine_get_jobs
from .redbull import get_jobs as redbull_get_jobs


parsers = [
    {'name': 'Haas', 'get_jobs': haas_get_jobs},
    {'name': 'Audi', 'get_jobs': audi_get_jobs},
    {'name': 'Williams', 'get_jobs': williams_get_jobs},
    {'name': 'Alpine', 'get_jobs': alpine_get_jobs},
    {'name': 'Red Bull', 'get_jobs': redbull_get_jobs},
]
