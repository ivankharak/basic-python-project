#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# script by Ruchir Chawdhry
# released under MIT License
# github.com/RuchirChawdhry/Python
# ruchirchawdhry.com
# linkedin.com/in/RuchirChawdhry

from selectolax.parser import HTMLParser
import urllib.request
import re
from more_itertools import filter_except
from itertools import zip_longest
import csv


def page_source(url):
    s = urllib.request.urlopen(url).read()
    return s


def book_images(html):
    img = [node.attributes.get("src") for node in HTMLParser(html).css("img.thumbnail")]
    return img


def book_titles(html):
    titles = [node.attributes.get("title") for node in HTMLParser(html).css("h3 > a")]
    return titles


def book_price(html):
    prices = [node.text() for node in HTMLParser(html).css("p.price_color")]
    return prices


def in_stock(html):
    stock_status = [node.text() for node in HTMLParser(html).css("p.instock")]
    stock_status = [re.sub(r"\W", "", i) for i in stock_status]
    return stock_status


def book_href(html):
    links = [
        node.attributes.get("href")
        for node in HTMLParser(html).css("div.image_container > a")
    ]
    return links


def book_rating(html):
    ratings = [
        node.attributes.get("class").strip("star-rating ")
        for node in HTMLParser(html).css("p.star-rating")
    ]
    return ratings


def page_href(html):
    last_page = HTMLParser(html).css_first("ul.pager > li.current").text().split(" ")
    last_page = [re.sub(r"\s", "", i) for i in last_page]
    last_page = list(filter_except(int, last_page, ValueError))
    pages = [
        f"http://books.toscrape.com/catalogue/page-{i}.html"
        for i in range(1, int(last_page[1]) + 1)
    ]
    return pages


def stock_num(html):
    num = HTMLParser(html).css_first("p.availability").text()
    num = re.sub(r"\D", "", num)
    return num


def product_desc(html):
    desc = HTMLParser(html).css_first("article > p").text()
    return desc


def product_info(html):
    d = {}
    d["upc"] = HTMLParser(html).css_first("table > tbody > tr:nth-child(1) > td").text()
    d["product_type"] = (
        HTMLParser(html).css_first("table > tbody > tr:nth-child(2) > td").text()
    )
    d["price_wo_tax"] = (
        HTMLParser(html).css_first("table > tbody > tr:nth-child(3) > td").text()
    )
    d["price_w_tax"] = (
        HTMLParser(html).css_first("table > tbody > tr:nth-child(4) > td").text()
    )
    d["tax"] = HTMLParser(html).css_first("table > tbody > tr:nth-child(5) > td").text()
    d["availability"] = (
        HTMLParser(html).css_first("table > tbody > tr:nth-child(6) > td").text()
    )
    d["reviews_num"] = (
        HTMLParser(html).css_first("table > tbody > tr:nth-child(7) > td").text()
    )
    return d


def book_cat(html):
    cat = HTMLParser(html).css_first("ul.breadcrumb").text().splitlines()
    cat = [re.sub(r"\s", "", i) for i in cat]
    cat = list(filter(None, cat))
    return cat[1:3]

if __name__ == "__main__":
    main = "http://books.toscrape.com/"
    html = page_source(main)
    with open("books.csv", "w", newline="") as f:
        for _, page in enumerate(page_href(html)):
            print(page)
            phtml = page_source(page)
            rows = [
                book_href(phtml),
                book_titles(phtml),
                book_price(phtml),
                in_stock(phtml),
                book_rating(phtml),
            ]
            export_data = zip_longest(*rows, fillvalue="")
            writer = csv.writer(f)
            writer.writerows(export_data)
