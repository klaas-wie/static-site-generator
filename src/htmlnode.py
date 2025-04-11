
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("subclasses should override")
    
    def props_to_html(self):

        if self.props is None:
            return ""

        ls = []
        for key in self.props:
            ls.append(f' {key}="{self.props[key]}"')
        
        return ''.join(ls)
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        
        if self.tag == None:
            return self.value
        
        if self.tag == 'img':
            return f"<{self.tag}{self.props_to_html()}>{self.value}"

        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
            
        # if self.tag == 'a':
        #     return f"<a{self.props_to_html()}>{self.value}</a>"
        
        # return f"<{self.tag}>{self.value}</{self.tag}>"
            
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, children = children, props = props)

    def to_html(self):
        
        if self.tag == None:
            raise ValueError("All parent nodes must have a tag")
        
        if self.children == None:
            raise ValueError("All parent nodes must have children")
        
        children_html = "".join([child.to_html() for child in self.children])
        
        return f"<{self.tag}>{children_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"