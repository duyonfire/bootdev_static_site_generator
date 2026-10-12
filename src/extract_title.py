def extract_title(markdown: str) -> str:
	lines = markdown.split("\n")
	text = ''
	for line in lines:
		if line.startswith('# '):
			text = line.lstrip('#').strip()
			if text:
				return text
	raise Exception("No H1 header found")
