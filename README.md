# libreoffice-bangla-converter-macros

## Overview
Macros to convert between Unicode and ANSI in Bangla in [LibreOffice](https://www.libreoffice.org/)

## Requirement
1. Python (Tested with v3.8)
2. [Bijoy2Unicode](https://github.com/Mad-FOX/bijoy2unicode) (Tested with v0.1.1)

## Usage
1. Download the repo
2. Run the script (Root permission required) (

Now try using it
1. Open a document with LibreOffice
2. Write something in Unicode or ANSI
3. Select it 
3. Click  
  > Tools => Macros => Run a macro => LibreOffice Macros => BangalConv => ToANSI/ToUni
 
 ## Known issue
 LibreOffice automatically select bangla font for unicode but when using ASCI, the font need to be manually converted. [Here](https://www.omicronlab.com/bangla-fonts.html) you can get some ANSI fonts.

