import tkinter as tk
from tkinter import scrolledtext, messagebox
import csv
from pythainlp.util import arabic_digit_to_thai_digit
from pythainlp.tokenize import word_tokenize, sent_tokenize
import spacy_thai
import pyperclip

S = "การเดินทางตลอดหนึ่งปีที่ผ่านมา เราต้องเจอกับเรื่องราวมากมาย เผชิญหน้ากับเหตุการณ์ไม่คาดคิด และรับมือกับหลายความรู้สึกที่เกาะกุมอยู่ในใจ ด้วยเหตุนี้ ยิ่งใกล้ช่วงท้ายปี หลายคนเลยอยากปล่อยให้ ‘ปีเก่า’ เป็นเรื่องราวของ ‘ปีเก่า’ พร้อมทิ้งเรื่องราวเดิมๆ ไว้ข้างหลังและมุ่งหน้าสู่การเดินทางใหม่ที่กำลังจะมาถึง"

sent_T = sent_tokenize(S)
print(sent_T)

for i in sent_T:
    W = word_tokenize(i)
    print(W)
