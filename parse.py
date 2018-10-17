# -*- coding: utf8 -*-
import re
import json
import codecs

# Some patterns
#p_newitem_jszj = re.compile(r'^[\x80-\xff]{3}\d{4}')
#p_newitem_zmlx = re.compile(r'^\w{2}\d{4}')
p_newitem = re.compile(r'^([\u4e00-\u9fa5]{1,2}|.{2,4})\d{4}')
p_newitemblank = re.compile(r'^\s+')
p_code = re.compile(r'^(([\u4e00-\u9fa5]{1,2}|.{2,4})\d{4})[\s.]*')

# Patterns of title is comple
p_title = re.compile(r'(\d{4})(.+)/')
p_title1 = re.compile(r'(\d{4})(.+)(\xef\xbc\x8f)')
p_title2 = re.compile(r'(\d{4})(.+)(\xc2\xb7\xe2)')
p_title3 = re.compile(r'(\d{4})(.+)')

# Patterns of info
p_info = re.compile(r'(/)(.+)')
p_info2 = re.compile(r'(\xc2\xb7\xe2)(.+)')

# Read the origin data
lines = codecs.open('data.txt','r', 'utf8').readlines()

# Prepare a list for output data
records = []
record = []
# Begin loop
for line in lines:
    # Check the line by pattern
    if p_newitem.match(line) is not None:
        # A new item found, save previous one first
        records.append(record)
        # Create New
        record = []
        record.append(line)
    elif p_newitemblank.match(line) is not None:
        # More info of an item
        record.append(line)
    else:
        # A new type?
        pass

# Last one
records.append(record)
print("* Found %s records" % len(records))

# Create JSON object
books = []
for record in records:
    if record==[]: continue
    # Get every parts
    code = p_code.match(record[0]).group()
    code = code.strip()
    try:
        title = p_title.search(record[0]).group(2)
    except:
        try:
            title = p_title1.search(record[0]).group(2)
        except:
            try:
                title = p_title2.search(record[0]).group(2)
            except:
                title = p_title3.search(record[0]).group(2)
            
    title = title.strip().strip()
    print('* parsed %s %s' % (code, title))
    
    info = ''.join(record)

    # Replace code and title
    info = info.replace(code,'').replace(title,'')

    # create a book document
    book = {'code':code, 'title':title, 'info':info}
    books.append(book)
    
json.dump({'books':books}, open('books.json', 'w'))
print('* dumped!')