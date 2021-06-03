#%%
import xml.dom.minidom
import xml.etree.ElementTree as ET

f = xml.dom.minidom.parse('b.xml')
#%%
root = f.documentElement
#%%
print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)
print(root.ELEMENT_NODE)
#%%
tree = ET.ElementTree(file='b.xml')
root = tree.getroot()

#%%
def delete(string):
    if type(string) == type('0'):
        if '{' in string:
            string = string.split('{')[1].split('}')[1]
    if type(string) == type(dict()):
        d = dict()
        for k,v in string.items():
            d[delete(k)]=delete(v)
        string = d
    return string

def search(element, n):
    print(f"{n*2*' '}>{delete(element.tag)}--{delete(element.attrib)}")
    if len(element)==0:
        print(f"{(n+1)*2*' '}{delete(element.text)}")
    else:
        b = 0
        for e in element:
            if b>=5:
                break
            search(e, n+1)
            b += 1

def decode(element):
    d = dict()
    d[delete(element.tag)]=delete(element.attrib)
    if len(element)==0:
        if 'context' not in d:
            d[delete(element.tag)]['context']=delete(element.text)
        else:
            d[delete(element.tag)]['context0']=delete(element.text)
    else:
        b = 0 
        c = []
        for sub_element in element:
            # if b>=5:
                # break
            c.append(decode(sub_element))
            # b += 1
        d[delete(element.tag)]['childs']=c
    return d


# %%
d = decode(root)

# %%
# %%
