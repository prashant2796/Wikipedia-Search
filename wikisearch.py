import wikipedia 
import json 

search = input("Enter your search term: ")

def get_wiki_url(search_list):

	"""
	takes a list of search terms and return a dict
    it contains the term and the wikipedia url
	"""
	wiki_url={curr_term:'http://en.wikipedia.org/wiki/' + curr_term.lower().replace(' ','_') for curr_term in search_list}
	return wiki_url

def get_wiki_data(search):
	 """
    Input: search, a string
    Output: return_data, a dictionary
    Returns page title, page url, page content for search term
    """

	return_data={}

	try:
		search_data = wikipedia.page(search)
		search_summary=wikipedia.summary(search,sentences=3)
		return_data['title'] = search_data.title
		return_data['url'] = search_data.url
		return_data['content'] = search_summary

	except wikipedia.exceptions.DisambiguationError as e:

		approx_links = e.options
		return_data['other_links'] =  get_wiki_url(approx_links)

	return return_data
print(get_wiki_data(search))




