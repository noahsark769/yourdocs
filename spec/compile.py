import yourdocs

###
# Something about this function.
# @nothing
class MembersOnlyDocSpec(yourdocs.DocSpec):
	def before_start():
		pass

	def before_parse_file(data):
		pass

	def parse_file(filetext):
		# go through the filetext and yield the contants to be parsed by
		# extract_context
		pass

	def after_parse_file(data):
		pass

	def before_extract():
		pass

	def extract_context(content, data):
		# given a content yieled by parse_file,
		pass

	def after_extract():
		pass

	def process_contexts(contexts):
		return contexts

	def render_file(contexts, data):
		pass

	def render_general(data):
		pass


def main():
	spec = MembersOnlyDocSpec()
	spec.compile(content_dir="code", out_dir="docs", ignore_files=["code/old"])

if __name__ == '__main__':
	main()