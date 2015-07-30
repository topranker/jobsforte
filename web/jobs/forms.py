from haystack.forms import SearchForm

class JobsSearchForm(SearchForm):

	def no_query_found(self):
		return self.searchqueryset.all()