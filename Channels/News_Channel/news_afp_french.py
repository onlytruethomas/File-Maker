#!/usr/bin/python
# -*- coding: utf-8 -*-

from newsdownload import download_lobs_french
from newsmake import download_source

download_source("AFP French", "afp_french", "https://rc24.xyz/images/profile_news_afp_french.png", 3, ["008", "009", "010", "011", "012", "013", "014", "015", "016", "017", "018", "019", "020", "021", "022", "023", "024", "025", "026", "027", "028", "029", "030", "031", "032", "033", "034", "035", "036", "037", "038", "039", "040", "041", "042", "043", "044", "045", "046", "047", "048", "049", "050", "051", "052", "065", "066", "067", "074", "076", "077", "078", "079", "082", "083", "088", "094", "095", "096", "098", "105", "107", "108", "110"], download_lobs_french())