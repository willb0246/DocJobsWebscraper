# DocJobsWebscraper
Scrape postings on the job board DocJobs


DocJobs is a great website that has job postings for people with MD and PhD. The poblem is that these job postings only last for 90 days, but you might want to keep trask of them for much longer.

This program uses beautiful soup to parse the html of the website, identify the aspects that are worth saving, and then put those into a .txt file.

The aspects that this program saves are:
  1) Title of the post (the title of the role)
  2) The company name
  3) The location that this job is posted for
  4) The email address given to DocJobs (IF there is one given, if not then pass)

The .txt file will be saved with the current date in the title. The program only runs on the most recent page, so make sure to run it relatively frequently (once every month?)
