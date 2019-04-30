import untangle

obj = untangle.parse('files/queries.xml')

for topic in obj.root.top:
    print(topic.num.cdata)
    print(topic.title.cdata)
    print(topic.desc.cdata)
    print(topic.narr.cdata)
    print()
