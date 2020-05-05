import os
from configparser import ConfigParser


def writeTarget(path):
    targetFile.write("#     " + path + "\n")
    file = open(path, 'r', encoding='UTF-8')
    line = file.readline()
    try:
        while line:
            targetFile.write(line)
            line = file.readline()
    except:
        print("跳过")
    file.close()
    targetFile.write("\n\n\n\n\n\n\n\n\n\n")
    targetFile.write("=================================================\n")


def work(inputPath):
    for i in os.listdir(inputPath):  # 当前目录下的所有文件与文件夹
        path2 = os.path.join(inputPath, i)  # 拼接绝对路径
        if os.path.isdir(path2):  # 判断如果是文件夹,并且是符合的，调用本身
            if i in accept_dir or i not in refuse_dir:  # 这个文件夹再需求名单里面或者不在排除名单里面
                work(path2)
        else:
            if i.split('.')[1] in accept_file and i not in refuse_file:  # 这个文件再需求后缀中并且不是要排除的文件
                writeTarget(path2)


if __name__ == '__main__':
    proDir = os.path.split(os.path.realpath(__file__))[0]
    path = os.path.join(proDir, r"manageCode.conf")
    cp = ConfigParser()
    cp.read(path, encoding='UTF-8')
    projectPATH = cp.get("django", 'project_path')
    OutPATH = cp.get("django", 'output_filename')
    accept_dir = cp.get("django", 'accept_dir').split(',')  # 目标文件夹
    accept_file = cp.get("django", 'accept_file').split(',')  # 目标文件夹
    refuse_file = cp.get("django", 'refuse_file').split(',')  # 不参与工作的文件
    refuse_dir = cp.get("django", 'refuse_dir').split(',')  # 不参与工作的文件夹
    try:
        targetFile = open(OutPATH, 'w')  # 创建输出文件
        work(projectPATH)
        targetFile.close()
    except:
        print("跳过！")
