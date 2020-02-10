import os
import json
import fitz
from utils import *

class PdfContensMaker():
    
    def __init__(self, inputpath, bid, outputpath = "OutputPdf"):
        self.bid = bid
        self.inputPath = inputpath
        mkdir(outputpath)
        self.outputPath = outputpath + "/" +os.path.basename(inputpath)
        self.bookmarks = self.getCatatree()


    def getCatatree( self ):
            url 	 = "https://lib-nuanxin.wqxuetang.com/v1/book/catatree?bid={}".format( self.bid );
            curl 	 = get_value("urllib");
            request  = curl.request.urlopen(url);
            data 	 = request.read().decode("UTF-8");
            cataTree = json.loads( data );
            cataTreeData = cataTree['data'];
            # self.parseCatatree( cataTreeData );
            return cataTreeData;

    def addBookMarks( self ):
        tempPath = self.inputPath;
        filePath = self.outputPath;
        doc = fitz.open( tempPath );
        toc = doc.getToC();
        self.tocAppend( toc, self.bookmarks );
        #new_toc = self.toc_checker(toc)
        doc.setToC(toc);
        doc.save( filePath );
        doc.close();

    def tocAppend( self, toc, lists ):
        for chapter in lists:
            level = int(chapter['level']);
            label = chapter['label'];
            pnum = int(chapter['pnum']);
            toc.append([ level, label, pnum ]);
            if "children" in chapter.keys():
                self.tocAppend( toc, chapter['children'] );

    def toc_checker(self, toc_origin):
        if self.lNumber == 0:
            return toc_origin
        elif self.lNumber == 1:
            new_toc = []
            for title in toc_origin:
                if title[2] > self.end: break
                new_toc.append(title)
        else :
            new_toc = []
            for i,title in enumerate(toc_origin):
                if title[2] > self.end: break
                if title[0] == 1:
                    current_lv1 = i
                if title[2] in range(self.start,self.end+1):
                    new_toc.append(title)
                    new_toc[-1][2] -= self.start
            temp_toc = copy.deepcopy(toc_origin[current_lv1])
            temp_toc[2] = 1
            new_toc = [temp_toc] + new_toc
        return new_toc