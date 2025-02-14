#!/usr/bin/env python3
import pandas as pd
from urllib.parse import urljoin
import scrapy
import re
import os
from scrapy.crawler import CrawlerProcess
class PaperCrawler(scrapy.Spider):
    name = 'paperSpider'
    start_urls = ['https://papers.nips.cc']

    def parse(self, response):
        for link in response.css('div ul li a::attr(href)').getall():
            yield scrapy.Request(response.urljoin(link), callback=self.parseYears)
    
    def parseYears(self, response):
        for link in response.css('div ul li a::attr(href)').getall():
            yield scrapy.Request(response.urljoin(link), callback=self.parsePapers)
    
    def parsePapers(self, response):
        link = response.css('div div div a.btn.btn-primary.btn-spacer::attr(href)').get()
        year = re.search(r'/(\d{4})/', link).group(1) if link else "unknown"
        title = response.css('div div h4::text').get().strip()
        # abstract = response.css('div.container-fluid div.col p:nth-last-of-type(1) *::text').getall()
        # full_text = ' '.join(abstract).strip() 
        safe_title = re.sub(r'[^\w\-/]', '_', title)
        path = f"{year}/{safe_title}"
        # self.save_to_excel(title, full_text)
        yield scrapy.Request(
            url=urljoin('https://papers.nips.cc', link),
            callback=self.parseSave,
            meta={'filename': path}
        )

    def save_to_excel(self, title, abstract):
        file_path = os.path.join(os.getcwd(), "papers.xlsx")
        df = pd.DataFrame([[title, abstract]], columns=["Title", "Abstract"])
        if not os.path.exists(file_path):
            df.to_excel(file_path, index=False, engine="openpyxl")
            print(f"New Excel file created: {file_path}")
        else:
            with pd.ExcelWriter(file_path, mode="a", if_sheet_exists="overlay", engine="openpyxl") as writer:
                df.to_excel(writer, index=False, header=False, startrow=writer.sheets["Sheet1"].max_row)
            print(f"Data appended to: {file_path}")

    def parseSave(self, response):
        path = response.meta.get('filename', 'default_filename')
        safe_path = re.sub(r'[^\w\-/]', '_', path)
        file_path = os.path.join(os.getcwd(), f"{safe_path}.pdf")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as f:
            f.write(response.body)


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(PaperCrawler)
    process.start()
