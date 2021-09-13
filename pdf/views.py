from logging import log
import threading
import PDFNetPython3
from django.shortcuts import render, resolve_url
from django.http.response import HttpResponse
from django.http.response import JsonResponse
from nltk.data import find

from . models import myuploadfile

from names_dataset import NameDataset 
from names_dataset import NameDatasetV1 

import nltk


from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
import glob
import os
import re
from threading import Timer
import time

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from pdf.serializers import MyUploadFileSerializer

from django.core.files.storage import default_storage





@csrf_exempt
def home(request):
    return render(request, "index.html",)

@csrf_exempt
def Upload(request):
    temps = 20

    def create_redaction(path):
        print("*************create_redact***********", path)


    if request.method == "POST":

        files=os.listdir("media/dossier")
        click=os.listdir("media/clickable")
        redact=os.listdir("media/redact")
        
        for i in range(0,len(files)):
            os.remove("media/dossier"+'/'+files[i])
        for i in range(0,len(click)):
            os.remove("media/clickable"+'/'+click[i])
        for i in range(0,len(redact)):
            os.remove("media/redact"+'/'+redact[i])

        print("files === ", click)
        myfile = request.FILES.getlist("myfiles")
        print("my file == ", myfile)
    
        for f in myfile:
            
            data = os.path.splitext(f.name)
            only_name = data[0]
            extension = data[1]
            if(extension ==".pdf"):
                file_enreg = default_storage.save(f.name, f)

                # Adding the new name
                new_base = only_name + '_clickable' + extension
                # # construct full file path
                new_name = os.path.join("click", new_base)
                # print("data == ", new_name)
                # create_redaction()
                # path = new_base
                create_red = threading.Thread(target=create_redaction, args=[f])
                create_red.start()
                time.sleep(temps+20)

        # print("myfile == ", myfile)
        dossier = glob.glob("media/dossier/*")
        
        print("dossie == ", dossier)
        resultat = []
        # for j in dossier:
        #     output_string = StringIO()

        #     with open(j, 'rb') as in_file:
        #         parser = PDFParser(in_file)
        #         doc = PDFDocument(parser)
        #         print("pFarser ******* ", doc)
        #         rsrcmgr = PDFResourceManager()
        #         device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        #         interpreter = PDFPageInterpreter(rsrcmgr, device)
        #         for page in PDFPage.create_pages(doc):
        #             interpreter.process_page(page)
        #         text = output_string.getvalue()

        #         # print(text)
        #         findEmail = re.findall(r'[\w\.-]+@[\w\.-]+', text)
        #         print("email == ", findEmail)

        #         findNum = re.findall(r'\B(([+]32)|(0032))\s*(\d{1,2})\s*(\d{2,3})\s*(\d{2,3})\s*(\d{2})+', text)
        #         print("numero == ", findNum)
        #         findTVA = re.findall(r'([A-Z]{2})\s{0,1}([0-9]{4})([^A-Za-z0-9_]{0,1})([0-9]{3})([^A-Za-z0-9_]{0,1})([0-9]{3})+', text)
        #         print("TVA == ", findTVA)

        #         findNumPermis = re.findall(r'([1-9]{2})([\s|.]{0,1})(?:1[0-2]|0[0-9]{1})([\s|.]{0,1})([0-9]{2})([\s|.]{0,1})([0-9]{2})([\s|.]{0,1})([0-9]{4})+',text)
        #         print("permis == ", findNumPermis)

        #         findIdEmployeur = re.findall(r'\\b(?:[1-9]{1}[0-9]{11})\\b+', text)
        #         print("id employeur == ", findIdEmployeur)

        #         findCIN = re.findall(r'([0-9]{2})([.])(?:1[0-2]|0([0-9]{1}))[.](?:3[0-1]|0([1-9]{1})|2([0-9]{1}))-([0-9]{3})[.]([0-9]{2})+', text)
        #         print("CIN == ", findCIN)

        #         findNumBancaire = re.findall(r'([A-Z]{2})([0-9]{2})(\s*)((\d{4})(\s*){3})+',text) 
        #         print("Num bancaire == ", findNumBancaire)

        #         findNumPassport = re.findall(r'(([A-Z]{2})([0-9]{6}))+',text) 
        #         print("Num passport == ", findNumPassport)

        #         table_mot=[]
        #         text_tokenize = nltk.word_tokenize(text)
        #         text_tokenize
        #         text_to_string = " "
        #         for text in text_tokenize:
        #             text_to_string += text + " "
        #         text_tagged = nltk.pos_tag(text_tokenize)
        #         for text in text_tagged:
        #             if text[1]=='NNP':
        #                 table_mot.append(text[0])


        #         m=NameDatasetV1()
        #         mot_cherche = []
        #         for tbl in table_mot:
        #             if m.search_first_name(tbl):
        #                 mot_cherche.append(tbl)
        #         resultat.append(mot_cherche)
        #         print("mot_cherche  ", mot_cherche)

        return JsonResponse("resultat",safe=False)
































































        # files=os.listdir("media")
        # for i in range(0,len(files)):
        #     os.remove("media"+'/'+files[i])
        
        
        # myfile = request.FILES.getlist("files")

        # for f in myfile:
            # myuploadfile(myfiles=f).save()

        # output_string = StringIO()
        # with open('test1.pdf', 'rb') as in_file:
        #     parser = PDFParser(in_file)
        #     doc = PDFDocument(parser)
        #     rsrcmgr = PDFResourceManager()
        #     device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        #     interpreter = PDFPageInterpreter(rsrcmgr, device)
        #     for page in PDFPage.create_pages(doc):
        #         interpreter.process_page(page)
        # text = output_string.getvalue()

        # ligne = text.splitlines()

        # dossier = glob.glob("media/*")

        # for j in dossier:
            
        #     output_string = StringIO()
        #     with open(j, 'rb') as in_file:
        #         parser = PDFParser(in_file)
        #         doc = PDFDocument(parser)
        #         rsrcmgr = PDFResourceManager()
        #         device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        #         interpreter = PDFPageInterpreter(rsrcmgr, device)
        #         for page in PDFPage.create_pages(doc):
        #             interpreter.process_page(page)
        #         text = output_string.getvalue()

                
        #         table_mot=[]
        #         text_tokenize = nltk.word_tokenize(text)
        #         text_tokenize
        #         text_to_string = " "
        #         for text in text_tokenize:
        #             text_to_string += text + " "
        #         text_tagged = nltk.pos_tag(text_tokenize)
        #         for text in text_tagged:
        #             if text[1]=='NNP':
        #                 table_mot.append(text[0])


        #         m=NameDatasetV1()
        #         mot_cherche = []
        #         for tbl in table_mot:
        #             if m.search_first_name(tbl):
        #                 mot_cherche.append(tbl)
        #         # resultat.append(mot_cherche)
        #         # print("mot_cherche  ", mot_cherche)

        # return JsonResponse(resultat, safe = False)
        # return render(resultat, safe = False)
        

