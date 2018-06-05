from scrapy import cmdline

# 用于调试运行代码

def main():
    cmdline.execute(['scrapy', 'crawl', 'top100'])

if __name__ == '__main__':
    main()