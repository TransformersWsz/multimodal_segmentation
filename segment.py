import os
import jieba

def write_file(target_dirpath, filename, content):
    filepath = os.path.join(target_dirpath, filename)
    with open(filepath, "w", encoding="utf8") as fw:
        for item in content:
            fw.write(item)
            fw.write("\n")

def main(dirpath, target_dirpath):
    files = os.listdir(dirpath)
    count = 0
    for filename in files:
        filepath = os.path.join(dirpath, filename)
        content = []
        with open(filepath, "r", encoding="utf8") as fr:
            for line in fr:
                line = line.strip()
                seg_list = jieba.cut(line)
                new_line = " ".join(seg_list)
                content.append(new_line)
            write_file(target_dirpath, filename, content)
            count += 1
            print("{}号文件写入成功".format(count))

if __name__ == "__main__":
    corpus = r"C:\Users\antco\Desktop\corpus"
    target = r"‪C:\Users\antco\Desktop\seg"
    main(corpus, target)