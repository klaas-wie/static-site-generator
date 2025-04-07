
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("subclasses should override")
    
    def props_to_html(self):
        ls = []
        for key in self.props:
            ls.append(f' {key}="{self.props[key]}"')
        
        return ''.join(ls)
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    
