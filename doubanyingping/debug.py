from scrapy import cmdline

# 用于调试运行代码

def main():
    cmdline.execute(['scrapy', 'crawl', 'yingping'])

if __name__ == '__main__':
    main()