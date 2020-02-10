import sys, getopt
from pdfmaker import PdfContensMaker
from utils import *


globalvar_init();
cookiesFile = os.getcwd()+"\\cookies.txt";
if not os.path.exists(cookiesFile):
	exit("cookies.txt文件不存在，请替换cookies_default.txt为cookies.txt。并修改相关参数");
setCookiesFile( cookiesFile );
initUrllib();

if __name__ == "__main__" :
	try:
		opts, args = getopt.getopt(sys.argv[1:],"hi:b:",["help","input=","bid="])
	except getopt.GetoptError:
		print("\n命令行解析错误")
		print("main.py -i <PDF_Files> -b <bid>\n")
		print("你可以通过运行 python main.py -h 来获取命令行参数帮助")
	if (opts[0][0] in ['-i', '--input']) and (opts[1][0] in ['-b', '--bid']):
		inputfile = opts[0][1].strip()
		bid = opts[1][1].strip()
		pdfmaker = PdfContensMaker(inputfile, bid)
		pdfmaker.addBookMarks()
	else:
		print("用法：python main.py -i <PDF_Files> -b <bid>\n")
		print("参数：\n")
		print("    -h, --help 查看此帮助\n" )
		print("    -i, --input 后接你要添加目录的pdf文件\n" )
		print("    -b, --bid 后接你要添加目录的bid编号\n" )
		sys.exit()