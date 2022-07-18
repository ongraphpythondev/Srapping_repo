from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from django.views import View
# Create your views here.


class ScrapJobs(View):
    def get(self, request):
        keyword = request.GET.get("search")
        if keyword is None:
            return render(request, 'Scrap_jobs_times.html', {'data': [], 'search': ""})

        url_ = f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={keyword}&txtLocation='

        html_text = requests.get(url_).text
        soup = BeautifulSoup(html_text, 'lxml')
        jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
        data = []

        for job in jobs:

            posted_date = job.find('span', class_='sim-posted')
            company_name = job.find('h3', class_='joblist-comp-name')
            skills = job.find('span', class_='srp-skills')

            more_info = job.find('ul', class_='list-job-dtl clearfix').li.a['href']
            response_text = requests.get(more_info).text
            soup_ = BeautifulSoup(response_text, 'lxml')
            description = \
                str(soup_.find('div', class_='jd-desc job-description-main').text).strip().replace(
                    "Job Description", '')

            temp = {}
            temp['company_name'] = str(company_name.text).strip()
            temp['skills'] = str(skills.text).strip()
            temp['posted'] = str(posted_date.text).strip()
            temp['description'] = description
            temp['apply'] = more_info.strip()
            data.append(temp)
        print(data)
        return render(request, 'Scrap_jobs_times.html', {'data': data, "search": keyword})
