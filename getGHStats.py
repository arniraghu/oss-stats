from github import Github
import csv

#Add GitHub API Token here
g = Github("")
L = []
count = 1

def getHeader():
	L.append([])
	L[0].append("Project")
	L[0].append("Company")
	L[0].append("Category")
	L[0].append("SubCat")
	L[0].append("URL")
	L[0].append("Starcount")
	L[0].append("Subscribers")
	L[0].append("TotalIssues")
	L[0].append("Forks")
	L[0].append("Contributors")
	L[0].append("Releases")
	L[0].append("Pulls")
	L[0].append("TopLanguage")
	L[0].append("GitURL")


def getTopLanguage(repo):
	langDict = repo.get_languages()
	langDictReverse = {}

	largest = 0

	for key in langDict:
		if(langDict[key]> largest):
			largest = langDict[key]
		langDictReverse[langDict[key]] = key

	return (langDictReverse[largest])

def getGHStats(count, row):
	L.append([])
	L[count].append(row[0])
	L[count].append(row[1])
	L[count].append(row[2])
	L[count].append(row[3])
	L[count].append(row[4])
	repo = g.get_repo(row[0])
	L[count].append(repo.stargazers_count)	
	L[count].append(repo.subscribers_count)			
	L[count].append(repo.get_issues(state='all').totalCount)			
	L[count].append(repo.forks_count)			
	L[count].append(repo.get_contributors().totalCount)			
	L[count].append(repo.get_releases().totalCount)			
	L[count].append(repo.get_pulls(state='all').totalCount)
	L[count].append(getTopLanguage(repo))
	L[count].append("https://github.com/"+row[0])	
			
	
getHeader()
with open('gh_projects.csv', 'r') as file:
	reader = csv.reader(file)
	for row in reader:
		if(count == 0):
			 continue;  
		print(row)
		getGHStats(count,row)	
		count =  count+1

f = open('gh_stats.csv', 'w')

with f:
    writer = csv.writer(f)
    for row in L:
        writer.writerow(row)
