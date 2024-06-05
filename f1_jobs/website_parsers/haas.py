import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'fr-FR,fr;q=0.7',
    'priority': 'u=1, i',
    'referer': 'https://haasf1team.bamboohr.com/careers',
    'sec-ch-ua': '"Brave";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}

def get_jobs():
    response = requests.get('https://haasf1team.bamboohr.com/careers/list', headers=headers)
    return parse_jobs(response.json())

def parse_jobs(data):
    jobs = data["result"]
    job_list = []
    for job in jobs:
        job_info = {
            "job_id": job["id"],
            "job_name": job["jobOpeningName"],
            "department": job["departmentLabel"],
            "employment_status": job["employmentStatusLabel"],
            "location_city": job["location"]["city"],
            "location_state": job["location"]["state"],
        }
        job_list.append(job_info)
    return job_list
