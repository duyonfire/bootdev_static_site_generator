class HTMLNode:
	def __init__(self, tag: str = None, value: str = None, children: list["HTMLNode"] = None, props: dict = None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError

	def props_to_html(self):
		if self.props is None:
			return ''
		my_str = ''
		for i in self.props:
			my_str += f' {i}="{self.props[i]}"'
		return my_str

	def __repr__(self):
		return f'HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})'

class LeafNode(HTMLNode):
	def __init__(self, tag: str, value: str, props: dict = None):
		super().__init__(tag, value, None, props)

	def to_html(self):
		if self.value is None:
			raise ValueError("All leaf nodes must have a value")
		if not self.tag:
			return self.value
		my_props = super().props_to_html()
		if len(my_props) != 0:
			return f'<{self.tag}{my_props}>{self.value}</{self.tag}>'
		return f'<{self.tag}>{self.value}</{self.tag}>'

	def __repr__(self):
		return f'LeafNode(tag={self.tag}, value={self.value}, props={self.props})'

class ParentNode(HTMLNode):
	def __init__(self, tag: str, children: list, props: dict = None):
		super().__init__(tag, None, children, props)

	def to_html(self):
		if not self.tag:
			raise ValueError("ParentNode must have a tag")
		if not self.children:
			raise ValueError("ParentNode must have children")
		results = ''
		for i in self.children:
			results += i.to_html()
		return f'<{self.tag}{self.props_to_html()}>{results}</{self.tag}>'
