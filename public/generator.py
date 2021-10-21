#!/bin/python3

import os
import yaml
import json
import shutil
import glob
import stat
from ebooklib import epub

note_list = {'total':[], 'list':{}}
article_list = {'total':[], 'list':{}, 'web':{'home':'', 'about':''}}
picture_list = {'total':[], 'list':{}}
ebook_list = {'total':[], 'list':{}}

def read_md_meta(file_path: str) -> dict:
    with open(file_path, 'r') as f:
        yaml_str = ''
        line = f.readline()
        if line == '---\n':
            while line:
                yaml_str += line
                line = f.readline()
                if line == '---\n':
                    break

    return yaml.load(yaml_str, Loader=yaml.BaseLoader)

def note_scan():
    if os.path.exists('article'):
        shutil.rmtree('article')
    os.mkdir('article')

    for root,dirs,files in os.walk("note/"):
        if len(root) > 5 :
            if root[5] == '.': continue
        for file in files:
            file_path = os.path.join(root,file)
            if file_path.split('.')[-1] == 'md':
                head_dic = read_md_meta(os.path.join(root,file))
                if head_dic != None:
                    path = os.path.join(root,file)[5:]
                    head_dic['path'] = path
                    parrent = head_dic['path'].split('/')[0]
                    if head_dic['cover'] != '':
                        head_dic['cover'] = parrent + '/' + head_dic['cover']
                    if parrent not in note_list['list']:
                        note_list['list'][parrent] = []
                    note_list['list'][parrent].append(head_dic)
                    note_list['total'].append(head_dic)

                    # public
                    if head_dic['public'] != 'false':
                        if not os.path.exists('article/' + parrent):
                            os.mkdir("article/" + parrent)

                        # find all pic
                        globs = glob.glob('note/'+path.split('.')[0]+'*')
                        print(path)
                        print(globs)
                        for i in globs:
                            shutil.copy(i, 'article/' + parrent)
                        if parrent not in article_list['list']:
                            article_list['list'][parrent] = []
                        article_list['list'][parrent].append(head_dic)
                        article_list['total'].append(head_dic)

                        if head_dic['public'] == 'home':
                            article_list['web']['home'] = path

                        if head_dic['public'] == 'about':
                            article_list['web']['about'] = path

def picture_scan():
    pass

def read_epub_meta(file_path: str) -> dict:
    ret = {'path':file_path[6:], 'title':'', 'creator':'', 'publisher':'', 'date':'', 'description':''}
    book = epub.read_epub(file_path)
    title = book.get_metadata('DC','title')
    if title:
        ret['title'] = title[0][0]
    creator = book.get_metadata('DC','creator')
    if creator:
        ret['creator'] = creator[0][0]
    publisher = book.get_metadata('DC','publisher')
    if publisher:
        ret['publisher'] = publisher[0][0]
    date = book.get_metadata('DC','date')
    if date:
        ret['date'] = date[0][0]
    description = book.get_metadata('DC','description')
    if description:
        ret['description'] = description[0][0]
    return ret

def ebook_scan():
    for root,dirs,files in os.walk("ebook/"):
        if len(root) > 6 :
            if root[6] == '.': continue
        for file in files:
            file_path = os.path.join(root,file)
            if file_path.split('.')[-1] == 'epub':
                book_dic = read_epub_meta(file_path)
                parrent = root.split('/')[-1]
                if parrent not in ebook_list['list']:
                    ebook_list['list'][parrent] = []
                ebook_list['list'][parrent].append(book_dic)
                ebook_list['total'].append(book_dic)





def print_json():
    with open('note/list.json', 'w') as note_f:
        json.dump(note_list, note_f, indent=4, separators=(',', ':'))
        os.chmod('note/list.json', stat.S_IROTH | stat.S_IWGRP | stat.S_IRGRP | stat.S_IWUSR | stat.S_IRUSR)

    with open('article/list.json', 'w') as article_f:
        json.dump(article_list, article_f, indent=4, separators=(',', ':'))
        os.chmod('article/list.json', stat.S_IROTH | stat.S_IWGRP | stat.S_IRGRP | stat.S_IWUSR | stat.S_IRUSR)

    with open('picture/list.json', 'w') as picture_f:
        json.dump(picture_list, picture_f, indent=4, separators=(',', ':'))
        os.chmod('picture/list.json', stat.S_IROTH | stat.S_IWGRP | stat.S_IRGRP | stat.S_IWUSR | stat.S_IRUSR)

    with open('ebook/list.json', 'w') as ebook_f:
        json.dump(ebook_list, ebook_f, indent=4, separators=(',', ':'))
        os.chmod('ebook/list.json', stat.S_IROTH | stat.S_IWGRP | stat.S_IRGRP | stat.S_IWUSR | stat.S_IRUSR)


if __name__ == "__main__":
    note_scan()
    # picture_scan()
    ebook_scan()

    print_json()
    print(note_list)
    print(ebook_list)

