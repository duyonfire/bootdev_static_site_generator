def markdown_to_blocks(markdown: str):
	split_markdown = markdown.split('\n\n')
	final_list: list[str] = []
	for i in split_markdown:
		i = i.strip()
		if len(i) != 0:
			final_list.append(i)
	return final_list
